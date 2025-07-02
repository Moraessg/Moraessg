class ObservadorStatus:
    def __init__(self, notificacoes):
        self.notificacoes = notificacoes

    def atualizar(self, pedido):
        mensagem = f"Status do pedido atualizado para: {pedido.status}"
        self.notificacoes.enviar_notificacoes(pedido.cliente, mensagem)