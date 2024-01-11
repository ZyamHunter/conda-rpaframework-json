import unittest
import os


def suite():
    loader = unittest.TestLoader()
    return loader.discover(start_dir=os.path.dirname(os.path.abspath(__file__)), pattern='test_*.py')

if __name__ == "__main__":
    # Execução dos testes
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    result = runner.run(test_suite)

    print(result)
    print(test_suite)
