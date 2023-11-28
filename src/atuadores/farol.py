from time import sleep

def iniciar_farol():
    return None

def atuar_sobre_o_farol(acao, objeto):
    if acao == 'ligar' and objeto == 'farol':
        print("Ligando o farol")
        sleep(5)
    elif acao == 'desligar' and objeto == 'farol':
        print("Desligando o farol")
        sleep(5)
