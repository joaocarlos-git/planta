import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import ImageFont, ImageDraw, Image

def carregar_imagem(imagem):
	imagem = cv2.imread(imagem)
	cv2.imshow("Cachorro", imagem)
	cv2.waitKey(0)
	cv2.destryAllWindows()			
	return imagem


def criar_linha(imagem, pi, pf, cor, espessura):
	cv2.line(imagem, pi,pf,cor,espessura)
	
	return imagem
	
def cria_circulo(imagem, centro, r,  cor, espessura):
	imagem = np.ones((300,400,3), np.uint8)* 255
	cv2.circle(imagem, centro, r, cor, espessura)	
	cv2.imshow("Imagem",imagem)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	return imagem
	
	
def criar_retangulo(imagem, supes, infdir, cor, espessura): 
	cv2.rectangle(imagem, supes, infdir, cor, espessura)
	
	return imagem
	
def criar_elipse(imagem, cel, eixel, rel, ain, afi, cor, espessura, tlinha):	
	cv2.ellipse(imagem, cel, eixel, rel, ain, afi, cor, espessura, tlinha)	
		
	return imagem
	
def criar_escrita(imagem, texto, cantoinf, fonte, tfont, cor, larglinha, tlinha):
	fonte = cv2.FONT_HERSHEY_PLAIN
	cv2.putText(imagem, texto, cantoinf, fonte, tfont, cor, larglinha, tlinha)
	#cv2.imshow("imagem",imagem)
	#cv2.waitKey(0)
	#cv2.destryAllWindows()
	
	return imagem	
	
def cria_poligono(imagem, pts, cor):
	pts = np.array(imagem) # Cria lista de pontos.
	pts = pts.reshape((-1,1,2)) # ajusta o formato do vetor de pontos para coluna unica.
	fechar =  True
	pts = np.array([[50,55],[130,140],[150,120],[100,50]], np.int32)
	pts = pts.reshape((-1,1,2)) # ajusta o formato do vetor de pontos para coluna unica.
	cv2.polylines(imagem,[pts],True , (0,255,0))
	cv2.imshow("Imagem",imagem)
	cv2.waitKey(0)
	cv2.destryAllWindows()
		
	return imagem
	
def criar_hist_img(imagem1, imagem2):
	imagem = mpimg.imread(imagem1, imagem2)
		
	return imagem
	
def criar_hist_dados(imagem, idades, bins):
	plt.hist(idades, bins)
	plt.show()
	cv2.destryAllWindows()
	
	return imagem
	
def criar_hist_pontos(imagem, x, y):
	plt.scatter(x,y,c='r')
	plt.xlabel('Eixo X')
	plt.ylabel('Eixo Y')
	plt.show()
	
	return imagem
	
def criar_hist_linha(imagem, x):
	plt.plot(x,x**2,c='r')
	plt.plot(x,x,c='g')
	plt.xlabel('Eixo X')
	plt.ylabel('Eixo Y')
	plt.show()
			
	return imagem
	
def criar_tcinzas(imagem):
	imagem = cv2.imread(imagem)
		
	return imagem
	
def criarbgr_rgb(imagem):
	imagem = cv2.imread(imagem)
	im_aux = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
	plt.imshow(im_aux)
	plt.show()
	
	return imagem
	
def recortar_imagem(imagem):
	imagem =cv2.imread(imagem)
	imCrop = imagem[40:300,40:400]
	cv2.imshow("ROI", imCrop)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	
	return imagem
	
def pedir_recortar(imagem):
	imagem = cv2.imread(imagem)
	pedido = int(input("Digite o retangulo a ser recortado\n 1 para retangulo maior\n 2 retangulo menor\n escolha: "))
	if pedido == 1:
		pedido = imCrop = imagem[40:300,40:400]
	elif pedido == 2:
		pedido = imCrop = imagem[20:150,20:200]
	cv2.imshow("ROI", pedido)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	
	return imagem
	
def redimencionar_imagem(imagem):
	imagem = cv2.imread(imagem)
	#cv2.imshow("Original", imagem)
	escala = 1.5
	nova=cv2.resize(imagem, None, fx=escala,fy=escala, interpolation = cv2.INTER_AREA)
	cv2.imshow("Imagem em Escala 1,5X", nova)
	cv2.waitKey(0)	
	cv2.destryAllWindows()
	
	return imagem
	
def rotacionar_imagem(imagem):
	imagem = cv2.imread(imagem)
	(altura, largura) = imagem.shape[:2]
	centro = (largura / 2, altura / 2)   # formato (x,y)
	mat = cv2.getRotationMatrix2D(centro, 90, 1.0)
	imagem_rotacionada = cv2.warpAffine(imagem, mat, (largura, altura))
	cv2.imshow("Imagem Rotacionada em 90 Graus", imagem_rotacionada)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	
	return imagem
	
def deslocar_imagem(imagem):
	altura,largura=imagem.shape[:2]		
	deslocamento = np.float32([[1,0,25], [0,1,50]])
	deslocado = cv2.warpAffine(imagem, deslocamento,(altura,largura))
	cv2.imshow("Deslocado",deslocado)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	
	return imagem
	
def detectar_faces(imagem):
	arq_classificador = "haarcascade_frontalface_default.xml"
	classificador = cv2.CascadeClassifier(arq_classificador)
	imagem = cv2.imread("selfie-1.png")
	cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	faces = classificador.detectMultiScale(
    	cinza,
    	scaleFactor=1.1,
    	minNeighbors=5,
    	minSize=(30, 30),
    	flags=cv2.CASCADE_SCALE_IMAGE
	)
	print("Total de faces detectadas: " + str(len(faces)))

	# Desenha um retangulo para cada face encontrada
	for (x, y, l, a) in faces:
    		cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 3)

	# Mostra a imagem (colorida) com os retangulos desenhados nas faces
	cv2.imshow("Faces detectadas", imagem)
	# Aguarda tecla para fechar a janela
	cv2.waitKey()
	cv2.destroyAllWindows()

	return imagem
	
def salvar_imagem(imagem, arquivo):
	#imagem = cv2.imread("bolinhas.jpeg")
	cv2.imwrite(arquivo, imagem)
	
	
def imagem_casa(largura, altura):
	imagem = np.ones((altura, largura, 3)) * 255
	return imagem
	
def exibir_imagem(imagem, janela, espera = 0):
	cv2.imshow(janela, imagem)
	cv2.waitKey(espera)



