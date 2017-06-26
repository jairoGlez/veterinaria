from flask import Flask, jsonify
from veterinaria import Veterinaria

app = Flask("bd")
vet = Veterinaria()

@app.route("/")
def raiz():
    return("Servidor Veterinaria")

@app.route("/dueños")
def dueños():
    dueños = vet.mostrarDueños()
    print(dueños)
    respuesta = jsonify(dueños)
    return respuesta

app.run()
