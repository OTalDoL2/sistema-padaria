import pymysql


class BancoDados:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='password', database='sistema_padaria')
        pass

    def verifica_cliente_existente(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cliente WHERE id = %s OR documento = %s;"
        cursor.execute(sql, (id, id))
        cliente = cursor.fetchone()
        return cliente
    
    def atualizar_cliente(self, cliente):
        cursor = self.db.cursor()
        sql = 'UPDATE cliente SET nome = %s, documento = %s, idade = %s, pontos = %s WHERE id = %s'
        cursor.execute(sql, (cliente.nome, cliente.documento, cliente.idade, cliente.pontos, cliente.id))
        return self.db.commit()
    
    def gera_nota_fiscal(self, nota):
        cursor = self.db.cursor()
        sql = 'INSERT INTO notaFiscal(itens, valoresIndividuais, valorTotal) values (%s,%s,%s)'
        cursor.execute(sql, (str(nota.itens), str(nota.valoresIndividuais), nota.valorTotal))
        id_nota_fiscal = self.db.cursor().execute("SELECT LAST_INSERT_ID()")
        print(f"ID da nota fiscal gerada: {id_nota_fiscal}")

        self.db.commit()
        nota.id = id_nota_fiscal
        return nota

    def registrar_compra(self, id_cliente, id_nota):
        cursor = self.db.cursor()
        sql = 'INSERT INTO historicoCompras(cliente, nota) values (%s,%s)'
        cursor.execute(sql, (id_cliente, id_nota))
        return self.db.commit()
    
    def atualiza_pontos(self, cliente, quantidade_itens_comprados):
        cursor = self.db.cursor()
        sql = 'UPDATE cliente SET pontos = pontos + %s WHERE id = %s'
        cursor.execute(sql, (10 * (quantidade_itens_comprados) , cliente.id))
        self.db.commit()