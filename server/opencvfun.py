import cv2
import numpy as np 

def process_img(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	retval, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)
	# kernel = 1/16 * np.array([[1,2,1],[2,4,2],[1,2,1]])
	# img = cv2.filter2D(img, -1, kernel)
	img = cv2.GaussianBlur(img, (13,13), 0)
	# retval, img = cv2.threshold(img, 165, 255, cv2.THRESH_BINARY)
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
def crop_img(img, new_x, new_y):
	res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
	return img

''' xuanzhuan img '''
def rotate_img(img, rotate_angle, outputdir):
	pass 


# img = cv2.imread("./image/reverseid.jpg")
img = cv2.imread("./image/positiveid.jpg")
# img = cv2.imread("./image/mez1.jpg")
# ret = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
print(img.shape)
img1 = process_img(img)
cv2.imshow("img1", img1)
img2, contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = get_rect_box(contours)

for box in boxes:
	cv2.drawContours(img, [box], 0, (0,0,255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
# cv2.destoryAllWindows()

