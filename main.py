from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus
from pagamento.pagamento_factory import PagamentoFactory
from pedido.pedido_delirevy import PedidoDelivery
from cliente import Cliente
from item import Item


MENSAGEM_PAGO = "O pagamento foi confirmado!"
MENSAGEM_PREPARANDO = "O pedido está sendo processao!"
MENSAGEM_ENVIADO = "O pedido saiu para a entrega!"


cliente = Cliente("Allysson", "Céu")

item_1 = Item("Livro 'Black Hat Python - 2° Edição'", 83)
item_2 = Item("Revival Five", 0)

itens = [item_1, item_2]

taxa_entrega = 5
pedido = PedidoDelivery(cliente, itens, taxa_entrega)

tipo_pagamento = "pix"
valor_pedido = pedido.calcular_total()
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

pedido.status = "Pedido confirmado!"
notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, pedido.status)

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
