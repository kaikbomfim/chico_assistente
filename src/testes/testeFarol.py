import unittest
from chico import *
from testes.audios import *

class TesteFarol(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.configuracao = iniciar()
        self.assertTrue(self.iniciado)

    def teste_ligar_farol(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, LIGAR_FAROL)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_desligar_farol(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, DESLIGAR_FAROL)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)