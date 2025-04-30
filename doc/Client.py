import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    while True:
        try:
            a = float(input("Enter first number: "))
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

