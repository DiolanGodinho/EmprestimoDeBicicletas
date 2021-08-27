from datetime import datetime, timedelta, timezone
from random import choice
import math
from IntervalosDeTempo import temposDeEmprestimo
from Emprestimo import Emprestimo

class Loja(object):

    VALOR_POR_MODALIDADE = {
        "Hora": 5,
        "Dia": 25,
        "Semana": 100
    }
    MODALIDADES_DISPONIVEIS = ["Hora", "Dia", "Semana"]

    def __init__(self, nome, estoque) -> None:
        try:
            if not (isinstance(nome, str) and isinstance(int(estoque), int)):
                raise TypeError("tipos de parâmetros inválidos")
            
            print(f"\nLoja: instanciando a classe sob o nome {nome} e com estoque de {estoque} bicicleta(s).")

            self.nome = nome
            self.estoque = estoque
            self.emprestimos = {}
            self.caixa = 0
        
        except TypeError as error:
            print(f"\nLoja: classe nao instanciada sob o nome {nome} e com estoque de {estoque} bicicleta(s). Motivo: {error}.")

        except:
            print(f"\nLoja: classe nao instanciada sob o nome {nome} e com estoque de {estoque} bicicleta(s). Motivo: desconhecido.")

    def recebePedido(self, nomeCliente, quantidade, modalidade):
        '''
        Recebe uma string nomeCliente, um inteiro quantidade e uma string modalidade. 
        Devolve True se o pedido for aceito e False em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(int(quantidade), int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida")

            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise ValueError("modalidade Inválida")

            if quantidade > self.estoque:
                raise SystemError("estoque indisponível")

            print(f"\nLoja: pedido em nome de {nomeCliente} de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} aceito.")
            return True
            
        except TypeError as error:
            print(f"\nLoja: pedido em nome de {nomeCliente} de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except ValueError as error:
            print(f"\nLoja: pedido em nome de {nomeCliente} de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except SystemError as error:
            print(f"\nLoja: pedido em nome de {nomeCliente} de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except:
            print(f"\nLoja: pedido em nome de {nomeCliente} de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: desconhecido.")
            return False

    def emprestaBicicletas(self, nomeCliente, quantidade, modalidade):
        '''
        Recebe uma string nomeCliente, um inteiro quantidade e uma string modalidade. 
        Devolve o inteiro quantidade de bicicletas emprestadas se o empréstimo for efetuado e 0 em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(int(quantidade), int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida")

            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise ValueError("Modalidade Inválida")

            if quantidade > self.estoque:
                raise SystemError("estoque indisponível")

            if nomeCliente in self.emprestimos:
                raise SystemError("cliente com empréstimo em andamento")

            self.estoque -= quantidade
            self.emprestimos[nomeCliente] = Emprestimo(nomeCliente, self.nome, quantidade, modalidade)

            print(f"\nLoja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} efetuado com sucesso. Estoque {self.estoque}.")

            return quantidade
            
        except TypeError as error:
            print(f"\nLoja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return 0

        except ValueError as error:
            print(f"\nLoja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"\nLoja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: {error}.")
            return 0

        except:
            print(f"\nLoja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: desconhecido")
            return 0

    def recebeBicicletas(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o inteiro quantidade devolvida se o recebimento das bicicletas for efetuado e 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipos de parâmetros inválidos")

            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            quantidadeDevolvida = self.emprestimos[nomeCliente].quantidade
            self.estoque += quantidadeDevolvida

            print(f"\nLoja: recebimento de {quantidadeDevolvida} bicicletas do {nomeCliente} na loja {self.nome} efetuado com sucesso. Estoque {self.estoque}.")

            self.finalizaEmprestimo(nomeCliente)
            
            return quantidadeDevolvida

        except TypeError as error:
            print(f"\nLoja: recebimento da(s) bicicleta(s) em nome de {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"\nLoja: recebimento da(s) bicicleta(s) em nome de {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: {error}.")
            return 0

        except:
            print(f"\nLoja: recebimento da(s) bicicleta(s) em nome de {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: desconhecido")
            return 0

    def finalizaEmprestimo(self, nomeCliente):
        '''
        Recebe uma string nomeCliente.
        Devolve True se o empréstimo for finalizado e False em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipos de parâmetros inválidos")

            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            self.emprestimos[nomeCliente].devolucao += timedelta(weeks=1, days=1, hours=4) #choice(temposDeEmprestimo)
            devolucao = self.emprestimos[nomeCliente].devolucao
            self.emprestimos[nomeCliente].valor = self.calculaValorEmprestimo(nomeCliente)

            print(f"\nLoja: empréstimo de {nomeCliente} na loja {self.nome} finalizado em {devolucao.strftime('%d/%m/%Y %H:%M')} com sucesso.")

            return True

        except TypeError as error:
            print(f"\nLoja: empréstimo em nome de {nomeCliente} na loja {self.nome} não finalizado. Motivo {error}.")
            return False
        
        except SystemError as error:
            print(f"\nLoja: empréstimo em nome de {nomeCliente} na loja {self.nome} não finalizado. Motivo {error}.")
            return False

        except:
            print(f"\nLoja: empréstimo em nome de {nomeCliente} na loja {self.nome} não finalizado. Motivo: desconhecido")
            return False

    def calculaValorEmprestimo(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o float valor total do empréstimo se o cálculo do valor for efetuado.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            quantidade = self.emprestimos[nomeCliente].quantidade
            fatorDoTotalComDesconto = self.determinaDesconto(nomeCliente)
            modalidade = self.emprestimos[nomeCliente].modalidade
            valorDaModalidade = self.VALOR_POR_MODALIDADE[modalidade]
            periodos = self.calculaPeriodos(nomeCliente)
            valorTotal = valorDaModalidade *periodos *quantidade *fatorDoTotalComDesconto

            print(f"\nLoja: {nomeCliente} utilizou {quantidade} bicicletas na modalidade {modalidade} por {periodos} {modalidade}(s) cada uma no valor de R$ {valorDaModalidade} e com {(1-fatorDoTotalComDesconto)*100}\% de desconto, totalizando R$ {valorTotal}.")
            
            return valorTotal

        except TypeError as error:
            print(f"\nLoja: Não foi possível calcular o valor do empréstimo. Motivo: {error}")
            return 0

        except SystemError as error:
            print(f"\nLoja: Não foi possível calcular o valor do empréstimo. Motivo: {error}")
            return 0

        except:
            print(f"\nLoja: Não foi possível calcular o valor do empréstimo. Motivo: desconhecido")
            return 0

    def determinaDesconto(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o float fração do total que deve ser paga se o cálculo da mesma for efetuado, e -1 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            quantidade = self.emprestimos[nomeCliente].quantidade
            fracaoDoTotal = 1
            if quantidade >= 3:
                fracaoDoTotal -= 0.3
            print(f"\nLoja: {nomeCliente} faz jus a {(1-fracaoDoTotal)*100}% de desconto no valor total por ter feito emprestimo de {quantidade} bicicleta(s).")
            return fracaoDoTotal

        except TypeError as error:
            print(f"\nLoja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo {error}.")
            return -1

        except SystemError as error:
            print(f"\nLoja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo {error}.")
            return -1

        except:
            print(f"\nLoja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo: desconhecido")
            return -1
    
    def calculaPeriodos(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o inteiro quantidade de periodos, de acordo com a modalidade, de empréstimio das bicicletas se o cálculo for efetuado.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            tempoDoPeriodo = {
                "Hora": timedelta(hours=1),
                "Dia": timedelta(days=1),
                "Semana": timedelta(weeks=1)
            }
            retirada = self.emprestimos[nomeCliente].retirada
            devolucao = self.emprestimos[nomeCliente].devolucao
            tempoEmprestimo = devolucao - retirada
            modalidade = self.emprestimos[nomeCliente].modalidade
            periodos = math.ceil(tempoEmprestimo / tempoDoPeriodo[modalidade])

            print(f"\nLoja: {nomeCliente} emprestou bicicleta(s) na modalidade {modalidade} por {periodos} {modalidade}(s).")

            return periodos
        
        except TypeError as error:
            print(f"\nLoja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"\nLoja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except:
            print(f"\nLoja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo: desconhecido")
            return 0

    def recebePagamento(self, nomeCliente, valorPago):
        '''
        Recebe uma string nomeCliente e um float valorPago.
        Devolve o valor do empréstimo se o mesmo for liquidado e 0 em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(float(valorPago), float)):
                raise TypeError("tipos de parâmetros inválidos")
            
            if valorPago < 0:
                raise ValueError("valor de pagamento inválido")

            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome")

            valorDevido = self.emprestimos[nomeCliente].valor
            if valorPago < valorDevido:
                raise SystemError("valor de pagamento menor do que o devido")

            self.caixa += valorPago
            if valorPago > valorDevido:
                troco = valorPago - valorDevido
                self.caixa -= troco

            print(f"\nLoja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta de R$ {valorDevido} em nome de {nomeCliente} efetuado com sucesso. Caixa {self.caixa}.")

            return valorDevido

        except TypeError as error:
            print(f"\nLoja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}.")
            return 0

        except ValueError as error:
            print(f"\nLoja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}.")
            return 0

        except SystemError as error:
            print(f"\nLoja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}.")
            return 0

        except:
            print(f"\nLoja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: desconhecido.")
            return 0

# ******************* POR FAZER ************************
# 
#  Ver necessidade de getters e setters e implementá-los
#  se for o caso.
#  
#  Estudar necessidade de atributos e metodos privados
# 
# ******************************************************

# *************** Ver com Victor ***********************
# 
#  Como implementar emprestimo com retirada e devolução
# em lojas diferentes.
# 
#  Necessidade de repetiçao dos blocos try/except.
# 
# ******************************************************
