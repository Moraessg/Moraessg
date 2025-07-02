from abc import ABC, abstractclassmethod

class Pagamento (ABC):
    @abstractclassmethod
    def processar (self, valor):
        pass