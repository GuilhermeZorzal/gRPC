from concurrent import futures
import grpc
import pickle

import serializer_pb2 as grpc_methods
import serializer_pb2_grpc as grpc_types

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
    def Discovery(self, request, context):
        print("teste serial")
        obj = pickle.loads(request.data)
        problem = discover_with_all_models(obj, max_seconds_model=0.9)
        obj = pickle.dumps(problem)
        print("type", type(obj))
        return grpc_methods.SerialData(data=obj)

    def Estimation(self, request, context):
        print("teste serial")
        obj = pickle.loads(request.data)
        problem = estimate_all_effects(obj, max_seconds_model=0.9)
        obj = pickle.dumps(problem)
        print("type", type(obj))
        return grpc_methods.SerialData(data=obj)

    def Refutation(self, request, context):
        print("teste serial")
        obj = pickle.loads(request.data)
        problem = refute_all_results(obj, max_seconds_model=0.9)
        obj = pickle.dumps(problem)
        print("type", type(obj))
        return grpc_methods.SerialData(data=obj)

    def Graphs(self, request, context):
        print("teste serial")
        obj = pickle.loads(request.data)
        problem = generate_all_results(obj, max_seconds_model=0.9)
        obj = pickle.dumps(problem)
        print("type", type(obj))
        return grpc_methods.SerialData(data=obj)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_types.add_SerializerServicer_to_server(CausalNestServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Calculator server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
