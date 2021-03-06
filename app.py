from flask import Flask
import os

# Récuperation des ENVs
PORT = os.environ.get("PORT", "80")
HOST = os.environ.get("HOST", "0.0.0.0")

app = Flask(__name__)

@app.route('/')
def hello():
    """Fonction appelé pour le chemin par defaut

    Returns:
        str: un message de la plus grande importance
    """
    return 'Hello, World !'


@app.route('/<name>')
def hello(name):
    return f'Hello, {name} !'

@app.route('/poulet')
def hello(name):
    return 'Hello, poulet!'

if __name__ == "__maim__":
    app.run(host=HOST, port=PORT)