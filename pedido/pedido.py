from abc import ABC, abstractclassmethod

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

    @abstractclassmethod
    def calcular_total(self):
        pass