from datetime import datetime, timedelta, timezone

class Emprestimo(object):
    HORARIO_BRASILIA = timezone(timedelta(hours=-3))

    def __init__(self, nomeCliente, nomeloja, quantidade, modalidade) -> None:
        self.nome = nomeCliente
        self.loja = nomeloja    # Loja de retirada das bicicletas
        self.quantidade = quantidade
        self.modalidade = modalidade
        self.retirada = datetime.now().astimezone(self.HORARIO_BRASILIA)
        self.devolucao = self.retirada
        self.valor = 0.0    
        