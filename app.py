from flask import Flask


# __name__ = "__main__"            Quando for feito de forma manual
app = Flask(__name__)

# Criando a rota para enviar os dados
@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/about")
def about():
    return "Página sobre!"


if __name__ == "__main__":
    app.run(debug=True)
