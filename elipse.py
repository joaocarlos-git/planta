import numpy as np
import cv2
imagem = np.ones((300,400,3), np.uint8)*255
cv2.ellipse(imagem,(200,100),(100,50),0,0,360,(0,0,0),-1,cv2.LINE_8)
cv2.imshow("imagem",imagem)
cv2.waitKey(0)
