import grpc
import calculator_pb2
import calculator_pb2_grpc
import pickle

channel = grpc.insecure_channel("localhost:50051")
stub = calculator_pb2_grpc.CalculatorStub(channel)


class Pessoa:
    def __init__(self, nome, idade, peso) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso


def testeSerializacao():
    p = Pessoa("ze", 34, 90)
    print(p)
    obj = pickle.dumps(p)
    print(obj)
    response = stub.TesteSerial(calculator_pb2.SerialData(data=str(obj), data2=obj))
    print(response)
    print("teste")


def run():
    while True:
        try:
            a = float(input("Enter first number: "))
            if a == 0:
                testeSerializacao()
                continue
            b = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ").strip()

            if op == "+":
                response = stub.Add(calculator_pb2.OperationRequest(a=a, b=b))
            elif op == "-":
                response = stub.Subtract(calculator_pb2.OperationRequest(a=a, b=b))
            elif op == "*":
                response = stub.Multiply(calculator_pb2.OperationRequest(a=a, b=b))
            elif op == "/":
                response = stub.Divide(calculator_pb2.OperationRequest(a=a, b=b))
            else:
                print("Invalid operation!")
                continue

            if response.error:
                print(f"Error: {response.error}")
            else:
                print(f"Result: {response.result}")

        except ValueError:
            print("Please enter valid numbers!")
        except grpc.RpcError as e:
            print(f"RPC Error: {e.code()}: {e.details()}")
        except KeyboardInterrupt:
            print("\nExiting...")
            print("hell")
            break


if __name__ == "__main__":
    run()
