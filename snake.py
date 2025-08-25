import pygame #biblioteca para desnvolver o jogo
from pygame.locals import *
from sys import exit
from random import randint

pygame.init() #inicializa o pygame

#cores
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

#variaveis do jogo
lista_cobra = []
pontos = 0
comprimento_inicial = 5
velocidade = 10
morreu = False

#coordenadas
tamanho_tela = (800,600)
cobra_x, cobra_y = 800/2, 600/2
maca_x, maca_y = randint(1,800), randint(1,600)
x_controle, y_controle = velocidade, 0


fps = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("snake game")
fonte = pygame.font.SysFont("arial", 40, True, True)

#desenha a cobra
def aumenta_cobra(lista_cobra):
	for XeY in lista_cobra:
		pygame.draw.rect(tela, verde, (XeY[0], XeY[1], 20, 20))

def reinicar_jogo():
	global pontos, comprimento_inicial, cobra_x, cobra_y, lista_cobra, lista_cabeca, maca_x, maca_y, morreu
	pontos = 0
	comprimento_inicial = 5
	cobra_x, cobra_y = 800/2, 600/2
	lista_cobra = []
	lista_cabeca = []
	maca_x, maca_y = randint(1,800), randint(1,600)
	morreu = False

while True:

	tela.fill((branco))#pintando o fundo
	fps.tick(30)#fps

	#mensagem
	mensagem = f'Pontos: {pontos}'
	texto_formatado = fonte.render(mensagem, False, preto)


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

		if event.type == KEYDOWN:
			if event.key == K_a:
				if x_controle == velocidade:
					pass
				else:
					x_controle = -velocidade
					y_controle = 0

			if event.key == K_d:
				if x_controle == -velocidade:
					pass
				else:
					x_controle = velocidade
					y_controle = 0

			if event.key == K_w:
				if y_controle == velocidade:
					pass
				else:
					x_controle = 0
					y_controle = -velocidade

			if event.key == K_s:
				if y_controle == -velocidade:
					pass
				else:
					x_controle = 0
					y_controle = velocidade

	if cobra_x < 0:
		cobra_x = tamanho_tela[0]
	elif cobra_x > tamanho_tela[0]:
		cobra_x = 0
	if cobra_y < 0:
		cobra_y = tamanho_tela[1]
	elif cobra_y > tamanho_tela[1]:
		cobra_y = 0

	cobra_x += x_controle
	cobra_y += y_controle
	#desenhando
	cobra = pygame.draw.rect(tela, verde, (cobra_x, cobra_y, 20,20))
	maca = pygame.draw.rect(tela, vermelho,(maca_x, maca_y, 20, 20)) 

	#verifica colisão da cobra
	if cobra.colliderect(maca):
		maca_x = randint(40, 800)
		maca_y = randint(50, 600)
		pontos = pontos + 1
		comprimento_inicial += 1

	#armazena as posiçoes da cabeça da cobra
	lista_cabeca = []
	lista_cabeca.append(cobra_x)
	lista_cabeca.append(cobra_y)

	#armazena todos os valores da cobra
	lista_cobra.append(lista_cabeca)

	if lista_cobra.count(lista_cabeca) > 1:
		morreu = True
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == KEYDOWN:
				if event.key == K_r:
						reinicar_jogo()
						
	if len(lista_cobra) > comprimento_inicial:
		del lista_cobra[0]

	aumenta_cobra(lista_cobra)


	tela.blit(texto_formatado, (450, 40))
	pygame.display.update()

