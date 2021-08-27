from datetime import datetime, timedelta, timezone

class Emprestimo(object):
    HORARIO_BRASILIA = timezone(timedelta(hours=-3))

    def __init__(self, nomeCliente, nomeloja, quantidade, modalidade) -> None:
        try:
            if not (isinstance(nomeCliente, str) and isinstance(nomeloja, str)):
                raise TypeError("tipos dos parametros 'nomes' incorretos")
            
            if not isinstance(modalidade, str):
                raise TypeError("tipo do parametro 'modalidade' incorreto")

            if not isinstance(int(quantidade), str):
                raise TypeError("tipos do parametro 'quantidade' incorreto")

            print(f"\nEmprestimo: instanciando a classe com o cliente {nomeCliente} emprestando na loja '{nomeloja}' {quantidade} biciclet(s) na modalidade '{modalidade}'.")

            self.nome = nomeCliente
            self.loja = nomeloja    # Loja de retirada das bicicletas
            self.quantidade = quantidade
            self.modalidade = modalidade
            self.retirada = datetime.now().astimezone(self.HORARIO_BRASILIA)
            self.devolucao = self.retirada
            self.valor = 0.0

        except TypeError as error:
            print(f"\nEmprestimo: classe com o cliente {nomeCliente} emprestando na loja '{nomeloja}' {quantidade} biciclet(s) na modalidade '{modalidade}' nao instanciada. Motivo: {error}.")

        except:
            print(f"\nEmprestimo: classe com o cliente {nomeCliente} emprestando na loja '{nomeloja}' {quantidade} biciclet(s) na modalidade '{modalidade}' nao instanciada. Motivo: desconhecido.")
        