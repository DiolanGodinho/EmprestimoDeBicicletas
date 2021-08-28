from Cliente import Cliente
from Loja import Loja
import unittest


class Teste(unittest.TestCase):
    def setUp(self) -> None:
        self.loja = Loja("Rio Vermelho", 23)
        self.cliente = Cliente("Diolan")
        self.loja2 = "Boa Viagem"
        #self.cliente.solicitaEmprestimo(self.loja, 2, "Hora")

    # Teste para solicitaEmprestimo(self)

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

# teste da Função devolve Bicicletas

    def testaDevolveBicicletasSemProblemas(self):
        print("\nTeste de cliente devolver bicicletas sem problemas.")
        
        self.cliente.solicitaEmprestimo(self.loja,10,"Hora")
     
        self.assertEqual(self.cliente.devolveBicicletas(self.loja), 0)
        ## não sei valor deste impréstimo. exatamente certo

    def testaDevolveBicicletasClienteSemEmprestimo(self):
        self.cliente1 = Cliente("Victor")
        self.assertEqual(self.cliente1.devolveBicicletas(self.loja),0)   

   

   


if __name__ == "__main__":
    store = Loja("Rio Vermelho","10")
    unittest.main()

    


