import numpy as np
import cv2
# Cria uma imagem com a cor preta.
imagem = np.zeros((300,400,3), np.uint8)
# Desenha uma linha azul, diagonal com espessura de 5 pixeis.
# Ponto inicial: (0,0)
# Ponto final: (400,300)
# Cor: (255,0,0) -> Azul
cv2.line(imagem,(0,0),(255,255),(255,0,0),5)
cv2.imshow("Imagem",imagem)
cv2.waitKey(0)
