from Loja import Loja
from Cliente import Cliente
from Emprestimo import Emprestimo
import unittest 



class classIntegrationLoja(unittest.TestCase):
    
    def TetsTest(self):
        c = Loja.Loja('Victor','10')

        menssage = "Teste assetIsInstance"
        self.assertIsNotInstance(c,Loja.Loja('Victor','10'),menssage)



if __name__ == '__main__':
    unittest.main()
    


