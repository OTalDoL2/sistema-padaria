from flask import Flask, render_template, redirect
import pymysql


app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='password', database='sistema_padaria')

@app.route('/', methods=['GET', 'POST'])
def index():

    cursor = db.cursor()
    query = 'select * from produtos'
    cursor.execute(query)
    db.commit()
    products = cursor.fetchall()
    return render_template('index.html', produtos=products)

if __name__ == "__main__":
    app.run(debug=True)

