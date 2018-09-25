# -*- coding:utf-8 -*-
from __future__ import print_function

import grpc

import imagerecognition_pb2
import imagerecognition_pb2_grpc
import os

def get_img_data(filepath):
	(filename, filetype) = os.path.splitext(os.path.basename(os.path.realpath(filepath)))
	with open(filepath, "rb") as f:
		for line in f.readlines():
			yield imagerecognition_pb2.ImgRequest(filename=filename,filetype=filetype,img=line) 

def run():
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = imagerecognition_pb2_grpc.ImageRecognitionStub(channel)

		ret = stub.PositiveID(get_img_data("../image/xiaob.jpg"))
		print(ret.IDnumber)
		# print(ret.addr)
		# print('--------------------------------')
		# ret = stub.ReverseID(get_img_data("../image/bei1.jpg"))
		# print(ret)


if __name__ == '__main__':
	run()