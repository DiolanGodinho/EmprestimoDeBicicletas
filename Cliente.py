from Loja import Loja

class Cliente(object):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.quantidadeBicicletas = 0
        self.saldo = 0.0

    def solicitaEmprestimo(self, loja, quantidade, modalidade):
        try:
            if not (isinstance(loja, Loja) and isinstance(quantidade, int) and isinstance(modalidade, str)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0:
                raise ValueError("quantidade de bicicletas inválida.")

            if modalidade not in ["Hora", "Dia", "Semana"]:
                raise SystemError("modalidade inválida.")

            self.quantidadeBicicletas += quantidade
            self.saldo = loja.recebePedido(self.nome, quantidade, modalidade)
            print(f"Cliente: {self.nome} solicita {quantidade} bicicletas na modalidade {modalidade}. Saldo R${self.saldo}. Bicicletas {self.quantidadeBicicletas}.")

        except TypeError as error:
            print(f"Cliente: {self.nome} solicitação de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Motivo: {error}. Saldo R${self.saldo}. Bicicletas {self.quantidadeBicicletas}.")

        except ValueError as error:
            print(f"Cliente: {self.nome} solicitação de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Motivo: {error}. Saldo R${self.saldo}. Bicicletas {self.quantidadeBicicletas}.")

        except SystemError as error:
            print(f"Cliente: {self.nome} solicitação de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Motivo: {error}. Saldo R${self.saldo}. Bicicletas {self.quantidadeBicicletas}.")

        except:
            print(f"Cliente: {self.nome} solicitação de {quantidade} bicicletas na modalidade {modalidade} não efetuada. Motivo: desconhecido. Saldo R${self.saldo}. Bicicletas {self.quantidadeBicicletas}.")

        finally:
            return self.quantidadeBicicletas, self.saldo

    def devolveBicicletas(self, quantidade, loja):
        try:
            if not (isinstance(loja, Loja) and isinstance(quantidade, int)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if quantidade <= 0 or quantidade > self.quantidadeBicicletas:
                raise ValueError("quantidade de bicicletas inválida.")

            self.quantidadeBicicletas -= quantidade
            loja.recebeBicicletas(self.nome, quantidade)
            print(f"Cliente: {self.nome} devolução de {quantidade} bicicletas na loja {loja.nome}. Saldo R${self.saldo}.")
        
        except TypeError as error:
            print(f"Cliente: {self.nome} devolução de {quantidade} bicicletas na loja {loja.nome} não concluída. Motivo: {error}.")

        except ValueError as error:
            print(f"Cliente: {self.nome} devolução de {quantidade} bicicletas na loja {loja.nome} não concluída. Motivo: {error}.")

        except:
            print(f"Cliente: {self.nome} devolução de {quantidade} bicicletas na loja {loja.nome} não concluída. Motivo: desconhecido")

        finally:        
            return self.quantidadeBicicletas

    def pagaEmprestimo(self, valorDesembolsado, loja):
        try:
            if not (isinstance(loja, Loja) and isinstance(valorDesembolsado, float)):
                raise TypeError("tipos de parâmetros inválidos.")
            
            if valorDesembolsado < self.saldo:
                raise ValueError("valor desembolsado menor do que o devido.")

            loja.recebePagamento(valorDesembolsado)
            self.saldo = 0
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome}.")
        
        except TypeError as error:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado.Motivo: {error}.")

        except ValueError as error:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: {error}.")

        except:
            print(f"Cliente: {self.nome} pagamento de {self.saldo} com {valorDesembolsado} na loja {loja.nome} não efetuado. Motivo: desconhecido.")

        finally:
            return self.saldo    
        