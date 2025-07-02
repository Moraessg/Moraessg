from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus

cliente = Cliente ("Gabriel", "None")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
itens = [item_um, item_dois]

taxa_entrega = 10.0
pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

pedido.status = "Pedido confirmado!"
notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, pedido.status)

MENSAGEM_PAGO = "O Pagamento foi confirmado"
MENSAGEM_PREPARANDO = "O Pedido está sendo preparado!"
MENSAGEM_ENVIADO = "O pedido saiu para entrega!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus (notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO