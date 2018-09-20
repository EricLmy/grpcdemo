# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import imagerecognition_pb2 as imagerecognition__pb2


class ImageRecognitionStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PositiveID = channel.stream_unary(
        '/recognition.ImageRecognition/PositiveID',
        request_serializer=imagerecognition__pb2.ImgRequest.SerializeToString,
        response_deserializer=imagerecognition__pb2.PositiveIDInfo.FromString,
        )
    self.ReverseID = channel.stream_unary(
        '/recognition.ImageRecognition/ReverseID',
        request_serializer=imagerecognition__pb2.ImgRequest.SerializeToString,
        response_deserializer=imagerecognition__pb2.ReverseIDInfo.FromString,
        )


class ImageRecognitionServicer(object):

  def PositiveID(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReverseID(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImageRecognitionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PositiveID': grpc.stream_unary_rpc_method_handler(
          servicer.PositiveID,
          request_deserializer=imagerecognition__pb2.ImgRequest.FromString,
          response_serializer=imagerecognition__pb2.PositiveIDInfo.SerializeToString,
      ),
      'ReverseID': grpc.stream_unary_rpc_method_handler(
          servicer.ReverseID,
          request_deserializer=imagerecognition__pb2.ImgRequest.FromString,
          response_serializer=imagerecognition__pb2.ReverseIDInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'recognition.ImageRecognition', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
