import unittest
from chico import *
from testes.audios import *

class TestePorta(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.configuracao = iniciar()
        self.assertTrue(self.iniciado)

    def teste_abrir_porta(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, ABRIR_PORTA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_destravar_porta(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, DESTRAVAR_PORTA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_fechar_porta(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, FECHAR_PORTA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_travar_porta(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, TRAVAR_PORTA)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)