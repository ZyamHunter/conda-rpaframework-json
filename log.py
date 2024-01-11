import unittest
import logging

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SeusTestes(unittest.TestCase):

    def setUp(self):
        # Configurações de inicialização, se necessário
        pass

    def tearDown(self):
        # Limpeza após cada teste, se necessário
        pass

    def test_exemplo_1(self):
        # Seu código de teste aqui
        self.assertTrue(True)

    def test_exemplo_2(self):
        # Seu código de teste aqui
        self.assertEqual(1, 1)

# Implementar um Test Runner personalizado
class CustomTestRunner(unittest.TextTestResult):

    def addSuccess(self, test):
        super().addSuccess(test)
        logger.info(f"SUCESSO: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        logger.error(f"FALHA: {test}\n{err}")

    def addError(self, test, err):
        super().addError(test, err)
        logger.error(f"ERRO: {test}\n{err}")

# Função principal
def main():
    # Carregar os testes automaticamente
    suite = unittest.TestLoader().loadTestsFromTestCase(SeusTestes)

    # Configurar e executar o Test Runner personalizado
    runner = unittest.TextTestRunner(resultclass=CustomTestRunner)
    result = runner.run(suite)

    # Log dos resultados globais
    logger.info("\nResultados globais:")
    logger.info(f"Total de testes executados: {result.testsRun}")
    logger.info(f"Sucessos: {result.testsRun - len(result.failures) - len(result.errors)}")
    logger.info(f"Falhas: {len(result.failures)}")
    logger.info(f"Erros: {len(result.errors)}")

if __name__ == '__main__':
    main()
