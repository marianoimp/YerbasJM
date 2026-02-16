from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)



@app.route('/')
def home():
    info_pagina={
        "titulo":"YERBASJM",
        "descripcion":"Hola somos una empresa encargada en la venta de artículos provenientes del país.Podés mirar nuestros productos apretando el botón.",
        "productos":"Nuestros Productos"
                 }
    return render_template('index.html', info=info_pagina)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run("localhost", port=8083, debug=True)