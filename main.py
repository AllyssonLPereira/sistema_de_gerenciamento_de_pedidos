from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delirevy import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from cliente import Cliente
from item import Item


cliente = Cliente("Allysson", "Céu")

item_1 = Item("Bíblia", 100)
item_2 = Item("Assinatura SOLYD", 1360)
item_3 = Item("Livro 'Black Hat Python - 2° Edição'", 83)
item_4 = Item("Revival Five", 0)

itens_retirado = [item_1, item_2]
itens_delivery = [item_3, item_4]

pedido_retirada = PedidoRetirada(cliente, itens_retirado)
pedido_delivery = PedidoDelivery(cliente, itens_delivery, 5)

valor_pedido = pedido_retirada.calcular_total()

tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido)

MENSAGEM = "Seu pedido saiu para entrega!"
notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, MENSAGEM)

pedido_delivery.status = "Pedido confirmado!"
notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, pedido_delivery.status)
