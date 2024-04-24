from BancoDados import BancoDados

class Cliente:
    def __init__(self):
        self.id = None
        self.nome = None
        self.documento = None
        self.idade = None
        self.pontos = None
    pass

    def buscar_cliente(self, id_cliente):
        db = BancoDados()
        cliente = db.verifica_cliente_existente(id_cliente)
        
        if not cliente:
            return False
    
        self.id = cliente[0]
        self.nome = cliente[1]
        self.documento = cliente[2]
        self.idade = cliente[3]
        self.pontos = cliente[4]
        
        return self

    def adicionar_pontos(self, quantidade_produtos_comprados, valor_compra):
        pontos_adicionais = 10
        if valor_compra > 100:
            pontos_adicionais = pontos_adicionais + 150
        pontos_adicionais = pontos_adicionais + quantidade_produtos_comprados * 1
        self.pontos = self.pontos + pontos_adicionais

        return self

    def criarCliente(self, id, nome, documento, idade, pontos):
        self.id = id
        self.nome = nome
        self.documento = documento
        self.idade = idade
        self.pontos = pontos
        return self
        
