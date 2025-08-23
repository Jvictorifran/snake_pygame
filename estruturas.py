from random import randint

cobra = []

tamanho_da_tela = (600, 400)

def comeu (comida):
    comida[0] = randint(1, 600)
    comida[1] = randint(1, 400)
