import cv2
import numpy as np 
# from PIL import Image
import pytesseract

def process_img(img):
	kernel = np.ones((9,9), np.uint8)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 
	img = cv2.GaussianBlur(img, (7,7), 0)
	retval, img = cv2.threshold(img, 165, 255, cv2.THRESH_BINARY_INV)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	# retval, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
	# cv2.medianBlur(img, 5)
	# img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
	# img = cv2.dilate(img, kernel, iterations=1)
	# img = cv2.erode(img, kernel, iterations=2)

	# kernel = 1/16 * np.array([[1,2,1],[2,4,2],[1,2,1]])
	# img = cv2.filter2D(img, -1, kernel)
	# retval, img = cv2.threshold(img, 165, 255, cv2.THRESH_BINARY)
	return img

def adjust_luminance(img, s, b):
	w = img.shape[1]
	h = img.shape[0]
	type(img)
	for xi in range(0, w):
		for xj in range(0, h):
			if int(img[xj, xi, 0] * s + b) > 255:
				img[xj, xi, 0] = 255 
			elif int(img[xj, xi, 0] * s + b) < 0:
				img[xj, xi, 0] = 0 
			else:
				img[xj, xi, 0] = int(img[xj, xi, 0] * s + b)

			if int(img[xj, xi, 1] * s + b) > 255:
				img[xj, xi, 1] = 255 
			elif int(img[xj, xi, 1] * s + b) < 0:
				img[xj, xi, 1] = 0 
			else:
				img[xj, xi, 1] = int(img[xj, xi, 1] * s + b)

			if int(img[xj, xi, 2] * s + b) > 255:
				img[xj, xi, 2] = 255 
			elif int(img[xj, xi, 2] * s + b) < 0:
				img[xj, xi, 2] = 0 
			else:
				img[xj, xi, 2] = int(img[xj, xi, 2] * s + b)
	return img

def get_rect_box(contours):
	ws = []
	valid_contours = []
	for contour in contours:
		x,y,w,h = cv2.boundingRect(contour)
		if w < 7:
			continue
		valid_contours.append(contour)

	result = []
	for contour in valid_contours:
		x,y,w,h = cv2.boundingRect(contour)
		box = np.int0([[x,y],[x+w,y],[x+w,y+h],[x,y+h]])
		result.append(box)

	result = sorted(result, key=lambda x: x[0][0])
	return result


''' suofang img '''
def cropxy_img(img, new_x, new_y):
	res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
	return res

def cropwh_img(img, new_w, new_h):
	res = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
	return res

''' xuanzhuan img '''
def rotate_img(img, rotate_angle):
	rows, cols = img.shape[0], img.shape[1]
	M = cv2.getRotationMatrix2D((cols/2, rows/2), rotate_angle, 1)
	dst = cv2.warpAffine(img, M, (rows, cols))
	return dst

def get_box_xy_and_wh(box):
	x, y = box[0][0], box[0][1]
	w = box[2][0] - box[0][0]
	h = box[2][1] - box[0][1]
	return x, y, w, h

def get_rectimg_from_img(img, box):
	x, y, w, h = get_box_xy_and_wh(box)
	return img[y: y+h, x:x+w]


# img = cv2.imread("./image/reverseid.jpg")
img = cv2.imread("./image/positiveid.jpg")
# img = cv2.imread("./image/mez.jpg")
# img = rotate_img(img, 90)
# img = cropwh_img(img, 475, 297)
# img = cv2.resize(img, (475, 297), interpolation=cv2.INTER_CUBIC)
# # img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)
print(img.shape)
# img = adjust_luminance(img, 1.2, 10)
# img = adjust_luminance(img, 1.2, 0)
# img = adjust_luminance(img, 0.8, 0)
img1 = process_img(img)
cv2.imshow("img1", img1)
img2, contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = get_rect_box(contours)
# 
for box in boxes:
	cv2.drawContours(img, [box], 0, (0,0,255), 2)
	x, y, w, h = get_box_xy_and_wh(box)
	if w > h*6:
		resultimg = get_rectimg_from_img(img, box)
		cv2.imwrite("./image/num.jpg", resultimg)
		text = pytesseract.image_to_string(resultimg, lang='eng')
		# text = pytesseract.image_to_string(Image.open("./image/num.jpg"), lang='eng')
		print(text)
	# print(box[0])
	# print(box[1])

cv2.imshow("img", img)
cv2.waitKey(0)
# cv2.destoryAllWindows()
