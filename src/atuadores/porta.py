from time import sleep

def iniciar_porta():
    return None

def atuar_sobre_a_porta(acao, objeto):
    if acao in ['abrir', 'destravar'] and objeto == 'porta':
        if acao == 'abrir':
            print("Abrindo a porta")
            sleep(3)
        else:
            print("Destravando a porta")
            sleep(3)
    elif acao in ['fechar', 'travar'] and objeto == 'porta':
        if acao == 'fechar':
            print("Fechando a porta")
            sleep(3)
        else:
            print("Travando a porta")
            sleep(3)