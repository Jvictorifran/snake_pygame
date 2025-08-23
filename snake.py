import pygame #biblioteca para desnvolver o jogo
from pygame.locals import *
from sys import exit
import estruturas
from random import randint

pygame.init() #inicializa o pygame

#variaveis cobra
cabeça_cobra = [estruturas.tamanho_da_tela[0]/2, estruturas.tamanho_da_tela[1]/2]

corpo_cobra_x, corpo_cobra_y = cabeça_cobra[0], cabeça_cobra[1]

comida = [randint(1, 600), randint(1, 400)]

tamanho_cobra = 0
corpo_cobra = [cabeça_cobra]
desenho_cobra = []

#eventos do jogo
fps = pygame.time.Clock()
tela = pygame.display.set_mode(estruturas.tamanho_da_tela)


while True:

	tela.fill((0, 0, 0))
	fps.tick(120)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit
			exit()

	#andando com a cobra
	if pygame.key.get_pressed()[K_a]:
		cabeça_cobra[0] = cabeça_cobra[0] - 2
	if pygame.key.get_pressed()[K_d]:
		cabeça_cobra[0] = cabeça_cobra[0] + 2
	if pygame.key.get_pressed()[K_w]:
		cabeça_cobra[1] = cabeça_cobra[1] - 2
	if pygame.key.get_pressed()[K_s]:
		cabeça_cobra[1] = cabeça_cobra[1] + 2

	#desenhando
	comida = pygame.draw.rect(tela, (255, 0, 0), (comida[0], comida[1], 10, 10))

	cabeça_cobra = pygame.draw.rect(tela, (0, 255, 0),(cabeça_cobra[0], cabeça_cobra[1], 20, 20 ))


	posicao_cabeca = [cabeça_cobra[0], cabeça_cobra[1]]
	corpo_cobra.append(posicao_cabeca)
	
	if cabeça_cobra.colliderect(comida):
		tamanho_cobra += 1
		estruturas.comeu(comida)
	if tamanho_cobra != 0:
		for i in range(tamanho_cobra):
			desenho_cobra.append = pygame.draw.rect(tela, (0, 255, 0), cabeça_cobra[0] - 1, cabeça_cobra[1] - 1, 30, 30)
			del corpo_cobra


		
	
	
		
	
	

	pygame.display.update()
