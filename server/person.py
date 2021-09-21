import cv2
import time
import mail

def person ():

    image=cv2.imread('body.jpg') #m.file('body.jpg')


    body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')



    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bodys = body_cascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in bodys:
        print ("trovato")
        mail.sendMail()
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return(True)
        
    return (False)

#    cv2.imshow("Result", image)

#    cv2.waitKey(0)



