protoc -I ./protos --python_out=./protos --grpc_out=./protos --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./protos/imagerecognition.proto

sleep 1

rm -rf ./server/imagerecognition_pb*.py 
cp ./protos/*.py ./server
rm -rf ./client/imagerecognition_pb*.py 
cp ./protos/*.py ./client
