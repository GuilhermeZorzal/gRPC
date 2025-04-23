import teste_pb2_grpc
import teste_pb2
import grpc


def client():
    channel = grpc.insecure_channel("server:8000")
    stub = teste_pb2_grpc.CalculatorStub(channel=channel)

    a = 3
    b = 2
    response = stub.Add(teste_pb2.CalcRequest(a=a, b=b))
    print(response)
    # while True:
    #     a = int(input("Digite o primeiro valor"))
    #     b = int(input("Digite o segundo valor"))
    #     c = str(input("Digite o operador"))
    #
    #     response = None
    #     match c:
    #         case "+":
    #             response = stub.Add(teste_pb2.CalcRequest(a=a, b=b))
    #         case "-":
    #             response = stub.Subtract(teste_pb2.CalcRequest(a=a, b=b))
    #         case "*":
    #             response = stub.Multiply(teste_pb2.CalcRequest(a=a, b=b))
    #         case "/":
    #             response = stub.Divide(teste_pb2.CalcRequest(a=a, b=b))
    #
    #     print("A resposta eh: ", response.result)


if __name__ == "__main__":
    client()
