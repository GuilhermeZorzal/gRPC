from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc
import pickle


class Pessoa:
    def __init__(self, nome, idade, peso) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        print("add")
        return calculator_pb2.ResultResponse(result=request.a + request.b)

    def Subtract(self, request, context):
        return calculator_pb2.ResultResponse(result=request.a - request.b)

    def Multiply(self, request, context):
        return calculator_pb2.ResultResponse(result=request.a * request.b)

    def Divide(self, request, context):
        if request.b == 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot divide by zero")
        return calculator_pb2.ResultResponse(result=request.a / request.b)

    def TesteSerial(self, request, context):
        print("teste serial")
        print(request.data)
        obj2 = pickle.loads(request.data2)
        print(obj2)
        print(obj2.nome)
        return calculator_pb2.SerialData(data="aaaaaaa")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Calculator server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
