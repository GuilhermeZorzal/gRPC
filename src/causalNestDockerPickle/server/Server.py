from concurrent import futures
import grpc
import pickle
from grpc import StatusCode

import teste_pb2 as grpc_methods
import teste_pb2_grpc as grpc_types
# import serializer_pb2 as grpc_methods
# import serializer_pb2_grpc as grpc_types

from causal_nest.dataset import (
    Problem,
    RefutationResult,
    IdentifiedEstimand,
    CausalEstimate,
    EstimationResult,
    DiscoveryResult,
    MissingDataHandlingMethod,
    create_mock_graph,
    FeatureType,
    Dataset,
    handle_missing_data,
    FeatureTypeMap,
    estimate_feature_importances,
    applyable_models,
    discover_with_all_models,
    discover_with_model,
    estimate_all_effects,
    estimate_model_effects,
    refute_all_results,
    refute_estimation,
    generate_result_graph,
    generate_all_results,
    parse_knowledge_file,
)


class CausalNestServicer(grpc_types.SerializerServicer):
    def Teste(self, request, context):
        return grpc_methods.SerialData(errorMessage="Nada")

    def Discovery(self, request, context):
        obj = pickle.loads(request.data)
        if not obj:
            return grpc_methods.SerialData(errorMessage="Problem não foi informado")

        # Funcao
        problem = discover_with_all_models(obj, max_seconds_model=0.9)

        if not problem:
            return context.abort(
                StatusCode.FAILED_PRECONDITION, f"Fase de refutacao nao realizada"
            )
        obj = pickle.dumps(problem)
        return grpc_methods.SerialData(data=obj)

    def Estimation(self, request, context):
        obj = pickle.loads(request.data)
        if not obj:
            print("deu erro")
            return grpc_methods.SerialData(errorMessage="Problem não foi informado")

        # Funcao
        problem = estimate_all_effects(obj)

        if not problem:
            return context.abort(
                StatusCode.FAILED_PRECONDITION, f"Fase de refutacao nao realizada"
            )
        obj = pickle.dumps(problem)
        return grpc_methods.SerialData(data=obj)

    def Refutation(self, request, context):
        obj = pickle.loads(request.data)
        if not obj:
            return grpc_methods.SerialData(errorMessage="Problem não foi informado")

        # Funcao
        problem = refute_all_results(obj)

        if not problem:
            return context.abort(
                StatusCode.FAILED_PRECONDITION, f"Fase de refutacao nao realizada"
            )
        obj = pickle.dumps(problem)
        return grpc_methods.SerialData(data=obj)

    def Graphs(self, request, context):
        obj = pickle.loads(request.data)
        if not obj:
            return grpc_methods.SerialData(errorMessage="Problem não foi informado")

        # Funcao
        problem = generate_all_results(obj)

        if not problem:
            return context.abort(
                StatusCode.FAILED_PRECONDITION, f"Fase de refutacao nao realizada"
            )
        obj = pickle.dumps(problem)
        return grpc_methods.SerialData(data=obj)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_types.add_SerializerServicer_to_server(CausalNestServicer(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    print("Calculator server running on port 8000")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
