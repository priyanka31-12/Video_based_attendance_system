import cv2

cap=cv2.VideoCapture("C:/Users/Ayush kumar/Desktop/vid.mp4")

i=0
while(cap.isOpened()):
    flag,frame=cap.read()
    if flag==False:
        break

    path='E:/Practice/py_beg/ML assignment/task1_priyanka/img' +str(i)+'.jpg'
    cv2.imwrite(path,frame)
    i+=1


cap.release()
cv2.destroyAllWindows()    

