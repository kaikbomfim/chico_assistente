from time import sleep

def iniciar_janela():
    return None

def atuar_sobre_a_janela(acao, objeto):
    if acao in ['abrir', 'destravar'] and objeto == 'janela':
        if acao == 'abrir':
            print("Abrindo a janela")
            sleep(3)
        else:
            print("Destravando a janela")
            sleep(3)
    elif acao in ['fechar', 'travar'] and objeto == 'janela':
        if acao == 'fechar':
            print("Fechando a janela")
            sleep(3)
        else:
            print("Travando a janela")
            sleep(3)