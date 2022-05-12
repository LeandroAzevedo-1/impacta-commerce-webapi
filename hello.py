from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>Hello word</p>"

@app.route("/products")
def products():
    response = jsonify([
        {
           "title": "Caneca Personalizada de Porcelana do Backend",
           "amount": 123.45,
           "installments": { "number": 3, "total": 41.15, "hasFee": True}
       },
       {
           "title": "Caneca de Tulipa",
           "amount": 123.45,
           "installments": { "number": 3, "total": 41.15}
       }
    ])
        # Desabilitar requisição de segurança para rodar o app 
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response