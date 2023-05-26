import cv2

img=cv2.imread("butterfly.jpg")

cv2.imshow("Mostrar Imagen", img)

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Espythoncala de Grises", gray_img)

#print(gray_img)
cv2.waitKey(0)