from concurrent import futures
import grpc

# import calculator_pb2
# import calculator_pb2_grpc
import serializer_pb2 as grpc_methods
import serializer_pb2_grpc as grpc_types
import pickle


class Pessoa:
    def __init__(self, nome, idade, peso) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso


class CalculatorServicer(grpc_types.SerializerServicer):
    def Add(self, request, context):
        print("add")
        return grpc_methods.ResultResponse(result=request.a + request.b)

    def TesteSerial(self, request, context):
        print("teste serial")
        print(request.data)
        obj2 = pickle.loads(request.data2)
        print(obj2)
        print(obj2.nome)
        return grpc_methods.SerialData(data="aaaaaaa")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_types.add_SerializerServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Calculator server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
