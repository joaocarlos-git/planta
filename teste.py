import numpy as np
import cv2
imagem = np.ones((200,100,3))*255
cv2.ellipse(imagem,(200,100)(100,50),0,0,270,(0,0,0),3,cv2.LINE_8)
cv2.imshow("imagem",imagem)
cv2.waitKey(0)
