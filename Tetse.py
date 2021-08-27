from Cliente import Cliente
from Loja import Loja
import unittest


class Teste(unittest.TestCase):
    
    def testechecaNomeLoja(self):
        loja = Loja("Bikes", 13)
        cliente = Cliente("Diolan")
        self.assertEqual(cliente.solicitaEmprestimo(loja,2,"Hora"),3)
        
        
        
        


if __name__ == "__main__":
    unittest.main()

    


