from Loja import Loja

class Cliente(object):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.quantidadeBicicletas = 0
        self.saldo = 0

    def solicitaEmprestimo(self, loja, quantidade, modalidade):
        '''Recebe uma instancia de Loja loja, um inteiro quantidade e uma string modalidade. Devolve a quantidade de bicicletas emprestadas em nome do cliente. Se houver erros devolve 0.'''
        try:
            if not (isinstance(loja, Loja) and isinstance(quantidade, int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida.")

            if modalidade not in ["Hora", "Dia", "Semana"]:
                raise SystemError("modalidade inválida.")

            loja.recebePedido(self.nome, quantidade, modalidade)
            self.quantidadeBicicletas = quantidade
            print(f"Cliente: solicitação de {self.nome} de {quantidade} bicicleta(s) na modalidade {modalidade} efetuada com sucesso. Bicicletas {self.quantidadeBicicletas}.")
            
            return self.quantidadeBicicletas

        except TypeError as error:
            print(f"Cliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}")
            return 0

        except ValueError as error:
            print(f"Cliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}")
            return 0

        except SystemError as error:
            print(f"Cliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}")
            return 0

        except:
            print(f"Cliente: solicitação de {self.nome} de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Bicicletas {self.quantidadeBicicletas}. Motivo: desconhecido.")
            return 0

    def devolveBicicletas(self, quantidade, loja):
        '''Recebe um inteiro quantidade e uma instancia de Loja loja. Devolve o valor total devido pelo emprestimo. Se houver erros devolve 0.'''
        try:
            if not (isinstance(loja, Loja) and isinstance(quantidade, int)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0 or quantidade > self.quantidadeBicicletas:
                raise ValueError("quantidade de bicicletas inválida.")

            self.quantidadeBicicletas = 0
            loja.recebeBicicletas(self.nome, quantidade)
            self.saldo = loja.calculaValorEmprestimo(self.nome)
            print(f"Cliente: devolução de {quantidade} bicicletas em nome de {self.nome} na loja {loja.nome} efetuada com sucesso. Valor do emprestimo R$ {self.saldo}. Bicicletas {self.quantidadeBicicletas}.")
       
            return self.saldo
        
        except TypeError as error:
            print(f"Cliente: devolução de {quantidade} bicicletas em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}")
            return 0

        except ValueError as error:
            print(f"Cliente: devolução de {quantidade} bicicletas em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Motivo: {error}")
            return 0

        except:
            print(f"Cliente: devolução de {quantidade} bicicletas em nome de {self.nome} na loja {loja.nome} não concluída. Bicicletas {self.quantidadeBicicletas}. Motivo: desconhecido.")
            return 0

    def pagaEmprestimo(self, valorDesembolsado, loja):
        '''Recebe um float valorDesembolsado e uma instancia de Loja loja. Devolve o valor devido  (deve ser igual a zero). Se houver erros devolve -1.'''
        try:
            if not (isinstance(loja, Loja) and isinstance(valorDesembolsado, float)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if valorDesembolsado < self.saldo:
                raise ValueError("valor desembolsado menor do que o devido.")

            loja.recebePagamento(self.nome, valorDesembolsado)
            self.saldo = 0
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome}.")
        
            return self.saldo    

        except TypeError as error:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: {error}")
            return -1

        except ValueError as error:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: {error}")
            return -1

        except:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: desconhecido.")
            return -1
