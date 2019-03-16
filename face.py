import cv2
myimage=cv2.imread(r"C:\Users\Navneet\Desktop\Photo\abcd.jpg") 
myimage1=cv2.imread(r"C:\Users\Navneet\Desktop\Photo\abcd.jpg",cv2.IMREAD_GRAYSCALE) 
facedetector=cv2.CascadeClassifier(r"C:\Users\Navneet\Anaconda3\Library\etc\haarcascades\haarcascade_fron+****589-talface_default.xml")
face=facedetector.detectMultiScale(myimage1,1.3,5)
for x,y,w,z in face: 
    cv2.rectangle(myimage,(x,y),(x+w,y+z),(0,0,255),3)
cv2.imshow("facedetected",myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
