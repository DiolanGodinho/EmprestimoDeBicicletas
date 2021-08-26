from Loja import Loja

class Cliente(object):
    MODALIDADES_DISPONIVEIS = ["Hora", "Dia", "Semana"]

    def __init__(self, nome) -> None:
        self.nome = nome
        self.quantidadeBicicletas = 0
        self.saldo = 0

    def solicitaEmprestimo(self, loja, quantidade, modalidade):
        '''
        Recebe uma instancia de Loja loja, um inteiro quantidade e uma string modalidade. Devolve a quantidade de bicicletas emprestadas em nome do cliente. Se houver erros devolve 0.
        '''
        try:
            if not (isinstance(loja, Loja) and isinstance(int(quantidade), int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida")

            if modalidade not in self.MODALIDADES_DISPONIVEIS:
                raise SystemError("modalidade inválida.")

            print(f"\nCliente: solicitação de {self.nome} de {quantidade} bicicleta(s) na modalidade {modalidade} efetuada com sucesso. Bicicletas {self.quantidadeBicicletas}.")

            pedidoAceito = loja.recebePedido(self.nome, quantidade, modalidade)
            if pedidoAceito:
                self.quantidadeBicicletas = loja.emprestaBicicletas(self.nome, quantidade, modalidade)
                # Aqui não usamos += pois estamos admitindo que o cliente pode ter apenas um    empréstimo em seu nome.
            
            return self.quantidadeBicicletas

        except TypeError as error:
            print(f"\nCliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}.")
            return 0

        except ValueError as error:
            print(f"\nCliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}.")
            return 0

        except SystemError as error:
            print(f"\nCliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}.")
            return 0

        except:
            print(f"\nCliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: desconhecido.")
            return 0

    def devolveBicicletas(self, loja):
        '''
        Recebe uma instancia de Loja loja. Devolve o valor total devido pelo emprestimo. Se houver erros devolve 0.
        '''
        try:
            if not isinstance(loja, Loja):
                raise TypeError("tipos de parâmetros inválidos")
            
            if self.nome not in loja.emprestimos:
                raise SystemError("loja de devolucao diferente da loja de retirada")

            self.quantidadeBicicletas -= loja.recebeBicicletas(self.nome)
            self.saldo = loja.emprestimos[self.nome].valor

            print(f"\nCliente: devolução da(s) bicicleta(s) em nome de {self.nome} na loja {loja.nome} efetuada com sucesso. Valor do emprestimo R$ {self.saldo}. Bicicletas {self.quantidadeBicicletas}.")
       
            return self.saldo
        
        except TypeError as error:
            print(f"\nCliente: devolução da(s) bicicleta(s) em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Valor do emprestimo R$ {self.saldo}. Motivo: {error}.")
            return 0

        except ValueError as error:
            print(f"\nCliente: devolução da(s) bicicleta(s) em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Valor do emprestimo R$ {self.saldo}. Motivo: {error}.")
            return 0

        except ValueError as error:
            print(f"\nCliente: devolução da(s) bicicleta(s) em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Valor do emprestimo R$ {self.saldo}. Motivo: {error}.")
            return 0

        except:
            print(f"\nCliente: devolução da(s) bicicleta(s) em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Valor do emprestimo R$ {self.saldo}. Motivo: desconhecido.")
            return 0

    def pagaEmprestimo(self, valorDesembolsado, loja):
        '''
        Recebe um float valorDesembolsado e uma instancia de Loja loja. Devolve o valor devido (deve ser igual a zero) pelo empréstimo se o pagamento for efetuado. Caso contrário, devolve -1.
        '''
        try:
            if not (isinstance(loja, Loja) and isinstance(float(valorDesembolsado), float)):
                raise TypeError("tipos de parâmetros inválidos")
            
            if valorDesembolsado < self.saldo:
                raise ValueError("valor desembolsado menor do que o devido")
            
            print(f"\nCliente: pagamento do cliente {self.nome} de R$ {self.saldo} com R$ {valorDesembolsado} na loja {loja.nome}.")

            self.saldo -= loja.recebePagamento(self.nome, valorDesembolsado)
        
            return self.saldo    

        except TypeError as error:
            print(f"\nCliente: pagamento do cliente {self.nome} de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: {error}.")
            return -1

        except ValueError as error:
            print(f"\nCliente: pagamento do cliente {self.nome} de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: {error}.")
            return -1

        except:
            print(f"\nCliente: pagamento do cliente {self.nome} de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: desconhecido.")
            return -1
