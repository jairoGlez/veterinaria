from flask import Flask, jsonify, request
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
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

@app.route("/agregarDueño", methods=["POST"])
def agregarDueño():
    print(request.form)
    correo = request.form['correo']
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']
    colonia = request.form['colonia']
    domicilio = request.form['domicilio']
    telefono = request.form['telefono']
    contraseña = request.form['contraseña']
    foto = request.form['foto']

    vet.insertarDueño([correo,nombre,apellido1,apellido2,colonia,domicilio,telefono,contraseña,foto])
    respuesta = jsonify({"status":"Ok"})
    respuesta.headers.add('Access-Control-Allow-Origin', '*')

    return respuesta

app.run()
