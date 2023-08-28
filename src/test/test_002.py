import unittest
class test_002(unittest.TestCase):
    def setUp(self):
        pass

    def test_002(self):
        self.variableA = 50
        self.variableB = 50
        self.resultado = self.variableA + self.variableB

        self.assertEqual(self.variableA, self.variableB, "los valores son distintos")

    def test_003(self):
        self.variableA = 50
        self.variableB = 40
        self.resultado = self.variableA + self.variableB

        self.assertNotEqual(self.variableA, self.variableB, "los valores son distintos")

    def test_004(self):
        self.variableA = 50

        if self.variableA >= 10:
           self.resultado = True
        else:
            self.resultado = False


        self.assertTrue(self.resultado, f'el valor no es verdadero: {self.variableA}')

    def test_005(self):
        self.variableA = 'Bienvenido a la clase unittest'
        self.variableB = 'unittestxx'


        self.assertIn(self.variableB, self.variableA, f'No coinciden')


    def tearDown(self):  # aca es donde se evalúa y se registra la prueba
        pass

if __name__ == '__main__':
    unittest.main()
