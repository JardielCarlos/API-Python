from flask import Flask, request

filmes = [
    {'nome':'Harry Potter', 'descricao':'filme sobre uma escola de bruxaria', 'id': "0"},
    {'nome':'Velozes e Furiosos', 'descricao':'Filme de acao com corrida ', 'id': "1"},  #Sem caracteres especiais para não bugar o browser
    {'nome':'Homem-Aranha', 'descricao':'Historia de um super heroi', 'id': "2"}
]

app = Flask(__name__)

#Página inicil.
@app.route("/")
def home():
    return "<h1>Página Inicial de filmes</h1>"

    #Mostra a lista de filmes.
@app.route("/filmes", methods=["GET"])
def get():
    return {'filmes': filmes}

#Coloca um novo filme na lista de filmes.
@app.route("/novo_filme", methods=["POST"])
def post():
    body = request.json

    tamanho = len(filmes)

    if ("descricao" not in body):
        return {"status": 400, "mensagem": "O paramentro descrição é obrigatorio"}

    if ("id" not in body):
        return {"status": 400, "mensagem": "O paramentro id é obrigatorio"}

    if ("nome" not in body):
        return {"status": 400, "mensagem": "O paramentro nome é obrigatorio"}

    filmes.insert(tamanho + 1, {"id": f'{body["id"]}', "nome": f'{body["nome"]}', 'descricao': f'{body["descricao"]}'})

    return {'filmes': filmes}


        #Atualizar algum filme
@app.route("/atualizar_filme", methods=["PATCH"])
def path():
    body = request.json
    int(body["id"])                      #ATENÇÃO NECESSARIO USAR O ID PARA ENCONTRAR O FILME
    try:
        filmes[int(body["id"])]["nome"] = body["nome"]

    except:
        filmes[int(body["id"])]["descricao"] = body["descricao"]

    else:
        filmes[int(body["id"])]["nome"] = body["nome"]
        filmes[int(body["id"])]["descricao"] = body["descricao"]

    return {'filmes': filmes}


        #Deletar filme
@app.route("/deletar_filme", methods=["DELETE"])
def delete():
    body = request.json

    for c in filmes:
        if c['nome'] == body["nome"]:
            filmes.pop(filmes.index(c))

    return {'filmes': filmes}


if __name__ == "__main__":
    app.run(debug=True)
