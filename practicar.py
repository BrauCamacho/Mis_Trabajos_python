import os
class Persona:
     def __init__(self):
         pass
class Alumno(Persona):
    def __init__(self, NUA, Nombre, CURP):
        self.Nombre = Nombre
        self.CURP = CURP
        self.NUA = NUA
    def __str__(self):
        return f'NUA: {self.NUA} \nNombre:  {self.Nombre},\nCURP: {self.CURP}' 
class Profesor(Persona):
    def __init__(self, NUE, Nombre, CURP):
        self.Nombre = Nombre
        self.CURP = CURP
        self.NUE = NUE
    def __str__(self):
        return f'NUE: {self.NUE} \nNombre:  {self.Nombre},\nCURP: {self.CURP}' 
if __name__ =="__main__":
     acc = -1
     lista = []
     while(acc != 4):
            acc = int(input("1.- Insertar \n 2.- Modificar \n 3.- Eliminar \n 4.- salir \n 5.- ver"))
            if acc ==1:
                os.system('cls')
                c = int(input("1.- Alumno \n 2.- Profesor \n 3.- cancelar"))
                if c == 1:
                   os.system('cls')
                   NUA = int(input("Introducir NUA: "))
                   Nombre = input("Introducir el Nombre: ")
                   CURP = int(input("Introducir el CURP: "))
                   persona = Alumno(NUA, Nombre, CURP)
                   lista.append(persona)
                elif c==2:
                   os.system('cls')
                   NUE = int(input("Introducir NUE: "))
                   Nombre = input("Introducir el Nombre: ")
                   CURP = int(input("Introducir el CURP: "))
                   persona = Profesor(NUE, Nombre, CURP)
                   lista.append(persona)
                elif c ==3:
                    os.system('cls')
                    print("cancelar")
                    pass
            elif acc ==2:
                pass
            elif acc == 3:
                pass
            elif acc == 4:
                pass
            elif acc == 5:
                for i in lista:
                    print(i)
