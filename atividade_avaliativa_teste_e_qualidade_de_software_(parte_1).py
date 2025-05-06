def calcular_preco_total(idade, quantidade):
    if quantidade < 1 or quantidade > 5:
        return "Erro: A quantidade de bilhetes deve ser entre 1 e 5."

    if idade <= 12:
        preco_unitario = 10.0  #Criança
    elif idade >= 60:
        preco_unitario = 15.0  #Idoso
    else:
        preco_unitario = 30.0  #Adulto

    preco_total = preco_unitario * quantidade
    return round(preco_total, 2)

import unittest

class TesteCompleto(unittest.TestCase):

    # === CLASSES DE EQUIVALÊNCIA ===

    # 1. Idade (1 válida, 2 inválidas)
    def test_idade_valida(self):
        self.assertEqual(calcular_preco_total(30, 2), 60.0)

    def test_idade_invalida_negativa(self):
        self.assertEqual(calcular_preco_total(-5, 2), 20.0)  #trata como criança

    def test_idade_invalida_muito_alta(self):
        self.assertEqual(calcular_preco_total(200, 1), 15.0)  #trata como idoso

    # 2. Quantidade (1 válida, 2 inválidas)
    def test_quantidade_valida(self):
        self.assertEqual(calcular_preco_total(25, 3), 90.0)

    def test_quantidade_invalida_abaixo(self):
        self.assertEqual(calcular_preco_total(25, 0), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

    def test_quantidade_invalida_acima(self):
        self.assertEqual(calcular_preco_total(25, 6), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

    # 3. Tipo por idade (conjuntos)
    def test_conjunto_valido_crianca(self):
        self.assertEqual(calcular_preco_total(10, 2), 20.0)

    def test_conjunto_invalido_string(self):
        self.assertEqual(calcular_preco_total("dez", 2), "Erro: Os valores devem ser inteiros.")

    def test_conjunto_invalido_none(self):
        self.assertEqual(calcular_preco_total(None, 2), "Erro: Os valores devem ser inteiros.")

    # 4. Condição específica: quantidade 1–5
    def test_condicao_especifica_valida(self):
        self.assertEqual(calcular_preco_total(40, 5), 150.0)

    def test_condicao_especifica_invalida_abaixo(self):
        self.assertEqual(calcular_preco_total(40, -1), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

    def test_condicao_especifica_invalida_acima(self):
        self.assertEqual(calcular_preco_total(40, 10), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

    # === ANÁLISE DE VALORES LIMITES ===

    # Idade - limites
    def test_limite_crianca(self):  # idade = 12 (último da criança)
        self.assertEqual(calcular_preco_total(12, 1), 10.0)

    def test_limite_crianca_adulto(self):  # idade = 13 (primeiro adulto)
        self.assertEqual(calcular_preco_total(13, 1), 30.0)

    def test_limite_adulto_superior(self):  # idade = 59 (último adulto)
        self.assertEqual(calcular_preco_total(59, 1), 30.0)

    def test_limite_inicio_idoso(self):  # idade = 60 (primeiro idoso)
        self.assertEqual(calcular_preco_total(60, 1), 15.0)

    # Quantidade - limites
    def test_quantidade_limite_inferior(self):  # quantidade = 1
        self.assertEqual(calcular_preco_total(30, 1), 30.0)

    def test_quantidade_limite_inferior_menos_um(self):  # quantidade = 0
        self.assertEqual(calcular_preco_total(30, 0), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

    def test_quantidade_limite_superior(self):  # quantidade = 5
        self.assertEqual(calcular_preco_total(30, 5), 150.0)

    def test_quantidade_limite_superior_mais_um(self):  # quantidade = 6
        self.assertEqual(calcular_preco_total(30, 6), "Erro: A quantidade de bilhetes deve ser entre 1 e 5.")

#Execução do teste
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TesteCompleto))