from abc import ABC, abstractclassmethod

class Notificacao(ABC):
    def enviar_notificacao(self, cliente, mensagem):
        pass