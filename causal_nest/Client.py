import grpc

# import calculator_pb2
# import calculator_pb2_grpc
import pickle
import serializer_pb2 as grpc_methods
import serializer_pb2_grpc as grpc_types

channel = grpc.insecure_channel("localhost:50051")
stub = grpc_types.SerializerStub(channel)


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
    response = stub.TesteSerial(grpc_methods.SerialData(data=str(obj), data2=obj))
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
                response = stub.Add(grpc_methods.OperationRequest(a=a, b=b))
            elif op == "-":
                response = stub.Subtract(grpc_methods.OperationRequest(a=a, b=b))
            elif op == "*":
                response = stub.Multiply(grpc_methods.OperationRequest(a=a, b=b))
            elif op == "/":
                response = stub.Divide(grpc_methods.OperationRequest(a=a, b=b))
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
