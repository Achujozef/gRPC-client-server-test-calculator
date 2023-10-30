# import math
# import grpc
# import calculator_pb2
# import calculator_pb2_grpc

# class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
#     def SquareRoot (sefl, request, context):
#         response = calculator_pb2.SquareRootResponse()
#         response.value = math.sqrt(request.value)
#         return response 

# server = grpc.server(futures.ThreadPoolExicutor(max_workers=10))
# calculator_pb2_grpc.add_CalculatorServicer_to_server(
#     CalculatorServicer(), server
#     )
# server.add_insecure_port('[::]:50051')
# server.start()
# server.wait_for_termination()

import math
import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.SquareRootResponse()
        response.value = math.sqrt(request.value)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
