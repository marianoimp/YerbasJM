from flask import Flask, render_template,redirect, url_for, request
import requests
import os

# API_BASE = "http://localhost:5053"
app = Flask(__name__)

def obtener_categorias():
    response = requests.get("http://localhost:5053/categorias")
    if response.status_code == 200:
        return response.json()
    return[]

d_productos = {"termos":"Termos elegantes y duraderos para mantener tus bebidas a la temperatura ideal",
             "mates":""}


@app.route('/')
def home():
    info_pagina={
        "titulo":"YERBASJM",
        "descripcion":"Hola somos una empresa encargada en la venta de artículos provenientes del país.Podés mirar nuestros productos apretando el botón.",
        "productos":"Nuestros Productos"
                 }
    
    nuestros_productos = obtener_categorias()
    return render_template('index.html', info=info_pagina, categorias=nuestros_productos, des_productos=d_productos)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run("localhost", port=8083, debug=True)