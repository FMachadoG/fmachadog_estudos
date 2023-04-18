from unittest import TestCase
from app.app import converte_F_pra_C, converte_C_pra_F


# COVERAGE EXEC
# > pip install coverage
# > python -m coverage run -m unittest teste.py -v
# > coverage report
# > coverage html

class TestConversaoFparaC(TestCase):
    def test_do_ze(self):
        valores = [(32, 0), (-40, -40)]

        for _input, _output in valores:
            with self.subTest(input=_input, output=_output):
                self.assertEqual(converte_F_pra_C(_input), _output)

    def test_deve_retornar_0_quando_receber_32(self):
        self.assertEqual(converte_F_pra_C(32), 0)

    def test_deve_retornar__40_quando_receber__40(self):
        self.assertEqual(converte_F_pra_C(-40), -40)

    def test_deve_retornar_37_77_quando_receber_100(self):
        self.assertAlmostEqual(converte_F_pra_C(100), 37.77, places=1)


class TestConversaoCparaF(TestCase):
    def test_deve_retornar_32_quando_receber_0(self):
        self.assertEqual(converte_C_pra_F(0), 32)

    def test_deve_retornar__40_quando_receber__40(self):
        self.assertEqual(converte_C_pra_F(-40), -40)

    def test_deve_retornar_100_quando_receber_37_77(self):
        self.assertAlmostEqual(converte_C_pra_F(37.77), 100, places=1)
