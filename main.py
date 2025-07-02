from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSMS
from notificacao.notificacao_facade import NotificacaoFacade

cliente = Cliente ("Gabriel", "None")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
itens = [item_um, item_dois]

print (f"Cliente: {cliente.nome}, Endereço: {cliente.endereco}")

print (f"Item 1: {item_um.nome}, Preço: {item_um.preco}")
print (f"Item 2: {item_dois.nome}, Preço: {item_dois.preco}")


pedido_retirada = PedidoRetirada(cliente, itens)
#print (f"Preço do pedido Retirada:{pedido_retirada.calcular_total():.2f} ")

taxa_entrega = 10.0
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)
#print (f"Preço do pedido Delivery: {pedido_delivery.calcular_total():.2f}")


valor_pedido = pedido_delivery.calcular_total()
Pagamento_cartao = PagamentoCartao().processar(valor_pedido)

valor_pedido_pix = pedido_retirada.calcular_total()
pagamento_pix = PagamentoPIX().processar(valor_pedido_pix)


tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido_pix)


MENSAGEM = "Seu pedido saiu para entrega!"
#notificacao_email = NotificacaoEmail().enviar_notificacao(cliente, MENSAGEM)
#notificacao_SMS = NotificacaoSMS().enviar_notificacao(cliente, MENSAGEM)

notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, MENSAGEM)


