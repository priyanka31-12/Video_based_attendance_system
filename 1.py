import cv2

fourcc=cv2.VideoWriter_fourcc(*'XVID') #it defines the format of the video captured

# Below VideoWriter object will create a frame defined output
# which is stored in 'output.avi' file.
out=cv2.VideoWriter('output1.avi',fourcc,20,(640,480))
cap=cv2.VideoCapture(0)
while(True):

        ret,frame=cap.read()

        out.write(frame)


        cv2.imshow('img',frame)
       

        if cv2.waitKey(30)==ord('q'): #video is closed when 'q' is pressed
               break
 
            

cap.release()
out.release()


cv2.destroyAllWindows()
