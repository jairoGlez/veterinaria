import sqlite3

class Veterinaria:
    db = sqlite3.connect("veterinaria.db")
    c = db.cursor()

    def mostrarDueños(self):
        f = self.c.execute("SELECT * FROM dueño")
        f = f.fetchall()
        lista = []

        for fila in f:
            lista.append(fila)

        return lista

    def insertarDueño(self,datos):
        self.c.execute("INSERT INTO dueño (eMail,nombre,apellido1,apellido2,colonia,domicilio,telefono,contraseña,foto) VALUES (?,?,?,?,?,?,?,?,?)",
        (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]))
        self.db.commit()

    def buscar(self,palabra):
        self.c.execute("SELECT * FROM dueño WHERE eMail LIKE ?",("%"+palabra+"%",))
        lista = []

        for d in self.c:
            dueño = {"correo":d[0],"nombre":d[1],"apellido1":d[2],"apellido2":d[3],"colonia":d[4],"domicilio":d[5],"telefono":d[6],"password":d[7],"foto":d[8]}
            lista.append(dueño)

        return lista
