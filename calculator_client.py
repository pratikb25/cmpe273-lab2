# Import required modules
from __future__ import print_function
import sys

# Import gRPC modules
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:15432') as channel:
		stub = calculator_pb2_grpc.AdderStub(channel)
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
		response = stub.AddNumbers(calculator_pb2.Numbers(number1=num1, number2=num2))
	print("Sum of two numbers is: " + str(response.addition))

if __name__ == '__main__':
	run()
