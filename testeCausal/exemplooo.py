import os
import json
from typing import Any, final

import pandas as pd
from flask import Blueprint
from flask import jsonify
from flask import request

from ciw_backend.extensions import db
from ciw_backend.utils.token import autorization
from ciw_backend.utils.verificacao import *

# Models
from ciw_backend.models import DataSet as ModelsDataSet
from ciw_backend.models import Analysis as ModelsAnalysis
from ciw_backend.models import DiscoveryResults as ModelsDiscoveryResults
from ciw_backend.models import EstimationResults as ModelsEstimationResults
from ciw_backend.models import RefutationResults as ModelsRefutationResults

# Causal Nest
from ciw_backend.causal_nest.dataset import (
    DiscoveryResult,
    MissingDataHandlingMethod,
    FeatureType,
    Problem,
    Dataset,
    generate_all_results,
    handle_missing_data,
    FeatureTypeMap,
    estimate_feature_importances,
    applyable_models,
    discover_with_all_models,
    estimate_all_effects,
    refute_all_results,
    generate_result_graph,
    parse_knowledge_file,
)

UPLOAD_FOLDER = "/app/ciw_backend/temp/ConfigFiles/"

results_full_blueprint = Blueprint("results_full", __name__, url_prefix="/results")


def find_estimation(treatment, analysis_id, estimation_ids, i, model):
    # based on the model and the treatment, we can find the estimation
    id_estimation = None
    for j in estimation_ids:
        if j.treatment == treatment:
            id_estimation = j.id
            break

    return id_estimation


def nome_config_igual(filename, user_id):
    name, ext = os.path.splitext(filename)
    cont = 1

    vetDataset = ModelsAnalysis.query.filter_by(user_id=user_id).all()

    if not vetDataset:
        return filename

    nomeUtilizados = {dataset.name for dataset in vetDataset}

    while filename in nomeUtilizados:
        filename = f"{name}({cont}){ext}"
        cont += 1

    return filename


def create_final_results(problem):
    final_results = {}
    # TODO : caso haja necessidade de retornar o problema ao usuario, tem que arrumar isso aqui
    # serialized_obj = {}
    # for key, value  in problem.__dict__.items():
    #     serialized_obj.update({key: value})
    # final_results.update({"problem": serialized_obj})

    sorted_results = list(
        sorted(
            filter(lambda x: x, problem.discovery_results.values()),
            key=lambda x: x.priority_score,
            reverse=True,
        )
    )

    # sorted_results = list(sorted(filter(lambda x: x,
    #                                     problem.discovery_results.values()),
    #                                     key=lambda x: x.priority_score,
    #                                     reverse=True))
    # # Discovery
    sorted_vector = []
    for values in sorted_results:
        aux = {}
        for key, value in values.__dict__.items():
            aux.update({key: value})
        sorted_vector.append(aux)
    final_results.update({"discovery_results_ordered": sorted_vector})

    serialized_obj = {}
    for key, value in problem.discovery_results.items():
        if value == None:
            # Nenhuma descoberta realizada")
            continue
        serialized_obj.update({key: value.__dict__})
    final_results.update({"discovery_results": serialized_obj})

    # Estimation
    serialized_obj = {}
    for key, values in problem.estimation_results.items():
        vector = []
        for value in values:
            vector.append(value.__dict__)
        serialized_obj.update({key: vector})
    final_results.update({"estimation_results": serialized_obj})

    # Refutation
    serialized_obj = {}
    for key, values in problem.refutation_results.items():
        vector = []
        for value in values:
            vector.append(value.__dict__)
        serialized_obj.update({key: vector})
    final_results.update({"refutation_results": serialized_obj})

    return final_results


def upload_config(id):
    file = request.files["configFile"]
    print("upload_txt >>> ", file)
    print("upload_txt >>> ", file.filename)

    if not file or file.filename == "" or not file.filename.endswith(".csv"):
        print("sem arquivo de configuração")
        return (
            jsonify(
                {
                    "mensagem": "Sem arquivo de configuração. Precisa tratar",
                    "field": "file",
                }
            ),
            200,
        )

    # return (
    #     jsonify(
    #         {"mensagem": "Arquivo enviado: necessario arrumar armazenamento de arquivo temporario", "field": "file"}
    #     ),
    #     200,
    # )
    user_folder = os.path.join(UPLOAD_FOLDER, id)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    filename = nome_config_igual(file.filename, id)

    try:
        file_path = os.path.join(user_folder, filename)
        file.save(file_path)

        # Calcula o tamanho do arquivo
        size_bytes = os.path.getsize(file_path)

        # Guarda o tamanho do arquivo em KB
        size_kb = size_bytes / 1024

        return (
            jsonify(
                {
                    "mensagem": "Arquivo CSV carregado com sucesso",
                    "size": size_kb,
                    "name": filename,
                    "file_path": file_path,
                }
            ),
            200,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "mensagem": f"Erro ao processar o arquivo CSV: {str(e)}",
                    "field": "file",
                }
            ),
            400,
        )


def storing_data_database(problem, analysis_id, final_results):
    # Adicionando o problema à tabela de análise original
    print("CRIANDO BANCO DE DADOS")
    analysis_updater = ModelsAnalysis.query.filter_by(id=analysis_id).first()
    analysis_updater.problem = problem
    analysis_updater.save()

    # Causal Discovery
    discoverys = []
    for key, value in problem.discovery_results.items():
        if value == None:
            print("Fase de Discovery: Nenhuma descoberta realizada")
            continue

            # FIXME: o discovery_results não possui reason. Precisa ser adicionado
        newDiscovery = ModelsDiscoveryResults(
            analysis_id=analysis_id,
            model=value.model,
            output_graph=value.output_graph,
            auc_pr=value.auc_pr,
            shd=value.shd,
            runtime=value.runtime,
            priority_score=value.priority_score,
            knowledge_integrity_score=value.knowledge_integrity_score,
            forbidden_edges_violation_rate=value.forbidden_edges_violation_rate,
            required_edges_compliance_rate=value.required_edges_compliance_rate,
            reason=None,
            problem=problem,
        )
        # Salvando
        newDiscovery.save()

        # Uma vez que o objeto é salvo no banco de dados, o sqlalchemy atualiza o objeto, adicionando o id
        discoverys.append(newDiscovery)

    estimation_ids = []
    # Estimation
    for key, values in problem.estimation_results.items():
        if values == None:
            print("Fase de Estimation: Nenhuma estimativa realizada")
            continue

        id_discovery = None

        # Encotrando o id da descoberta
        for i in discoverys:
            # print("I >>>", i.model, key)
            if i.model == key:
                id_discovery = i.id
                break

        if id_discovery == None:
            print("Nenhum dos algoritmos de descoberta deram resultado")
            continue

        for value in values:
            newEstimation = ModelsEstimationResults(
                discovery_id=id_discovery,
                model=value.model,
                treatment=value.treatment,
                estimand=value.estimand,
                estimate=value.estimate,
                control_value=value.control_value,
                treatment_value=value.treatment_value,
                p_value=value.p_value,
                analysis_id=analysis_id,
                problem=problem,
            )
            # Salvando
            newEstimation.save()
            estimation_ids.append(newEstimation)

    # Refutation
    for dis_model, values in problem.refutation_results.items():
        for i in values:
            if values == None:
                print("Fase de Refutation: Nenhuma refutação realizada")
                continue
            treatment = i.treatment
            # print("TREATMENT >>>", treatment, "MODEL >>>", dis_model)
            # based on the model and the treatment, we can find the estimation
            id_estimation = find_estimation(
                treatment, analysis_id, estimation_ids, i, dis_model
            )

            newRefutation = ModelsRefutationResults(
                estimation_id=id_estimation,
                analysis_id=analysis_id,
                model=i.model,
                model_discovery=dis_model,
                p_value=i.p_value,
                estimated_effect=i.estimated_effect,
                new_effect=i.new_effect,
                runtime=i.runtime,
                passed=i.passed,
                treatment=treatment,
                problem=problem,
            )
            # print(newRefutation.__dict__)
            # Salvando
            newRefutation.save()

    return True


@results_full_blueprint.route(
    "full/<user_id>/<analysis_id>", methods=["GET", "OPTIONS"]
)
def full(user_id, analysis_id):
    print(user_id, analysis_id)
    # General Information about the analysis
    if request.method == "OPTIONS":
        print("teste")
        return jsonify({"message": "OPTIONS"}), 200

    # TODO: Conferir os campos obrigatórios da análise

    final_results = {}

    full_analysis = ModelsAnalysis.query.filter_by(
        user_id=user_id, id=analysis_id
    ).first()

    if full_analysis is None:
        return jsonify({"message": "Analysis not found"}), 404

    # Extracting analysis data
    full_analysis = {
        column.name: getattr(full_analysis, column.name)
        for column in full_analysis.__table__.columns
    }

    analysis_id = full_analysis["id"]
    analysis_name = full_analysis["name"]
    analysis_description = full_analysis["description"]
    analysis_created_at = full_analysis["created_at"]
    analysis_user_id = full_analysis["user_id"]
    analysis_dataset_id = full_analysis["dataset_id"]
    analysis_config_file_path = full_analysis["config_file_path"]
    analysis_response_time = full_analysis["response_time"]
    analysis_discovery_timeout = full_analysis["discovery_timeout"]
    analysis_estimation_timeout = full_analysis["estimation_timeout"]
    analysis_refutation_global_timeout = full_analysis["refutation_global_timeout"]
    analysis_refutation_model_timeout = full_analysis["refutation_model_timeout"]
    analysis_target_variable = full_analysis["target_variable"]
    analysis_feature_selection = full_analysis["feature_selection"]
    analysis_feature_types = full_analysis["feature_types"]

    # Extracting dataset data
    full_dataset = ModelsDataSet.query.filter_by(
        user_id=user_id, id=full_analysis["dataset_id"]
    ).first()
    full_dataset = {
        column.name: getattr(full_dataset, column.name)
        for column in full_dataset.__table__.columns
    }

    dataset_file_path = full_dataset["file_path"]

    # ████████╗██╗███╗   ███╗███████╗
    # ╚══██╔══╝██║████╗ ████║██╔════╝
    #    ██║   ██║██╔████╔██║█████╗
    #    ██║   ██║██║╚██╔╝██║██╔══╝
    #    ██║   ██║██║ ╚═╝ ██║███████╗
    #    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
    filed_all_fields = (
        analysis_discovery_timeout
        and analysis_estimation_timeout
        and analysis_refutation_global_timeout
        and analysis_refutation_model_timeout
    )
    filed_some_field = (
        analysis_discovery_timeout
        or analysis_estimation_timeout
        or analysis_refutation_global_timeout
        or analysis_refutation_model_timeout
    )

    if analysis_response_time and filed_some_field:
        # The user filed both the general response time and one of the other camps.
        return (
            jsonify(
                {
                    "message": "Conflicting Fields. If responseTime is filed, the other shouldn't be",
                    "field": "form",
                }
            ),
            404,
        )

    if not analysis_response_time and not filed_all_fields:
        # The user dont filed the response time, nor filed all the other fields
        return (
            jsonify(
                {
                    "message": "Conflicting Fields. If responseTime is not filed, the other shouldn be",
                    "field": "form",
                }
            ),
            404,
        )
    if analysis_response_time:
        # FIXME: retrieve the time configuration from the env
        # DISCOVERY_TIME_PERCENTAGE = os.getenv("DISCOVERY_TIME_PERCENTAGE", None)
        DISCOVERY_TIME_PERCENTAGE = 0.8
        divided_time = (
            1 - DISCOVERY_TIME_PERCENTAGE
        ) / 3  # Dividing the remaining time into 3 equal parts
        analysis_discovery_timeout = DISCOVERY_TIME_PERCENTAGE * analysis_response_time
        analysis_estimation_timeout = analysis_response_time * divided_time
        analysis_refutation_global_timeout = analysis_response_time * divided_time
        analysis_refutation_model_timeout = analysis_response_time * divided_time

    # FIXME: All the info below are placeholders. Need to be fixed
    missing_data_handler = MissingDataHandlingMethod.FORWARD_FILL
    feature_type = FeatureType.CONTINUOUS

    knowledge = parse_knowledge_file(analysis_config_file_path)

    df = pd.read_csv(dataset_file_path)

    # Convertendo o feature mapping para o formato correto
    feature_mapping = []
    feature_types_json = json.loads(analysis_feature_types)
    for i in df.drop(analysis_target_variable, axis=1).columns:
        if i in feature_types_json:
            if i in [
                FeatureType.CONTINUOUS,
                FeatureType.DISCRETE,
                FeatureType.CATEGORICAL,
            ]:
                feature_mapping.append(
                    FeatureTypeMap(feature=i, type=feature_types_json[i])
                )
        else:
            feature_mapping.append(
                FeatureTypeMap(feature=i, type=FeatureType.IGNORABLE)
            )

        # A analise é submetida as modelos de discovery, gerando diferentes discoverys : analysis -> model
        # Cada modelo de discovery é estimado com uma feature diferente, gerando diferentes estimations: model -> feature
        # Cada estimation é refutation_results com diferentes modelos, gerando diferentes refutations: feature -> modelo
        #

    # Creating the dataset
    #  ____        _                 _
    # |  _ \  __ _| |_ __ _ ___  ___| |_ ___
    # | | | |/ _` | __/ _` / __|/ _ \ __/ __|
    # | |_| | (_| | || (_| \__ \  __/ |_\__ \
    # |____/ \__,_|\__\__,_|___/\___|\__|___/
    #

    dataset = Dataset(
        data=dataset_file_path,
        target=analysis_target_variable,
        feature_mapping=feature_mapping,
    )
    dataset = handle_missing_data(dataset, missing_data_handler)
    dataset = estimate_feature_importances(dataset)

    # Considerando que a classe é capaz de tratar os casos em que o knowledge é None
    problem = Problem(
        dataset=dataset, description=analysis_description, knowledge=knowledge
    )

    if full_analysis is None:
        return jsonify({"message": "Analysis not found"}), 404

    # Discovery
    #  ____  _
    # |  _ \(_)___  ___ _____   _____ _ __ _   _
    # | | | | / __|/ __/ _ \ \ / / _ \ '__| | | |
    # | |_| | \__ \ (_| (_) \ V /  __/ |  | |_| |
    # |____/|_|___/\___\___/ \_/ \___|_|   \__, |
    #                                      |___/
    models = applyable_models(problem)
    final_results.update({"models": models})

    problem = discover_with_all_models(
        problem, max_seconds_model=analysis_discovery_timeout
    )

    # Estimation
    #            _   _                 _   _
    #   ___  ___| |_(_)_ __ ___   __ _| |_(_) ___  _ __
    #  / _ \/ __| __| | '_ ` _ \ / _` | __| |/ _ \| '_ \
    # |  __/\__ \ |_| | | | | | | (_| | |_| | (_) | | | |
    #  \___||___/\__|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|
    #
    problem = estimate_all_effects(
        problem, verbose=True, max_seconds_model=analysis_estimation_timeout
    )

    # Refutation
    #            __       _        _   _
    #  _ __ ___ / _|_   _| |_ __ _| |_(_) ___  _ __
    # | '__/ _ \ |_| | | | __/ _` | __| |/ _ \| '_ \
    # | | |  __/  _| |_| | || (_| | |_| | (_) | | | |
    # |_|  \___|_|  \__,_|\__\__,_|\__|_|\___/|_| |_|
    #
    problem = refute_all_results(
        problem,
        max_seconds_global=analysis_refutation_global_timeout,
        max_seconds_model=analysis_refutation_model_timeout,
    )

    # Grafos
    #
    #   ____                 _
    #  / ___|_ __ __ _ _ __ | |__  ___
    # | |  _| '__/ _` | '_ \| '_ \/ __|
    # | |_| | | | (_| | |_) | | | \__ \
    #  \____|_|  \__,_| .__/|_| |_|___/
    #                 |_|
    graphs = generate_all_results(problem)
    final_results.update({"graphs": graphs})

    # Storing the results on db
    #  ____  ____
    # |  _ \| __ )
    # | | | |  _ \
    # | |_| | |_) |
    # |____/|____/
    #
    storing_db = storing_data_database(problem, analysis_id, final_results)
    if not storing_db:
        return jsonify(
            {"message": "Erro ao salvar os resultados no banco de dados"}
        ), 500

    final_results.update(create_final_results(problem))

    return (
        jsonify(final_results),
        200,
    )
