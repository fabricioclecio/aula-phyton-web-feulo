from flask import Flask, render_template

app = Flask("meu app")

# criado mooc para simular o banco de dados.
posts = [
    {
    'titulo' : "Minha primeira postagem",
    'texto' : "teste"
    },

    {
    'titulo' : "Minha segunda postagem",
    'texto' : "outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens.
    return render_template('exibir_entradas.html', entradas=entradas)

#@app.route('/novo')
#def novo():
#    return "Hello Mundo novo !!"  



