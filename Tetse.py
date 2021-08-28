from Cliente import Cliente
from Loja import Loja
import unittest


class Teste(unittest.TestCase):
    def setUp(self): 
        self.loja = Loja("BikeShop's", 10)
        self.cliente = Cliente("Victor")

    def testechecaNomeLoja(self):
    
        self.assertEqual(self.cliente.solicitaEmprestimo(self.loja,2,"Hora")\
            ,2)
        
        
        
        


if __name__ == "__main__":
    unittest.main()

    


