from cliente import Cliente
from item import Item


cliente = Cliente("Allysson", "Céu")
item = Item("Bíblia", "100")


print(f"Cliente: {cliente.nome}\nEndereço: {cliente.endereco}")
print(f"Item: {item.nome}\nValor: R${item.preco}")
