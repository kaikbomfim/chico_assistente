from time import sleep

def iniciar_motor():
    return None

def atuar_sobre_o_motor(acao, objeto):
    if acao == 'ligar' and objeto == 'motor':
        print("Ligando o motor")
        sleep(5)
    elif acao == 'desligar' and objeto == 'motor':
        print("Desligando o motor")
        sleep(5)
