from veterinaria import Veterinaria

class Menu:
    vet = Veterinaria()
    def __init__(self):
        while True:
            print("1) Mostrar dueños")
            print("2) Agregar dueño")
            print("3) buscar")
            print("0) Salir")
            op = input()

            if op == "1":
                self.mostrar()
            elif op == "2":
                self.capturar()
            elif op == "3":
                self.buscar()
            elif op == "0":
                break

    def mostrar(self):
        usuarios = self.vet.mostrarDueños()
        for u in usuarios:
            print("{0:25} {1:10} {2:15} {3:15} {4:10} {5:15} {6:10} {7:15} {8:10}".format(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8]))

    def capturar(self):
        correo = input("Correo: ")
        nombre = input("Nombre: ")
        apellido1 = input("Apellido paterno: ")
        apellido2 = input("Apellido materno: ")
        colonia = input("Colonia: ")
        domicilio = input("Domicilio: ")
        telefono = input("Telefono: ")
        contraseña = input("Contraseña: ")
        foto = input("Nombre de la foto: ")

        self.vet.insertarDueño([correo,nombre,apellido1,apellido2,colonia,domicilio,telefono,contraseña,foto])

    def buscar(self):
        palabra = input("Correo: ")
        lista = self.vet.buscar(palabra)

        for d in lista:
            print("{0:25} {1:10} {2:15} {3:15} {4:10} {5:15} {6:10} {7:15} {8:10}".format(d["correo"],d["nombre"],d["apellido1"],d["apellido2"],d["colonia"],d["domicilio"],d["telefono"],d["password"],d["foto"]))
