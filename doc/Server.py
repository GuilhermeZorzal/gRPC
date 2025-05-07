from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return calculator_pb2.ResultResponse(result=request.a + request.b)

    def Subtract(self, request, context):
        return calculator_pb2.ResultResponse(result=request.a - request.b)

    def Multiply(self, request, context):
        return calculator_pb2.ResultResponse(result=request.a * request.b)

    def Divide(self, request, context):
        if request.b == 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot divide by zero")
        return calculator_pb2.ResultResponse(result=request.a / request.b)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Calculator server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
