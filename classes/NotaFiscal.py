class NotaFiscal:
    def __init__(self):
        self.id = None
        self.itens = None
        self.valoresIndividuais = None
        self.valorTotal = None
        pass

    def nova_nota_fiscal(self, itens, valoresIndividuais, valorTotal):
        self.itens = itens
        self.valoresIndividuais = valoresIndividuais
        self.valorTotal = valorTotal
        return self