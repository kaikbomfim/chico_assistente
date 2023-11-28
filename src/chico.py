import speech_recognition as reconhecedor
from nltk import word_tokenize, corpus
from os import path
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_RAIZ = path.abspath(path.dirname(__file__))
ARQUIVO_DE_CONFIGURACAO = path.join(CAMINHO_RAIZ, "..\\config.json")

from atuadores import motor, farol, ar_condicionado, janela, porta

ATUADORES = [
    {
        "nome": "motor",
        "iniciar": motor.iniciar_motor,
        "atuacao": motor.atuar_sobre_o_motor
    },
    {
        "nome": "farol",
        "iniciar": farol.iniciar_farol,
        "atuacao": farol.atuar_sobre_o_farol
    },
    {
        "nome": "porta",
        "iniciar": porta.iniciar_porta,
        "atuacao": porta.atuar_sobre_a_porta
    },
    {
        "nome": "janela",
        "iniciar": janela.iniciar_janela,
        "atuacao": janela.atuar_sobre_a_janela
    },
    {
        "nome": "ar condicionado",
        "iniciar": ar_condicionado.iniciar_ar_condicionado,
        "atuacao": ar_condicionado.atuar_sobre_o_ar_condicionado
    }
]

def iniciar():
    iniciado = False

    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))

    configuracao = {
        "palavras_de_parada": palavras_de_parada
    }

    configuracao.update({'reconhecedor':reconhecedor.Recognizer()})

    try:
        with open(ARQUIVO_DE_CONFIGURACAO, 'r', encoding='utf-8') as arquivo:
            
            assistente = dict(json.load(arquivo))
            
            configuracao.update({'nome_assistente':assistente.get('nome')})
            configuracao.update({'acoes':assistente.get('acoes')})
            
            arquivo.close()

            iniciado = True
    except:
        pass

    for atuador in ATUADORES:
        atuador['iniciar']()

    return iniciado, configuracao

def escutar_fala(configuracao):
    tem_fala = False

    with reconhecedor.Microphone() as fonte_de_audio:
        configuracao['reconhecedor'].adjust_for_ambient_noise(fonte_de_audio)

        print("Fale alguma coisa...")
        try:
            fala = configuracao['reconhecedor'].listen(fonte_de_audio, timeout=4)

            tem_fala = True
        except:
            pass
    
    return tem_fala, fala

def processar_audio_de_comando(configuracao, arquivo_de_audio):
    tem_transcricao, transcricao = False, None

    with reconhecedor.AudioFile(arquivo_de_audio) as fonte_de_audio:
        fala = configuracao['reconhecedor'].listen(fonte_de_audio)

        try:
            transcricao = configuracao['reconhecedor'].recognize_google(fala, language=IDIOMA_FALA)
            tem_transcricao = True
        except:
            pass
    
    return tem_transcricao, transcricao

def transcrever_fala(fala, configuracao):
    tem_transcricao = False

    try:
        transcricao = configuracao['reconhecedor'].recognize_google(fala, language=IDIOMA_FALA)
        tem_transcricao = True
    except:
        pass

    return tem_transcricao, transcricao

def tokenizar(transcricao):

    tokens = word_tokenize(transcricao)

    return tokens

def eliminar_palavras_de_parada(tokens, configuracao):
    tokens_filtrados = []

    for token in tokens:
        if token not in configuracao["palavras_de_parada"]:
            tokens_filtrados.append(token)
    
    return tokens_filtrados

def validar_comando(tokens, configuracao):
    valido, acao, objeto = False, None, None

    if len(tokens) >= 3:
        if configuracao['nome_assistente'] == tokens[0]:
            acao = tokens[1]
            objeto = tokens[2]

            for acao_prevista in configuracao['acoes']:
                if acao == acao_prevista['nome']:
                    if objeto in acao_prevista['objetos']:
                        valido = True

                        break
    
    return valido, acao, objeto

def executar_comando(acao, objeto):

    for atuador in ATUADORES:
        atuador['atuacao'](acao, objeto)

if __name__ == "__main__":
    iniciado, configuracao = iniciar()
    if iniciado:
        while True:
            try:
                tem_fala, fala = escutar_fala(configuracao)
                if tem_fala:
                    tem_transcricao, transcricao = transcrever_fala(fala, configuracao)
                    if tem_transcricao:
                        tokens = tokenizar(transcricao.lower())
                        tokens = eliminar_palavras_de_parada(tokens, configuracao)

                        valido, acao, objeto = validar_comando(tokens, configuracao)
                        if(valido):
                            executar_comando(acao, objeto)
                        else:
                            print(f"Comando inválido!")
            except:
                pass