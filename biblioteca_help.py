import numpy as np
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

import interface as trab

#Trabalho de Computação Gráfica
#Anderson Lopes de Siqueira
#João Carlos Silva Ribeiro
#Sidney Barros de Souza
tarefa = int(input("\n1 - Cachorro \n2 - Linha \n3 - Círculo \n4 - Retangulo \n5 - Elipse \n6 - Escrita \n7 - Poligono \n8 - Histograma \n9 - Histograma_dados \n10 - Histograma_pontos \n11 - Histograma de linhas\n12 - Tons de cinza\n13 - BGR para RGB\n14 - Recortar Imagem\n15 - Pedir para recortar\n16 - Redimencionar imagem\n17 - Rotacionar Imagem\n18 - Deslocamento de Imagem\n19 - Detectar faces\n20 - Desenhar planta\n21 - Salvar Imagem\n22 - Sair\n Escolha a tarefa: "))

continuar = True
while continuar:
	if tarefa == 1: 
		imagem = trab.carregar_imagem('cachorro.jpg')
		
		pass 
	
	elif tarefa == 2:
		imagem = np.zeros((300,400,3), np.uint8) * 255
		imagem = trab.criar_linha(imagem, (100,100), (100,200), (255,255,255), 1)
		trab.exibir_imagem(imagem, "Linha")
		
		pass
		
	elif tarefa ==3:
		imagem = np.ones((300, 400, 3)) * 255
		imagem = trab.cria_circulo(imagem,(200,150), 100, (0,165,255), -1)
		
		pass
		
	elif tarefa == 4:
		imagem = np.ones((300, 400, 3)) * 255	
		imagem = trab.criar_retangulo(imagem, (50,50), (353,268), (0,255,255), -1)
		trab.exibir_imagem(imagem, "Retangulo")
				
		pass
		
	elif tarefa == 5:
		imagem = np.ones((300, 400, 3)) * 255
		imagem = trab.criar_elipse(imagem,(200,100),(100,50),30,0,360,		(0,0,0),4,cv2.LINE_8)
		trab.exibir_imagem(imagem, "Elipse")
		
		pass
		
	elif tarefa == 6:
		imagem1 = np.ones((300, 400, 3)) * 255
		imagem1 = trab.criar_escrita(imagem1,'Anderson, Joao, Sidney',(16,20), cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0),1,cv2.LINE_AA)
		trab.exibir_imagem(imagem1, "Escrita")
				
		pass
		
	elif tarefa == 7:
		imagem = np.ones((300, 400, 3)) * 255
		imagem = trab.cria_poligono(imagem, (np.array([[50,55],[130,140],[150,120],[100,50]], np.int32)), (0,0,255))
				
		pass
		
	elif tarefa == 8:
		imagem1 = mpimg.imread("gato_cinza.jpg")
		imagem2 = mpimg.imread("gato_cinza2.jpg")
		imagem = trab.criar_hist_img(imagem1 = "gato_cinza.jpg", imagem2 = "gato_cinza2.jpg")
		plt.subplot(1,2,1)
		plt.hist(imagem1.flatten(), bins=256)
		plt.subplot(1,2,2)
		plt.hist(imagem2.flatten(), bins=256)
		plt.xlabel('idade')
		plt.ylabel('Frequência')
		plt.tight_layout()
		plt.show()
			
		
		pass 
		
	elif tarefa == 9:
		idades = [17,28,62,19,28,30,18,22,23,29,
		          31,18,25,23,30,22,21,56,39,18,
		          19,41,22,52,22,41,23,20,60,19]
		bins = [18, 26, 36, 46, 56, 65]
		imagem = np.ones((300, 400, 3)) * 255
		imagem = trab.criar_hist_dados(imagem ,idades = [17,28,62,19,28,30,18,22,23,29,
		          31,18,25,23,30,22,21,56,39,18,19,41,22,52,22,41,23,20,60,19], bins = [18, 26, 36, 46, 56, 65])
				
		pass
		
	elif tarefa == 10:
		x = [1,4,5,7,10,15,20]
		y = [0,3,5,7,12,20,25]
		imagem = np.ones((300, 400, 3)) * 255
		imagem = trab.criar_hist_pontos(imagem, x = [1,4,5,7,10,15,20], y = [0,3,5,7,12,20,25])
		plt.scatter(x = [1,4,5,7,10,15,20], y = [0,3,5,7,12,20,25] ,c = 'r')
		
		pass
		
	elif tarefa == 11:
		imagem = np.ones((300, 400, 3)) * 255
		x = np.linspace(1,5,5)
		imagem = trab.criar_hist_linha(imagem, x)
				
		pass

	elif tarefa == 12:
		imagem = cv2.imread("gato.jpg")
		im_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
		imagem = trab.criar_tcinzas("gato.jpg")
		cv2.imwrite("gato_cinza.jpg", im_cinza)
		cv2.imshow("Imagem", im_cinza)
		cv2.waitKey(0)
		cv2.destryAllWindows()
		
		pass
		
	elif tarefa == 13:
		imagem = cv2.imread("apollo8.jpg")
		imagem = trab.criarbgr_rgb("apollo8.jpg")
		
		pass
		
	elif tarefa == 14:
		imagem = cv2.imread("spaceX.jpg")
		imagem = trab.recortar_imagem("spaceX.jpg")
				
		pass
		
	elif tarefa == 15:
		imagem = trab.pedir_recortar("cachorro.jpg")
		
		pass
		
	elif tarefa == 16:
		imagem = trab.redimencionar_imagem("spaceX.jpg")
				
		pass
		
	elif tarefa == 17:
		imagem = cv2.imread("apollo8.jpg")
		imagem = trab.rotacionar_imagem("apollo8.jpg")
			
		pass
		
	elif tarefa == 18:
		imagem = cv2.imread("cachorro.jpg")
		imagem = trab.deslocar_imagem(imagem)
				
		pass
		
	elif tarefa == 19:
		imagem = cv2.imread("selfie-1.png")
		imagem = trab.detectar_faces("selfie-1.png")		
		
		pass

	elif tarefa == 20:
		imagem = trab.imagem_casa(1000, 500)
		#trab.exibir_imagem(imagem, "Casa")
		trab.criar_retangulo(imagem, (100, 100), (900,400), (0, 0, 0), -1)#criando o retangulo principal
		trab.criar_retangulo(imagem, (102, 102), (898,398), (157,157,157), -
		1)#criando o retangulo interno
		trab.criar_retangulo(imagem, (113, 113), (312,388), (0,0,0), -1)#criando as paredes internas da cozinha
		trab.criar_retangulo(imagem, (115, 115), (310,386), (255, 255, 255), -1)#pintando de branco a cozinha
		trab.criar_retangulo(imagem, (318, 102), (411,388), (255,255,255), -1)#criando o retangulo do banheiro
		trab.criar_retangulo(imagem, (328, 113), (397,287), (0,0,0), -1)#criando area do banheiro
		trab.criar_retangulo(imagem, (330, 115), (395,285), (255,255,255), -1)#pintando o banheiro de branco		
		trab.criar_retangulo(imagem, (622, 113), (412,388), (0,0,0), -1)#criando o retangulo da sala	
		trab.criar_retangulo(imagem, (620, 115), (414,386), (255,255,255), -1)#pintando a sala de branco	
		trab.criar_retangulo(imagem, (638, 113), (888,388), (0,0,0), -1)#criando o retangulo do quarto	
		trab.criar_retangulo(imagem, (640, 115), (886,386), (255,255,255), -1)#pintando o retangulo do quarto
		trab.criar_retangulo(imagem, (312, 300), (412,388), (0,0,0), -1)#Criando o retangulo entre a cozinha e a sala
		trab.criar_retangulo(imagem, (310, 302), (414,386), (255,255,255), -1)#pintando o retangulo reparador entre cozinha e sala
		trab.criar_retangulo(imagem, (113, 113), (680,114), (0,0,0), -1)#Criando linha para fechar parte superior interna da planta
		trab.criar_retangulo(imagem, (388, 388), (886,387), (0,0,0), -1)#Criando linha para fechar parte inferior interna da planta
		trab.criar_retangulo(imagem, (622, 300), (637,380), (0,0,0), -1)#Criando o retangulo entre a sala e o quarto
		trab.criar_retangulo(imagem, (640, 302), (600,378), (255,255,255), -1)#Criando o retangulo entre a sala e o quarto
		trab.criar_retangulo(imagem, (623, 388), (637,387), (255,255,255), -1)#Criando linha branca para a parte inferior interna da planta
		trab.criar_retangulo(imagem, (113, 113), (680,114), (0,0,0), -1)#Criando linha banca para fechar parte superior interna da planta
		trab.criar_retangulo(imagem, (313, 113), (327,114), (255,255,255), -1)#Criando linha brancapara fechar parte superior interna da planta
		trab.criar_retangulo(imagem, (398, 113), (411,114), (255,255,255), -1)#Criando linha branca para fechar parte superior interna da planta
		trab.criar_retangulo(imagem, (623, 113), (637,114), (255,255,255), -1)#Criando linha branca para fechar parte superior interna da planta		
		trab.criar_retangulo(imagem, (343, 112), (382,100), (0,0,0), -1)#Criando janela do  banheiro
		trab.criar_retangulo(imagem, (345, 114), (380,100), (255,255,255), -1)#pintando o retangulo da janela do banheiro
		trab.criar_retangulo(imagem, (340, 301), (385,286), (0,0,0), -1)#Criando retangulo da porta do banheiro  banheiro
		trab.criar_retangulo(imagem, (342, 302), (383,284), (255,255,255), -1)#pintando o retangulo da porta do banheiro
		trab.criar_retangulo(imagem, (170, 400), (255,387), (0,0,0), -1)#Criando o retangulo da janela da cozinha
		trab.criar_retangulo(imagem, (172, 401), (253,385), (255,255,255), -1)#pintando o retangulo da janela da cozinha
		trab.criar_retangulo(imagem, (311, 400), (375,387), (0,0,0), -1)#Criando o retangulo da porta da cozinha
		trab.criar_retangulo(imagem, (313, 401), (373,385), (255,255,255), -1)#pintando o retangulo da porta da cozinha
		trab.criar_retangulo(imagem, (460, 400), (545,387), (0,0,0), -1)#Criando o retangulo da janela da sala
		trab.criar_retangulo(imagem, (462, 401), (543,385), (255,255,255), -1)#pintando o retangulo da janela da sala
		trab.criar_retangulo(imagem, (735, 400), (815,387), (0,0,0), -1)#Criando o retangulo da janela do quarto
		trab.criar_retangulo(imagem, (737, 401), (813,385), (255,255,255), -1)#pintando o retangulo da janela do quarto
		
		
		
		trab.criar_linha(imagem, (345, 104), (380,104), (255,0,0), 1)#Criando a linha da janela do banheiro
		trab.criar_linha(imagem, (345, 108), (380,108), (255,0,0), 1)#Criando a linha da janela do banheiro
		trab.criar_linha(imagem, (170, 390), (255,390), (255,0,0), 1)#Criando a linha da janela da cozinha
		trab.criar_linha(imagem, (170, 394), (255,394), (255,0,0), 1)#Criando a linha da janela da cozinha
		trab.criar_linha(imagem, (460, 390), (545,390), (255,0,0), 1)#Criando a linha da janela da sala
		trab.criar_linha(imagem, (460, 394), (545,394), (255,0,0), 1)#Criando a linha da janela da sala
		trab.criar_linha(imagem, (735, 390), (815,390), (255,0,0), 1)#Criando a linha da janela do quarto
		trab.criar_linha(imagem, (735, 394), (815,394), (255,0,0), 1)#Criando a linha da janela do quarto
		trab.criar_linha(imagem, (313,305), (313,386), (255,0,0), 1)#Criando a linha da porta da cozinha
		trab.criar_linha(imagem, (315,305), (315,386), (255,0,0), 1)#Criando a linha da porta da cozinha
		trab.criar_linha(imagem, (384,234), (384,284), (255,0,0), 1)#Criando a linha da porta da cozinha
		trab.criar_linha(imagem, (382,234), (382,284), (255,0,0), 1)#Criando a linha da porta da cozinha
		trab.criar_linha(imagem, (641, 379), (715,379), (255,0,0), 1)#Criando a linha da porta do banheiro
		trab.criar_linha(imagem, (641, 377), (715,377), (255,0,0), 1)#Criando a linha da porta do banheiro		
		trab.criar_elipse(imagem,(653,369),(80,50),50,220,305, (255,0,0),1,cv2.LINE_8)#Criando angulo da porta sala/quarto
		trab.criar_elipse(imagem,(306,365),(90,50),50,245,320, (255,0,0),1,cv2.LINE_8)#Criando angulo da porta cozinha/sala	
		trab.criar_elipse(imagem,(400,290),(60,60),50,125,205, (255,0,0),1,cv2.LINE_8)#Criando angulo da porta cozinha/sala
		
		
		#Criando linhas do lado esquerdo da planta
		trab.criar_linha(imagem, (80,90), (80,410), (0,0,255), 1)#Criando a primeira linha vertical do lado esquerdo
		trab.criar_linha(imagem, (40,100), (40,400), (0,0,255), 1)#Criando a segunda linha vertical do lado esquerdo
		trab.criar_linha(imagem, (70, 386), (95,386), (0,0,255), 1)#Criando a primeira linha horizontal inferior para medida lado de fora
		trab.criar_linha(imagem, (30, 400), (90,400), (0,0,255), 1)#Criando a segunda linha horizontal inferior para medida lado de fora
		trab.criar_linha(imagem, (70, 115), (95,115), (0,0,255), 1)#Criando a primeira linha horizontal superior para medida lado de fora
		trab.criar_linha(imagem, (30, 100), (90,100), (0,0,255), 1)#Criando a segunda linha horizontal inferior para medida lado de fora
		
		#Criando as linhas da parte de cima da planta
		trab.criar_linha(imagem, (100, 40), (900, 40), (0, 0, 255), 1) # linha horizontal de cima
		trab.criar_linha(imagem, (85, 60), (915, 60), (0,0,255), 1)#Linha horizontal de baixo
		trab.criar_linha(imagem, (100,30), (100,65), (0,0,255), 1)#1 Linha vertical de fora lado esquerdo	
		trab.criar_linha(imagem, (115,50), (115,95), (0,0,255), 1)#2 Linha vertical de dentro lado esquerdo	
		trab.criar_linha(imagem, (310,50), (310,95), (0,0,255), 1)#3 Linha vertical do lado esquerdo para o direito
		trab.criar_linha(imagem, (327,50), (327,95), (0,0,255), 1)#4Linha vertical do lado esquerdo para o direito
		trab.criar_linha(imagem, (395,50), (395,95), (0,0,255), 1)#5Linha vertical do lado esquerdo para direito		
		trab.criar_linha(imagem, (412,50), (412,95), (0,0,255), 1)#6Linha vertical do lado esquerdo para direito
		trab.criar_linha(imagem, (620,50), (620,95), (0,0,255), 1)#7Linha vertical do lado esquerdo para direito	
		trab.criar_linha(imagem, (638,50), (638,95), (0,0,255), 1)#8Linha vertical do lado esquerdo para direito	
		trab.criar_linha(imagem, (887,50), (887,95), (0,0,255), 1)#9Linha vertical do lado esquerdo para direito		
		trab.criar_linha(imagem, (900,30), (900,65), (0,0,255), 1)#9Linha vertical do lado esquerdo para direito	
		
		#Criando as linhas de medidas do lado direito
		trab.criar_linha(imagem, (940,90), (940,410), (0,0,255), 1)#Criando a primeira linha vertical
		trab.criar_linha(imagem, (920,100), (950,100), (0,0,255), 1)#Criando a primeira linha horizontal de cima para baixo lado direito
		trab.criar_linha(imagem, (905, 114), (950,114), (0,0,255), 1)#Criando a segunda linha horizontal de cima para baixo lado direito
		trab.criar_linha(imagem, (905, 386), (950,386), (0,0,255), 1)#Criando a terceira linha horizontal de cima para baixo lado direito
		trab.criar_linha(imagem, (920, 400), (950,400), (0,0,255), 1)#Criando a quarta linha horizontal de cima para baixo lado direito
		
		#Criando linha de baixo da planta
		trab.criar_linha(imagem, (85, 440), (915, 440), (0,0,255), 1)#Linha horizontal de baixo
		trab.criar_linha(imagem, (100,420), (100,445), (0,0,255), 1)#1 Linha vertical de fora lado esquerdo para a direito	
		trab.criar_linha(imagem, (115,410), (115,445), (0,0,255), 1)#2 Linha vertical de fora lado esquerdo para o direito
		trab.criar_linha(imagem, (310,410), (310,445), (0,0,255), 1)#3 Linha vertical do lado esquerdo para o direito
		trab.criar_linha(imagem, (412,410), (412,445), (0,0,255), 1)#4Linha vertical do lado esquerdo para direito	
		trab.criar_linha(imagem, (622,410), (622,445), (0,0,255), 1)#5Linha vertical do lado esquerdo para direito
		trab.criar_linha(imagem, (637,410), (637,445), (0,0,255), 1)#6Linha vertical do lado esquerdo para direito	
		trab.criar_linha(imagem, (888,410), (888,445), (0,0,255), 1)#7Linha vertical do lado esquerdo para direito
		trab.criar_linha(imagem, (900,420), (900,445), (0,0,255), 1)#8Linha vertical do lado esquerdo para direito
		
		
		#Escrevendo na planta lado de cima
		trab.criar_escrita(imagem, '800',(450,40),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#Valor 800
		trab.criar_escrita(imagem, '15',(100,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#1valor 15 da esquerda pra direita
		trab.criar_escrita(imagem, '200',(190,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#2valor 200 da esquerda para direita
		trab.criar_escrita(imagem, '15',(310,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#3valor 15 da esquerda para direita
		trab.criar_escrita(imagem, '100',(350,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#4valor 100 da esquerda para direita
		trab.criar_escrita(imagem, '200',(490,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#5valor 200 da esquerda para direita
		trab.criar_escrita(imagem, '15',(620,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#6valor 15 da esquerda para direita
		trab.criar_escrita(imagem, '225',(740,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#7valor 225 da esquerda para direita
		trab.criar_escrita(imagem, '15',(885,60),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#8valor 15 da esquerda para direita
		
		#Escrevendo na planta lado direito
		trab.criar_escrita(imagem, '15',(950,112),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#1valor 15 de cima para baixo
		trab.criar_escrita(imagem, '270',(950,250),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#2valor 270 de cima para baixo
		trab.criar_escrita(imagem, '15',(950,397),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#3valor 15 da esquerda para direita
		
		#Escrevendo na planta lado esquerdo
		trab.criar_escrita(imagem, '15',(50,112),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#1 valor 15 de cima para baixo
		trab.criar_escrita(imagem, '270',(50,270),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#2 valor 270 de cima para baixo
		trab.criar_escrita(imagem, '15',(50,397),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#3 valor 15 de cima para baixo
		trab.criar_escrita(imagem, '300',(10,270),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#4 valor de 300 do lado de fora
		
		#Escrevendo na planta do lado de baixo
		trab.criar_escrita(imagem, '15',(100,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#1 valor 15 da esquerda para a direita
		trab.criar_escrita(imagem, '200',(190,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#2valor 200 da esquerda para direita
		trab.criar_escrita(imagem, '130',(350,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#3valor 130 da esquerda para direita
		trab.criar_escrita(imagem, '200',(490,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#4valor 200 da esquerda para direita
		trab.criar_escrita(imagem, '15',(620,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#5valor 15 da esquerda para direita
		trab.criar_escrita(imagem, '225',(740,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#6valor 225 da esquerda para direita
		trab.criar_escrita(imagem, '15',(885,437),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#7valor 15 da esquerda para direita
		
		#Escrevendo dentro da planta
		trab.criar_escrita(imagem, 'QUARTO',(720,307),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor quarto
		trab.criar_escrita(imagem, '70',(620,347),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 70
		trab.criar_linha(imagem, (619, 348), (645,348), (0,0,0), 1)#Criando a linha da divisão de 70 por 210
		trab.criar_escrita(imagem, '210',(620,362),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 210
		trab.criar_escrita(imagem, 'SALA',(520,307),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor sala
		trab.criar_escrita(imagem, '80',(320,347),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 80
		trab.criar_linha(imagem, (319, 348), (345,348), (0,0,0), 1)#Criando a linha da divisão de 80 por 210
		trab.criar_escrita(imagem, '210',(320,362),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 210
		trab.criar_escrita(imagem, '60',(353,270),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 80
		trab.criar_linha(imagem, (353, 270), (379,270), (0,0,0), 1)#Criando a linha da divisão de 80 por 210
		trab.criar_escrita(imagem, '210',(350,282),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor 210
		trab.criar_escrita(imagem, 'COZINHA',(190,307),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),1,cv2.LINE_AA)#valor cozinha
		
					
		imagem = trab.exibir_imagem(imagem, "Casa")
		
						
	elif tarefa == 21:
		imagem = cv2.imread("apollo8.jpg")
		trab.salvar_imagem(imagem, "apollo8.jpeg")
				
							
	elif tarefa == 22:
		continuar = False
		print("Fechando o programa")
	else:
		print("Opção invalida. Digite novamente")
	tarefa = int(input("\n1 - Cachorro \n2 - Linha \n3 - Círculo \n4 - Retangulo \n5 - Elipse \n6 - Escrita \n7 - Poligono \n8 - Histograma \n9 - Histograma_dados \n10 - Histograma_pontos \n11 - Histograma de linhas\n12 - Tons de cinza\n13 - BGR para RGB\n14 - Recortar Imagem\n15 - Pedir para recortar\n16 - Redimencionar imagem\n17 - Rotacionar imagem\n18 - Deslocamento de Imagem\n19 - Detectar faces\n20 - Desenhar planta\n21 - Salvar Imagem\n22 - Sair\n  Escolha a tarefa: "))




