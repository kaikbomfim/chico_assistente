from testes.testeJanela import *
from testes.testePorta import *
from testes.testeFarol import *
from testes.testeArCondicionado import *
from testes.testeMotor import *
from testes.testeNomeDoAssistente import *

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeDoAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteArCondicionado))
    testes.addTest(carregador.loadTestsFromTestCase(TesteMotor))
    testes.addTest(carregador.loadTestsFromTestCase(TesteFarol))
    testes.addTest(carregador.loadTestsFromTestCase(TestePorta))
    testes.addTest(carregador.loadTestsFromTestCase(TesteJanela))

    executor = unittest.TextTestRunner()
    executor.run(testes)