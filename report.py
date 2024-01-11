import unittest

class CustomTestResult(unittest.TestResult):
    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super().__init__(stream, descriptions, verbosity)
        self.test_status = {}

    def startTest(self, test):
        super().startTest(test)
        self.test_status[test] = {'Com sucesso': 0, 'Com falha': 0}

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_status[test]['Com sucesso'] += 1

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_status[test]['Com falha'] += 1

def run_tests_and_get_results(test_suite):
    result = CustomTestResult()
    test_suite.run(result)
    return result

def get_test_status(result):
    message = 'Resultados dos Testes:\n'
    for test, data in result.test_status.items():
        message += f'{test}:\n'
        message += f' ✅Com sucesso: {data["Com sucesso"]}\n'
        message += f' ❌Com falha: {data["Com falha"]}\n'
    return message

if __name__ == '__main__':
    # Execute os testes e obtenha os resultados
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestJson)
    test_results = run_tests_and_get_results(test_suite)

    # Obtenha e imprima o status dos testes
    print(get_test_status(test_results))
