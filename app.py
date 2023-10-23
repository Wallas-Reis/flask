from flask import Flask, render_template
from bd import select

app = Flask(__name__)

@app.route('/')
def index():
    result = select("select coluna2 from tabela")
    
    # Extrair o valor Decimal da tupla
    value = result[0][0] if result and result[0] else None
    
    return render_template('index.html', variavel=value)

if __name__ == '__main__':
    app.run(debug=True)