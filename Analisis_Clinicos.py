#ver si las persionas tienen diabetes
#diabetes glucosa >120
#trigliceridos altos >180
# colesterol alto  > 200
def Eliminar(Personas):
    Buscar = float(input("inserte un INE valido: "))
    c = -1
    t =0
    for i in Personas:
        if i['INE'] == Buscar:
            c = t
        t+=1
    if c != -1:
        print("Registro Encontrado y eliminado ")
        Personas.pop(c)
    else:
        print("registro no encontrado")
    return Personas
def Agregar():
    persona = {}
    persona['Sexo'] = input("inserte sexo (M para mujer y H para hombre) : ")
    persona['Nombre'] = input("inserte un Nombre : ")
    persona['INE'] = float(input("inserte un INE : "))
    persona['Glucosa'] = float(input("inserte los niveles de Glucosa : "))
    persona['Colesterol'] = float(input("inserte los niveles de Colesterol : "))
    persona['Trigliceridos'] = float(input("inserte el número de Trigliceridos : "))
    return persona
def Editar(personas):
    Buscar = float(input("inserte un INE valido: "))
    c = -1
    t =0
    for i in personas:
        if i['INE'] == Buscar:
            c = t
        t+=1
    if c != -1:
        print("registro encontrado")
        print("1 .- nombre")
        print("2 .- Sexo")
        print("3 .- INE")
        print("4 .- Glucosa")
        print("5 .- Colesterol")
        print("6 .- Trigliceridos")
        campo = int(input("inserte cual campo desea editar"))
        if campo == 1:
            personas[c]['Nombre'] =input("inserte un Nombre : ")
        elif campo == 2:
            personas[c]['Sexo'] = input("inserte sexo (M para mujer y H para hombre) : ")
        elif campo == 3:
            personas[c]['INE'] = float(input("inserte un INE : "))
        elif campo == 4:
            personas[c]['Glucosa'] = float(input("inserte los niveles de Glucosa : "))
        elif campo == 5:
            personas[c]['Colesterol'] = float(input("inserte los niveles de Colesterol : "))
        elif campo == 6:
            personas[c]['Trigliceridos'] = float(input("inserte el número de Trigliceridos : "))
        else:
            print('campo no existente')

    else:
        print("Registro no encontrado")   
    return personas 

Personas = []
iter = 0
while(iter < 4):
    print("0 .- para capturar persona")
    print("1 .- para editar  los datos de una persona ")
    print("2.- para eliminar los datos de una persona ")
    print("3.- para ver los registros")
    print("4 .- para salir")
    iter = int(input())
    if iter == 0:
        persona = Agregar()
        Personas.append(persona)
    elif iter == 1:
        Personas = Editar(Personas)
    elif iter == 2:
        Personas = Eliminar(Personas)
    elif iter == 3:
        print(Personas)
    elif iter == 4:
        print("saliendo...")
print("personas con Diabetes")
for i in Personas:
    if i['Glucosa'] > 120:
        print(i)
print("personas con Colesterol alto")
for i in Personas:
    if i['Colesterol'] > 180:
        print(i)
print("personas con trigliceridos altos")
for i in Personas:
    if i['Trigliceridos'] > 200:
        print(i)





         
        