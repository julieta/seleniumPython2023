import unittest


class test_001(unittest.TestCase):

    def setUp(self):          #aca se define los datos de pruebas
        self.Variable_a = 6
        self.Variable_b = 4

    def test_001(self):             #aca se define el tests y el nombre debe comenzar llamandose tests
        self.Resultado = self.Variable_a + self.Variable_b

    def tearDown(self): #aca es donde se evalúa y se registra la prueba
        self.assertTrue(self.Resultado == 10, f"El valor no es 10, es {self.Resultado}")

if __name__ == '__main__':
    unittest.main()
