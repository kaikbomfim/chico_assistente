import unittest
from chico import *
from testes.audios import *

class TesteArCondicionado(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.configuracao = iniciar()
        self.assertTrue(self.iniciado)

    def teste_ligar_ar_condicionado(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, LIGAR_AR_CONDICIONADO)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)

    def teste_desligar_ar_condicionado(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, DESLIGAR_AR_CONDICIONADO)
        self.assertTrue(tem_transcricao)
        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, self.configuracao)
        valido, _, _ = validar_comando(tokens, self.configuracao)
        self.assertTrue(valido)