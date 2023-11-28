import unittest
from chico import *
from testes.audios import *

class TesteNomeDoAssistente(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.configuracao = iniciar()
        self.assertTrue(self.iniciado)
    
    def teste_reconhecer_nome(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, CHAMANDO_CHICO)
        self.assertTrue(tem_transcricao)

        tokens = tokenizar(transcricao.lower())
        self.assertEqual(tokens[0], self.configuracao['nome_assistente'])
    
    def teste_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = processar_audio_de_comando(self.configuracao, CHAMANDO_OUTRO_NOME)
        self.assertTrue(tem_transcricao)

        tokens = tokenizar(transcricao.lower())
        self.assertNotEqual(tokens[0], self.configuracao['nome_assistente'])