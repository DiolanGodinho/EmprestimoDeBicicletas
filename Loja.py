from datetime import datetime, timedelta, timezone
from random import choice
import math
from IntervalosDeTempo import temposDeEmprestimo
from Emprestimo import Emprestimo

class Loja(object):
    VALOR_HORA = 5
    VALOR_DIA = 25
    VALOR_SEMANA = 100
    MODALIDADES_DISPONIVEIS = ["Hora", "Dia", "Semana"]

    def __init__(self, nome, estoque) -> None:
        self.nome = nome
        self.estoque = estoque
        self.emprestimos = {}
        self.caixa = 0

    def recebePedido(self, nomeCliente, quantidade, modalidade):
        '''
        Recebe uma string nomeCliente, um inteiro quantidade e uma string modalidade. 
        Devolve True se o pedido for aceito e False em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(quantidade, int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida.")

            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise ValueError("modalidade Inválida.")

            if quantidade > self.estoque:
                raise SystemError("estoque indisponível.")

            print(f"Loja: pedido de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} aceito.")
            self.emprestaBicicletas(nomeCliente, quantidade, modalidade)
            return True
            
        except TypeError as error:
            print(f"Loja: pedido de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except ValueError as error:
            print(f"Loja: pedido de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except SystemError as error:
            print(f"Loja: pedido de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: {error}.")
            return False

        except:
            print(f"Loja: pedido de {quantidade} bicicletas na modalidade {modalidade} na loja {self.nome} não aceito. Motivo: desconhecido.")
            return False

    def emprestaBicicletas(self, nomeCliente, quantidade, modalidade):
        '''
        Recebe uma string nomeCliente, um inteiro quantidade e uma string modalidade. 
        Devolve o inteiro quantidade de bicicletas no estoque se o empréstimo for efetuado e -1 em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(quantidade, int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida.")

            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise ValueError("Modalidade Inválida.")

            if quantidade > self.estoque:
                raise SystemError("estoque indisponível.")

            if nomeCliente in self.emprestimos:
                raise SystemError("cliente com empréstimo em andamento.")

            print(f"Loja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} efetuado com sucesso. Estoque {self.estoque}")
            self.estoque -= quantidade
            self.emprestimos[nomeCliente] = Emprestimo(nomeCliente, self.nome, quantidade, modalidade)

            return self.estoque
            
        except TypeError as error:
            print(f"Loja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return -1

        except ValueError as error:
            print(f"Loja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return -1

        except SystemError as error:
            print(f"Loja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: {error}.")
            return -1

        except:
            print(f"Loja: empréstimo de {quantidade} bicicletas na modalidade {modalidade} para {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: desconhecido")
            return -1

    def recebeBicicletas(self, nomeCliente, quantidade):
        '''
        Recebe uma string nomeCliente e um inteiro quantidade. 
        Devolve o inteiro quantidade de bicicletas no estoque se o recebimento das bicicletas for efetuado e -1 em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(quantidade, int)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida.")

            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            if quantidade > self.emprestimos[nomeCliente][quantidade]:
                raise SystemError("quantidade de bicicletas maior do que emprestadas.")

            self.estoque += quantidade
            self.finalizaEmprestimo(self, nomeCliente)
            print(f"Loja: recebimento de {quantidade} bicicletas do {nomeCliente} na loja {self.nome} efetuado com sucesso. Estoque {self.estoque}.")
            
            return self.estoque

        except TypeError as error:
            print(f"Loja: recebimento de {quantidade} bicicletas do {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return -1

        except ValueError as error:
            print(f"Loja: recebimento de {quantidade} bicicletas do {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo {error}.")
            return -1

        except SystemError as error:
            print(f"Loja: recebimento de {quantidade} bicicletas do {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: {error}.")
            return -1

        except:
            print(f"Loja: recebimento de {quantidade} bicicletas do {nomeCliente} na loja {self.nome} não efetuado. Estoque {self.estoque}. Motivo: desconhecido")
            return -1

    def finalizaEmprestimo(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve True se o empréstimo for finalizado e False em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            self.emprestimos[nomeCliente]["devolucao"] += choice(temposDeEmprestimo)
            self.emprestimos[nomeCliente]["valor"] = self.calculaValorEmprestimo(nomeCliente)
            print(f"Loja: empréstimo de {nomeCliente} na loja {self.nome} finalizado com sucesso.")
            return True

        except TypeError as error:
            print(f"Loja: empréstimo de {nomeCliente} na loja {self.nome} não finalizado. Motivo {error}.")
            return False

        except SystemError as error:
            print(f"Loja: empréstimo de {nomeCliente} na loja {self.nome} não finalizado. Motivo {error}.")
            return False

        except:
            print(f"Loja: empréstimo de {nomeCliente} na loja {self.nome} não finalizado. Motivo: desconhecido")
            return False

    def calculaValorEmprestimo(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o float valor total do empréstimo se o cálculo do valor for efetuado.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            quantidade = self.pegaQuantidadeDeBicicletas(nomeCliente)
            fatorDesconto = self.determinaDesconto(nomeCliente)
            modalidade = self.pegaModalidade(nomeCliente)
            valorDaModalidade = self.pegaValorDa(modalidade)
            periodos = self.calculaPeriodos(nomeCliente)
            valorTotal = valorDaModalidade * periodos * fatorDesconto

            print(f"Loja: {nomeCliente} utilizou {quantidade} bicicletas na modalidade {modalidade} por {periodos} {modalidade}(s) cada uma no valor de R$ {valorDaModalidade} e com {(1-fatorDesconto)*100}\% de desconto, totalizando R$ {valorTotal}.")
            
            return valorTotal

        except TypeError as error:
            print(f"Loja: Não foi possível calcular o valor do Empréstimo. Motivo: {error}")
            return 0

        except SystemError as error:
            print(f"Loja: Não foi possível calcular o valor do Empréstimo. Motivo: {error}")
            return 0

        except:
            print(f"Loja: Não foi possível calcular o valor do Empréstimo. Motivo: desconhecido")
            return 0

    def pegaQuantidadeDeBicicletas(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o inteiro quantidade de bicicletas em nome do cliente.
        Devolve 0 se não for possível obter tal quantidade.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            quantidade = self.emprestimos[nomeCliente]["quantidade"]
            print(f"Loja: {nomeCliente} possui {quantidade} bicicletas em seu nome.")
            return quantidade
        
        except TypeError as error:
            print(f"Loja: Não foi possível obter a quantidade de bicicletas em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"Loja: Não foi possível obter a quantidade de bicicletas em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except:
            print(f"Loja: Não foi possível obter a quantidade de bicicletas em nome de {nomeCliente}. Motivo: desconhecido")
            return 0

    def determinaDesconto(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o float fração do total que deve ser paga se o cálculo da mesma for efetuado, e -1 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            quantidade = self.pegaQuantidadeDeBicicletas(nomeCliente)
            fracaoDoTotal = 1
            if quantidade >= 3:
                fracaoDoTotal -= 0.3
            print(f"Loja: {nomeCliente} faz jus a {(1-fracaoDoTotal)*100}\% de desconto no valor total.")
            return fracaoDoTotal

        except TypeError as error:
            print(f"Loja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo {error}.")
            return -1

        except SystemError as error:
            print(f"Loja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo {error}.")
            return -1

        except:
            print(f"Loja: Não foi possível verificar se {nomeCliente} tem direito a desconto. Motivo: desconhecido")
            return -1

    def pegaModalidade(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve a string modalidade de empréstimo se for possível obtê-la e a string vazia em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            modalidade = self.emprestimos[nomeCliente]["modalidade"]
            print(f"Loja: {nomeCliente} emprestou bicicletas na modalidade {modalidade}.")
            return modalidade

        except TypeError as error:
            print(f"Loja: Não foi possível obter a modalidade de empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return ""

        except SystemError as error:
            print(f"Loja: Não foi possível obter a modalidade de empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return ""

        except:
            print(f"Loja: Não foi possível obter a modalidade de empréstimo em nome de {nomeCliente}. Motivo: desconhecido")
            return ""

    def pegaValorDa(self, modalidade):
        '''
        Recebe uma string modalidade. 
        Devolve o valor da modalidade se for possível obter tal valor.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(modalidade, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise ValueError("modalidade inválida.")

            valorDaModalidade = {
                "Hora": self.VALOR_HORA,
                "Dia": self.VALOR_DIA,
                "Semana": self.VALOR_SEMANA
            }
            
            valorModalidade = valorDaModalidade[modalidade]
            print(f"Loja: a modalidade {modalidade} custa R$ {valorModalidade} por período.")

            return valorModalidade
        
        except TypeError as error:
            print(f"Loja: Não foi possível obter o valor da modalidade {modalidade}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"Loja: Não foi possível obter o valor da modalidade {modalidade}. Motivo {error}.")
            return 0

        except:
            print(f"Loja: Não foi possível obter o valor da modalidade {modalidade}. Motivo: desconhecido")
            return 0
    
    def calculaPeriodos(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o inteiro quantidade de periodos, de acordo com a modalidade, de empréstimio das bicicletas se o cálculo for efetuado.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            tempoDoPeriodo = {
                "Hora": timedelta(hours=1),
                "Dia": timedelta(days=1),
                "Semana": timedelta(weeks=1)
            }
            tempoEmprestimo = self.calculaTempoTotalEmprestimo(nomeCliente)
            modalidade = self.pegaModalidade(nomeCliente)
            periodos = math.ceil(tempoEmprestimo / tempoDoPeriodo(modalidade))
            print(f"Loja: {nomeCliente} emprestou bicicleta(s) na modalidade {modalidade} por {periodos} {modalidade}(s).")

            return periodos
        
        except TypeError as error:
            print(f"Loja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"Loja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except:
            print(f"Loja: Não foi possível obter a quantidade de periodos do empréstimo em nome de {nomeCliente}. Motivo: desconhecido")
            return 0

    def calculaTempoTotalEmprestimo(self, nomeCliente):
        '''
        Recebe uma string nomeCliente. 
        Devolve o "timedelta" diferença de tempo entre a retirada e a devolução das bicicletas se o cálculo da diferença for efetuado.
        Devolve 0 em caso contrário.
        '''
        try:
            if not isinstance(nomeCliente, str):
                raise TypeError("tipo de parâmetro inválido.")
            
            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            retirada = self.emprestimos[nomeCliente]["retirada"]
            devolucao = self.emprestimos[nomeCliente]["devolucao"]
            tempoTotalDoEmprestimo = devolucao - retirada

            print(f"Loja: {nomeCliente} emprestou bicicleta(s) por {tempoTotalDoEmprestimo}.")

            return tempoTotalDoEmprestimo

        except TypeError as error:
            print(f"Loja: Não foi possível obter o tempo total do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except SystemError as error:
            print(f"Loja: Não foi possível obter o tempo total do empréstimo em nome de {nomeCliente}. Motivo {error}.")
            return 0

        except:
            print(f"Loja: Não foi possível obter ao tempo total do empréstimo em nome de {nomeCliente}. Motivo: desconhecido")
            return 0

    def recebePagamento(self, nomeCliente, valorPago):
        '''
        Recebe uma string nomeCliente e um float valorPago.
        Devolve 0 se o valor do empréstimo for liquidado e -1 em caso contrário.
        '''
        try:
            if not (isinstance(nomeCliente, str) and isinstance(valorPago, float)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if valorPago < 0:
                raise ValueError("valor de pagamento inválido.")

            if nomeCliente not in self.emprestimos:
                raise SystemError("cliente não possui empréstimo em seu nome.")

            valorDevido = self.emprestimos[nomeCliente]["valor"]
            if valorPago < valorDevido:
                raise SystemError("valor de pagamento menor do que o devido.")

            print(f"Loja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta de R$ {valorDevido} em nome de {nomeCliente} efetuado com sucesso. Caixa {self.caixa}")
            self.caixa += valorPago
            if valorPago > valorDevido:
                troco = valorPago - valorDevido
                self.caixa -= troco

            return 0

        except TypeError as error:
            print(f"Loja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}")
            return -1

        except ValueError as error:
            print(f"Loja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}")
            return -1

        except SystemError as error:
            print(f"Loja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: {error}")
            return -1

        except:
            print(f"Loja: recebimento na loja {self.nome} do valor de R$ {valorPago} como pagamento da conta em nome de {nomeCliente} não efetuado. Caixa {self.caixa}. Motivo: desconhecido.")
            return -1

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
