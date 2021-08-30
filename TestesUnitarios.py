from Cliente import Cliente
from Loja import Loja
import unittest


class Teste(unittest.TestCase):
    def setUp(self) -> None:
        self.lojaRV = Loja("Rio Vermelho", 13)
        self.lojaBV = Loja("Boa Viagem", 18)

        self.diolan = Cliente("Diolan")
        self.victor = Cliente("Victor")
        self.brian = Cliente("Brian")

        self.diolan.solicitaEmprestimo(self.lojaRV, 2, "Hora") # R$ 1960,00
        self.victor.solicitaEmprestimo(self.lojaBV, 4, "Semana") # R$ 560,00
        self.brian.solicitaEmprestimo(self.lojaRV, 1, "Dia") # R$ 225,00

        self.diolan.devolveBicicletas(self.lojaRV)
        self.victor.devolveBicicletas(self.lojaBV)
        self.brian.devolveBicicletas(self.lojaRV)

    # Teste para solicitaEmprestimo(self)

    def testaClienteSolicitaEmprestimoSemProblemas(self):
        print("\nTeste de cliente solicitar emprestimo sem problemas.")
        self.assertEqual(self.brian.solicitaEmprestimo(self.lojaBV, 4, "Semana"), 4)

    def testaClienteSolicitaEmprestimoComParametroLojaDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro loja de tipo incorreto.")
        self.assertEqual(self.brian.solicitaEmprestimo("Boa Viagem", 4, "Semana"), 0)

    def testaClienteSolicitaEmprestimoComParametroQuantidadeDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro qtde de tipo incorreto")
        self.assertEqual(self.brian.solicitaEmprestimo(self.lojaBV, "@", "Semana"), 0)

    def testaClienteSolicitaEmprestimoComParametroModalidadeDeTipoIncorreto(self):
        print("\nTeste de cliente solicitar emprestimo com parametro modalidade de tipo incorreto")
        self.assertEqual(self.brian.solicitaEmprestimo(self.lojaBV, 2, 7), 0)    

    def testaClienteSolicitaEmprestimoComParametroQuantidadeInvalido(self):
        print("\nTeste de cliente solicitar emprestimo de quantidade invalida.")
        self.assertEqual(self.brian.solicitaEmprestimo(self.lojaBV, 0, "Semana"), 0)    
        
    def testaClienteSolicitaEmprestimoComParametroModalidadeInvalido(self):
        print("\nTeste de cliente solicitar emprestimo de modalidade invalida.")
        self.assertEqual(self.brian.solicitaEmprestimo(self.lojaBV, 0, "Mes"), 0)

    # teste da Função devolve Bicicletas

    def testaClienteDevolveBicicletasSemProblemas(self):
        print("\nTeste de cliente devolver bicicletas sem problemas.")
        self.assertEqual(self.victor.devolveBicicletas(self.lojaBV), 560)

    def testaClienteDevolveBicicletasComParametroLojaDeTipoIncorreto(self):
        print("\nTeste de cliente devolver bicicletas com parametro loja de tipo incorreto.")
        self.assertEqual(self.victor.devolveBicicletas(None), 0)

    def testaClienteDevolveBicicletasClienteNaoEstaNaListaDeEmprestimosDaLoja(self):
        print("\nTeste de cliente devolver bicicletas com seu nome não constante da lista de emprestimos da loja.")
        self.assertEqual(self.diolan.devolveBicicletas(self.lojaBV), 0)

    # Testes de Cliente Paga Emprestimo

    def testaClientePagaEmprestimoSemTrocoSemProblemas(self):
        print("\nTeste de cliente paga emprestimos com valor exato sem problemas.")
        self.assertEqual(self.victor.pagaEmprestimo(560, self.lojaBV), 0)

    def testaClientePagaEmprestimoComTrocoSemProblemas(self):
        print("\nTeste de cliente paga emprestimos com valor acima do devido sem problemas.")
        self.assertEqual(self.victor.pagaEmprestimo(600, self.lojaBV), 0)

    def testaClientePagaEmprestimoComValorDesembolsadoMenorDoQueDevido(self):
        print("\nTeste de cliente paga emprestimos com valor menor do que o devido.")
        self.assertEqual(self.victor.pagaEmprestimo(500, self.lojaBV), -1)
    
    def testaClientePagaEmprestimoComParametroValorDesembolsadoDeTipoIncorreto(self):
        print("\nTeste de cliente paga emprestimos com valor de tipo incorreto.")
        self.assertEqual(self.victor.pagaEmprestimo(None, self.lojaBV), -1)

    def testaClientePagaEmprestimoNomeNaoConstaNaListaDeEmprestimos(self):
        print("\nTeste de cliente paga emprestimos com loja de tipo incorreto.")
        self.assertEqual(self.diolan.pagaEmprestimo(1960, self.lojaBV), -1)

    # Testes de Loja Recebe Pedido

    def testaLojaRecebePedidoSemProblemas(self):
        print(f"\nTeste de Loja receber pedido sem problemas.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", 4, "Semana"), True)

    def testaLojaRecebePedidoComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja receber pedido com parametro nome cliente de tipo incorreto.")
        self.assertEqual(self.lojaRV.recebePedido(None, 4, "Semana"), False)

    def testaLojaRecebePedidoComParametroQuantidadeDeTipoIncorreto(self):
        print(f"\nTeste de Loja receber pedido com parametro quantidade de tipo incorreto.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", "$", "Semana"), False)

    def testaLojaRecebePedidoComParametroModalidadeDeTipoIncorreto(self):
        print(f"\nTeste de Loja receber pedido com parametro modlalidade de tipo incorreto.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", 4, 7), False)

    def testaLojaRecebePedidoComParametroQuantidadeInvalido(self):
        print(f"\nTeste de Loja receber pedido com parametro quantidade invalido.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", -1, "Semana"), False)

    def testaLojaRecebePedidoComParametroQuantidadeMaiorDoQueEstoqueDisponivel(self):
        print(f"\nTeste de Loja receber pedido com parametro quantidade maior do que estoque disponivel.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", 20, "Semana"), False)

    def testaLojaRecebePedidoComParametroModalidadeInvalido(self):
        print(f"\nTeste de Loja receber pedido com parametro modalidade invalido.")
        self.assertEqual(self.lojaRV.recebePedido("Victor", 4, "Mes"), False)

    def testaLojaRecebePedidoDeClienteComEmprestimoEmAndamento(self):
        print(f"\nTeste de Loja receber pedido de cleinte com emprestimo em andamento.")
        self.assertEqual(self.lojaBV.recebePedido("Victor", 4, "Mes"), False)

    # Testes de Loja Empresta Bicicletas

    def testaLojaEmprestaBicicletasSemProblemas(self):
        print(f"\nTeste de Loja empresta bicicletas sem problemas.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", 4, "Semana"), 4)

    def testaLojaEmprestaBicicletasComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro nome cliente de tipo incorreto.")
        self.assertEqual(self.lojaRV.emprestaBicicletas(self.victor, 4, "Semana"), 0)

    def testaLojaEmprestaBicicletasComParametroQuantidadeDeTipoIncorreto(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro quantidade de tipo incorreto.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", None, "Semana"), 0)

    def testaLojaEmprestaBicicletasComParametroModalidadeDeTipoIncorreto(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro modlalidade de tipo incorreto.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", 4, self.lojaBV), 0)

    def testaLojaEmprestaBicicletasComParametroQuantidadeInvalido(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro quantidade invalido.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", -1, "Semana"), 0)

    def testaLojaEmprestaBicicletasComParametroQuantidadeMaiorDoQueEstoqueDisponivel(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro quantidade maior do que estoque disponivel.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", 20, "Semana"), 0)

    def testaLojaEmprestaBicicletasComParametroModalidadeInvalido(self):
        print(f"\nTeste de Loja empresta bicicletas com parametro modalidade invalido.")
        self.assertEqual(self.lojaRV.emprestaBicicletas("Victor", 4, "Mes"), 0)

    # Testes Loja Recebe Bicicletas

    def testaLojaRecebeBicicletasSemProblemas(self):
        print(f"\nTeste de Loja recebe bicicletas sem problemas.")
        self.assertEqual(self.lojaBV.recebeBicicletas("Victor"), 4)

    def testaLojaRecebeBicicletasComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja recebe bicicletas com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.recebeBicicletas(self.victor), 0)

    def testaLojaRecebeBicicletasDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja recebe bicicletas de cliente nao constante nos emprestimos.")
        self.assertEqual(self.lojaBV.recebeBicicletas("Diolan"), 0)

    # Testes Loja Finaliza Emprestimo

    def testaLojaFinalizaEmprestimoSemProblemas(self):
        print(f"\nTeste de Loja finaliza emprestimo sem problemas.")
        self.assertEqual(self.lojaBV.finalizaEmprestimo("Victor"), True)

    def testaLojaFinalizaEmprestimoComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja finaliza emprestimo com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.finalizaEmprestimo(None), False)

    def testaLojaFinalizaEmprestimoDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja finaliza emprestimo de cliente nao constante nos emprestimos.")
        self.assertEqual(self.lojaBV.finalizaEmprestimo("Diolan"), False)

    # Testes Loja Calcula Valor Do Emprestimo

    def testaLojaCalculaValorEmprestimoSemProblemas(self):
        print(f"\nTeste de Loja calcula valor do emprestimo sem problemas.")
        self.assertEqual(self.lojaBV.calculaValorEmprestimo("Victor"), 560)

    def testaLojaCalculaValorEmprestimoComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja calcula valor do emprestimo com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.calculaValorEmprestimo(4), 0)

    def testaLojaCalculaValorEmprestimoDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja calcula valor do emprestimo de cliente nao constante nos emprestimos.")
        self.assertEqual(self.lojaBV.calculaValorEmprestimo("Diolan"), 0)

    # Testes Loja Determina Desconto

    def testaLojaDeterminaDescontoClienteComDireitoAdescontoSemProblemas(self):
        print(f"\nTeste de Loja determina desconto do emprestimo com desconto sem problemas.")
        self.assertEqual(self.lojaBV.determinaDesconto("Victor"), 0.7)

    def testaLojaDeterminaDescontoClienteSemDireitoAdescontoSemProblemas(self):
        print(f"\nTeste de Loja determina desconto do sem desconto emprestimo sem problemas.")
        self.assertEqual(self.lojaRV.determinaDesconto("Diolan"), 1)

    def testaLojaDeterminaDescontoComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja determina desconto do emprestimo com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.determinaDesconto(True), -1)

    def testaLojaDeterminaDescontoDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja determina desconto do emprestimo de cliente nao constante nos emprestimos.")
        self.assertEqual(self.lojaBV.determinaDesconto("Diolan"), -1)

    # Testes Loja Calcula Periodos do Emprestimo

    def testaLojaCalculaPeriodosNaModalidadeSemanaSemProblemas(self):
        print(f"\nTeste de Loja calcula periodos do emprestimo na modalidade 'semana' sem problemas.")
        self.assertEqual(self.lojaBV.calculaPeriodos("Victor"), 2)

    def testaLojaCalculaPeriodosNaModalidadeDiaSemProblemas(self):
        print(f"\nTeste de Loja calcula periodos do emprestimo na modalidade 'dia' sem problemas.")
        self.assertEqual(self.lojaRV.calculaPeriodos("Brian"), 9)

    def testaLojaCalculaPeriodosNaModalidadeHoraSemProblemas(self):
        print(f"\nTeste de Loja calcula periodos do emprestimo na modalidade 'hora' sem problemas.")
        self.assertEqual(self.lojaRV.calculaPeriodos("Diolan"), 196)

    def testaLojaCalculaPeriodosComParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja calcula periodos do emprestimo com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.calculaPeriodos(4), 0)

    def testaLojaCalculaPeriodosDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja calcula periodos do emprestimo de cliente nao constante nos emprestimos.")
        self.assertEqual(self.lojaBV.calculaPeriodos("Diolan"), 0)

    # Testes de Loja Recebe Pagamentos

    def testaLojaRecebePagamentoIgualAoValorDevido(self):
        print(f"\nTeste de Loja recebe pagamento igual ao valor devido.")
        self.assertEqual(self.lojaBV.recebePagamento("Victor", 560), 560)

    def testaLojaRecebePagamentoAcimaDoValorDevido(self):
        print(f"\nTeste de Loja recebe pagamento acima do valor devido.")
        self.assertEqual(self.lojaBV.recebePagamento("Victor", 600), 560)

    def testaLojaRecebePagamentoAbaixoDoValorDevido(self):
        print(f"\nTeste de Loja recebe pagamento abaixo do valor devido.")
        self.assertEqual(self.lojaBV.recebePagamento("Victor", 500), 0)

    def testaLojaRecebePagamentoParametroNomeClienteDeTipoIncorreto(self):
        print(f"\nTeste de Loja recebe pagamento com parametro nome do cliente de tipo incorreto.")
        self.assertEqual(self.lojaBV.recebePagamento(self.victor, 600), 0)

    def testaLojaRecebePagamentoParametroValorPagoDeTipoIncorreto(self):
        print(f"\nTeste de Loja recebe pagamento com parametro valor pago de tipo incorreto.")
        self.assertEqual(self.lojaBV.recebePagamento("Victor", "Seiscentos"), 0)

    def testaLojaRecebePagamentoParametroValorPagoInvalido(self):
        print(f"\nTeste de Loja recebe pagamento com parametro valor pago invalido.")
        self.assertEqual(self.lojaBV.recebePagamento("Victor", -10), 0)

    def testaLojaRecebePagamentoDeClienteQueNaoConstaNosEmprestimos(self):
        print(f"\nTeste de Loja recebe pagamento de cliente que nao consta nos emprestimos.")
        self.assertEqual(self.lojaBV.recebePagamento("Diolan", 2000), 0)
    
if __name__ == "__main__":
    unittest.main()
