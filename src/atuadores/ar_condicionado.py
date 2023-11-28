from time import sleep

def iniciar_ar_condicionado():
    return None

def atuar_sobre_o_ar_condicionado(acao, objeto):
    if acao == 'ligar' and objeto == 'ar':
        print("Ligando o ar-condicionado")
        sleep(5)
    elif acao == 'desligar' and objeto == 'ar':
        print("Desligando o ar-condicionado")
        sleep(5)