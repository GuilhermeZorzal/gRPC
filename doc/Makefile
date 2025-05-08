all:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./calculator.proto
server: 
	python ./Server.py
client: 
	python ./Client.py
