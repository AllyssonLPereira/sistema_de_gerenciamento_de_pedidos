from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delirevy import PedidoDelivery
from cliente import Cliente
from item import Item


cliente = Cliente("Allysson", "Céu")

item_1 = Item("Bíblia", 100)
item_2 = Item("Assinatura SOLYD", 1360)
item_3 = Item("Livro 'Black Hat Python - 2° Edição'", 83)
item_4 = Item("Revival Five", 0)

itens_retirado = [item_1, item_2]
itens_delirevy = [item_3, item_4]

pedido_retirada = PedidoRetirada(cliente, itens_retirado)
pedido_delivery = PedidoDelivery(cliente, itens_delirevy, 5)

print(f"Preço total - retirados: {pedido_retirada.calcular_total():.2f}")
print(f"Preço total - delivery: {pedido_delivery.calcular_total():.2f}")
