import cv2

#create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier("E:\Haar Cascade paths\haarcascade_frontalface_alt2.xml")

#reading the image as it is 
img = cv2.imread("E:/Practice/py_beg/ML assignment/task1_priyanka/img4.jpg")


#search the coordinates of the face
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

#scalefactor specifies how much the image size is reduced at each image scale.
# minNeighbors specifies how many neighbors each candidate rectangle should have to retain it.


print(type(faces))
print(faces)

#for rectangular shape arround the face
for x,y,w,h in faces:  #(img, pt1, pt2, color,thickness)
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,225,0),2)

resized = cv2.resize(img, (int(img.shape[1]*(1.5)), int(img.shape[1]*1)))   
cropped = img[x:x+w, y:y+h]

cv2.imshow("Gray", img)


path='E:/Practice/py_beg/ML assignment/task1_image_FACE/task1_img4_FACE'+'.jpg'

# to store the cropped face only 
cv2.imwrite(path, cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
