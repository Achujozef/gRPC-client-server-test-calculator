import grpc
import calculator_pb2
import calculator_pb2_grpc

channel =grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

number = float(input('Enter a number:   '))
request = calculator_pb2.SquareRootRequest(value=number)
response =stub.SquareRoot(request)

print(response.value)