import unittest

def suma(num1, num2):
    return num1 + num2

class CajaNegraTest(unittest.TestCase):

    '''Esta función suma dos numeros enteros'''
    def test_sumas_2_numeros(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 15)

    def test_sum_2_negatives(self):
        num1 = -10
        num2 = -7

        resultado = suma(num1, num2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()            