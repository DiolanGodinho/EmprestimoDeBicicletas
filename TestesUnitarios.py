import unittest
from Cliente import Cliente
from Loja import Loja
from Emprestimo import Emprestimo

class Testes(unittest.TestCase):
    def setUp(self) -> None:
        self.loja = Loja("Rio Vermelho", 23)
        self.cliente = Cliente("Diolan")
        self.loja2 = "Rio Vermelho"
        self.cliente.solicitaEmprestimo(self.loja, 2, "Hora")

    # ********************** Cliente: Solicita Emprestimo **********************************

    def testaSolicitaEmprestimoSemProblemas(self):
        print("\nTeste de cliente solicitar emprestimo sem problemas.")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja, 2, "Hora"), 2)

    def testaSolicitaEmprestimoComParametroLojaDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro loja de tipo incorreto.")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja2, 2, "Hora"), 0)

    def testaSolicitaEmprestimoComParametroQuantidadeDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro qtde de tipo incorreto")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja2, "@", "Hora"), 0)

    def testaSolicitaEmprestimoComParametroModalidadeDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro modalidade de tipo incorreto")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja2, 2, 24), 0)

    def testaSolicitaEmprestimoComParametroQuantidadeInvalido(self):
        print("\nTeste de cliente solicitar emprestimo de quantidade invalida.")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja2, 0, "Hora"), 0)

    def testaSolicitaEmprestimoComParametroModalidadeInvalido(self):
        print("\nTeste de cliente solicitar emprestimo de modalidade invalida.")
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja2, 0, "Mes"), 0)

    # ********************** Cliente: Devolve Bicicletas **********************************
    
    def testaDevolveBicicletasSemProblemas(self):
        print("\nTeste de cliente devolver bicicletas sem problemas.")
        self.assertEqual(self.cliente.devolveBicicletas(2, "Rio Vermelho"), 2)

if __name__ == "main":
    unittest.main()