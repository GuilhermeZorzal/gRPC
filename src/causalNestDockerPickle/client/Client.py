import grpc
import os

# import calculator_pb2
# import calculator_pb2_grpc
import pickle
# import serializer_pb2 as grpc_methods
# import serializer_pb2_grpc as grpc_types

import teste_pb2 as grpc_methods
import teste_pb2_grpc as grpc_types

import causal_nest as cn
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

# channel = grpc.insecure_channel("localhost:8000")
channel = grpc.insecure_channel("server:8000")
stub = grpc_types.SerializerStub(channel)


def grpc_discovery_results(problem):
    obj = pickle.dumps(problem)
    response = stub.Discovery(grpc_methods.SerialData(data=obj))
    if not hasattr(response, "data") or not response.data:
        print("Erro:", response.errorMessage)
        return problem

    problemBack = pickle.loads(response.data)
    print("Funcionou discovery!!")
    return problemBack


def grpc_estimate_all_effects(problem):
    obj = pickle.dumps(problem)
    response = stub.Estimation(grpc_methods.SerialData(data=obj))
    if not hasattr(response, "data") or not response.data:
        print("Erro:", response.errorMessage)
        return problem

    problemBack = pickle.loads(response.data)
    print("Funcionou estimation!!")
    return problemBack


def grpc_refute_all_results(problem):
    obj = pickle.dumps(problem)
    response = stub.Refutation(grpc_methods.SerialData(data=obj))
    if not hasattr(response, "data") or not response.data:
        print("Erro:", response.errorMessage)
        return problem

    problemBack = pickle.loads(response.data)
    print("Funcionou refutation!!")
    return problemBack


def grpc_generate_all_results(problem):
    obj = pickle.dumps(problem)
    response = stub.Graphs(grpc_methods.SerialData(data=obj))
    if not hasattr(response, "data") or not response.data:
        print("Erro:", response.errorMessage)
        return problem

    problemBack = pickle.loads(response.data)
    print("Funcionou geracao dos grafos!!")
    return problemBack


def run():
    problem = None
    teste = stub.Teste(grpc_methods.SerialData())
    print(teste)
    try:
        dataset = Dataset(data="path", target="cilinders", feature_mapping="objeto")
        problem = Problem(
            dataset=dataset,
            description="analise de teste",
            knowledge="teste2",
        )
        problem = grpc_discovery_results(problem)
        problem = grpc_estimate_all_effects(problem)
        problem = grpc_refute_all_results(problem)
        problem = grpc_generate_all_results(problem)
    except ValueError:
        print("Please enter valid numbers!")
    except grpc.RpcError as e:
        print(f"RPC Error: {e.code()}: {e.details()}")
    except KeyboardInterrupt:
        print("\nExiting...")
    print("FUNCIONOU TUDO")
    return
    while True:
        try:
            print("Choose the operation:")
            print(" - 1. Create Problem ")
            print(" - 2. Run Discovery")
            print(" - 3. Run Estimation")
            print(" - 4. Run Refutation")
            print(" - 5. Show Graph Results")
            print(" - 6. print:")

            op = input("\nEnter operation: ")
            os.system("clear")
            match op:
                case "1":
                    dataset = Dataset(
                        data="path", target="cilinders", feature_mapping="objeto"
                    )
                    problem = Problem(
                        dataset=dataset,
                        description="analise de teste",
                        knowledge="teste2",
                    )
                    continue
                case "2":
                    problem = grpc_discovery_results(problem)
                    continue
                case "3":
                    problem = grpc_estimate_all_effects(problem)
                    continue
                case "4":
                    problem = grpc_refute_all_results(problem)
                    continue
                case "5":
                    problem = grpc_generate_all_results(problem)
                    continue
                case "6":
                    print("  - 1. Discovery")
                    print("  - 2. Estimation")
                    print("  - 3. Refutation")
                    print("  - 4. Graph Results")
                    op = input("\nEnter operation: ")
                    match op:
                        case "1":
                            print(problem.discovery_results)
                            continue
                        case "2":
                            print(problem.estimation_results)
                            continue
                        case "3":
                            print(problem.refutation_results)
                            continue
                        case "4":
                            print(problem)
                            continue
                    continue
        except ValueError:
            print("Please enter valid numbers!")
        except grpc.RpcError as e:
            print(f"RPC Error: {e.code()}: {e.details()}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    run()
