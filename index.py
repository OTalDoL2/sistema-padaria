from flask import Flask, render_template, redirect, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', user='root', password='password', database='sistema_padaria')

lista_de_compras = []
valor_total_compra = 0


def atualiza_estoque():
    global lista_de_compras, valor_total_compra
    
    cursor = db.cursor()
    print("a lista: ")
    print(lista_de_compras)
    for item in lista_de_compras:
        sql = 'UPDATE produtos SET estoque = estoque - %s WHERE nome = %s'
        cursor.execute(sql, ( item['quantidade'], item['nomeItem']))
        db.commit()
    lista_de_compras.clear()


@app.route('/deletar', methods=['GET', 'POST'])
def deletar(): 
    global lista_de_compras

    lista_de_compras.clear()
    id = request.args.get('id')
    # print(lista_de_compras)

    for i in range(len(lista_de_compras)):
        print(f"{lista_de_compras[i]['id']} == {id}")
        if int(lista_de_compras[i]['id']) != int(id):
            lista_de_compras.append(lista_de_compras[i])
    return redirect('/')



@app.route('/realizar-compra', methods=['GET'])
def finaliza_compra():
    atualiza_estoque()
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    global lista_de_compras, valor_total_compra

    if request.method == 'GET':
        cursor = db.cursor()
        query = 'select * from produtos'
        cursor.execute(query)
        db.commit()
        products = cursor.fetchall()
        print(lista_de_compras)
        return render_template('index.html', produtos=products, valor_compra=valor_total_compra, lista=lista_de_compras)

    else:
        # cursor = db.cursor()
        # query = 'select * from produtos'
        # cursor.execute(query)
        # db.commit()
        # products = cursor.fetchall()
        # return render_template('index.html', produtos=products, lista=lista_de_compras)
        
        id = request.form.get('idItem')
        quantidade = request.form.get('idQtd')
        cursor = db.cursor()

        sql = 'SELECT * FROM produtos WHERE id = %s and estoque > %s'
        cursor.execute(sql, (id, quantidade))
        db.commit()
        lista = cursor.fetchall()[0]
        item_lista = {"id": lista[0],"nomeItem": lista[1], "quantidade": quantidade, "valor_unidade": float(lista[4]), "valor_total": float(lista[4]) * float(quantidade) }
        lista_de_compras.append(item_lista)
        valor_total_compra += float(lista[4]) * float(quantidade)
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

