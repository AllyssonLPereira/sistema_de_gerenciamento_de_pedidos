from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPix


class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "pix":
            return PagamentoPix()
        elif tipo == "cartao":
            return PagamentoCartao()
        else:
            raise ValueError(f"Esse tipo de pagamento - {tipo} - não é suportado!")
