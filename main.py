from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada


cliente = Cliente("Allysson", "Céu")
item_1 = Item("Bíblia", 100)
item_2 = Item("Assinatura SOLYD", 1360)
itens = [item_1, item_2]

pedido_retirada = PedidoRetirada(cliente, itens)
print(f"Preço total: {pedido_retirada.calcular_total():.2f}")
