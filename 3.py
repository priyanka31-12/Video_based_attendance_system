import cv2
import numpy as np

img_path = "E:/Practice/py_beg/ML assignment/task1_priyanka/img0.jpg"

img = cv2.imread(img_path)
img = cv2.resize(img, (360,520))
print(img.shape)

b, g, r = cv2.split(img)

#to show any one color the attribute for the other parts must be zero 
zero_ch = np.zeros(img.shape[0:2], dtype="uint8")

blue_img = cv2.merge([b, zero_ch, zero_ch])
cv2.imshow("Blue Image", blue_img)



green_img = cv2.merge([zero_ch, g, zero_ch])
cv2.imshow("Green Image", green_img)


red_img = cv2.merge([zero_ch, zero_ch, r])
cv2.imshow("red Image", red_img)



pathB='E:/Practice/py_beg/ML assignment/task1_img_RGB/task1_img0/image_B'+'.jpg'
cv2.imwrite(pathB, blue_img)

pathG='E:/Practice/py_beg/ML assignment/task1_img_RGB/task1_img0/image_G'+'.jpg'
cv2.imwrite(pathG, green_img)

pathR='E:/Practice/py_beg/ML assignment/task1_img_RGB/task1_img0/image_R'+'.jpg'
cv2.imwrite(pathR, red_img)

 

cv2.waitKey(0)
cv2.destroyAllWindows()       
