import sqlite3

db = sqlite3.connect("veterinaria.db")
c = db.cursor()

def mostrarDueños():
    f = c.execute("SELECT * FROM dueño")
    f = f.fetchall()

    for fila in f:
        print(fila)

def insertarDueño(datos):
    c.execute("INSERT INTO dueño (eMail,nombre,apellido1,apellido2,colonia,domicilio,telefono,contraseña,foto) VALUES (?,?,?,?,?,?,?,?,?)",
    (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]))
    db.commit()

insertarDueño(["juan@gmail.com","juan","lopez","duran","centro","roble #8","3378995423","passwooord","img78.jpg"])
mostrarDueños()
