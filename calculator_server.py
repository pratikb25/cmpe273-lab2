# Import gRPC modules
import grpc;
import calculator_pb2;
import calculator_pb2_grpc;

# Import required modules
from concurrent import futures
import time

class Server(calculator_pb2_grpc.AdderServicer):
	def AddNumbers(self, request, context):
		sum = request.number1 + request.number2;
		return calculator_pb2.Addition(addition=sum);

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10));
calculator_pb2_grpc.add_AdderServicer_to_server(Server(), server);
server.add_insecure_port('[::]:15432');
print("Started server on port '[::]:15432'...");
server.start();
try:
	while True:
		print("Waiting for request...");
		time.sleep(60 * 60);
except KeyboardInterrupt:
	server.stop(0);
