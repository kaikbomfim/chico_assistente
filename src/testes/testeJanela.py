import unittest
from chico import *
from testes.audios import *

class TesteJanela(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.configuracao = iniciar()
        self.assertTrue(self.iniciado)

    def teste_abrir_janela(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, ABRIR_JANELA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_destravar_janela(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, DESTRAVAR_JANELA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_fechar_janela(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, FECHAR_JANELA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)
        
    def teste_travar_janela(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, TRAVAR_JANELA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)