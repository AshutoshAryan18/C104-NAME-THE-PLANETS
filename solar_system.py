import cv2

img=cv2.imread(r"C:\Users\ASHUTOSH ARYAN\OneDrive\Desktop\coding\module 3\project\C ---104[NAME THE PLANETS]\PRO-104-Project-Image-main\solar-system.jpg")


text_1= "SUN"
text_2= "MERCURY"
text_3= "VENUS"
text_4= "EARTH"
text_5= "MARS"
text_6= "JUPITER"
text_7= "SATURN"
text_8= "URANUS"
text_9= "NEPTUNE"

cv2.putText(img,text_1,(20,220),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(200,29,6))
cv2.putText(img,text_2,(100,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(200,29,6))
cv2.putText(img,text_3,(180,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,6))
cv2.putText(img,text_4,(280,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,6))
cv2.putText(img,text_5,(380,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,6))
cv2.putText(img,text_6,(500,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,6))
cv2.putText(img,text_7,(800,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,6))
cv2.putText(img,text_8,(950,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,64))
cv2.putText(img,text_9,(1115,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(200,29,64))



cv2.imshow("solar_system",img)
cv2.imwrite("name_of_solar_system.jpg",img)
cv2.waitKey(0) 