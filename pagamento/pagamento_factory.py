from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX

class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "pix":
            return PagamentoPIX()
        elif tipo == "cartão":
            return PagamentoCartao
        else:
            raise ValueError(f"Tipo de pagamento '{tipo}' não suportado")