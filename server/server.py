# -*- coding:utf-8 -*-
import imagerecognition_pb2
import imagerecognition_pb2_grpc
import time
import os

from opencvfun import get_IDnum

_ONE_DAY_IN_SECONDS = 60*60*24

class ImageRecognition(imagerecognition_pb2.BetaImageRecognitionServicer):
	def PositiveID(self, request_iterator, context):
		count = 0
		with open("./image/img_file", "wb") as f:
			for line in request_iterator:
				num = f.write(line.img)
				count += num
				filename = line.filename
				filetype = line.filetype

		tmp_file = "./image/positiveid" + filetype
		os.rename("./image/img_file", tmp_file)
		num = get_IDnum(tmp_file)
		return imagerecognition_pb2.PositiveIDInfo(name="李梦元",
			sex="男", nation="汉族", age="19900218", addr="河南省郸城县南丰镇双庙村001号",
			IDnumber=num)

	def ReverseID(self, request_iterator, context):
		count = 0
		with open("./image/img_file", "wb") as f:
			for line in request_iterator:
				num = f.write(line.img)
				count += num
				filename = line.filename
				filetype = line.filetype

		tmp_file = "./image/reverseid" + filetype
		os.rename("./image/img_file", tmp_file)
		return imagerecognition_pb2.ReverseIDInfo(organization="郸城县公安局",
			effectivedate="19902.15-1621.5")


server = imagerecognition_pb2.beta_create_ImageRecognition_server(ImageRecognition())
server.add_insecure_port('[::]:50051')
server.start()

try:
	while True:
		time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
	server.stop()