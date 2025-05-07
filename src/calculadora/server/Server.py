from concurrent import futures
import grpc
import teste_pb2_grpc
import teste_pb2


class CalcService(teste_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        print("add feito")
        return teste_pb2.CalcResponse(result=request.a + request.b)

    def Subtract(self, request, context):
        print("add feito")
        return teste_pb2.CalcResponse(result=request.a - request.b)

    def Multiply(self, request, context):
        print("add feito")
        return teste_pb2.CalcResponse(result=request.a * request.b)

    def Divide(self, request, context):
        print("add feito")
        if request.b == 0:
            return teste_pb2.CalcResponse(result=0)
        return teste_pb2.CalcResponse(result=request.a / request.b)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    teste_pb2_grpc.add_CalculatorServicer_to_server(CalcService(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    print("Calculator server running on port 50051")
    print("Calculator server running on port 50051")
    print("Calculator server running on port 50051")
    print("Calculator server running on port 50051")
    print("Calculator server running on port 50051")
    server.wait_for_termination()
    print("add feito")


if __name__ == "__main__":
    serve()
