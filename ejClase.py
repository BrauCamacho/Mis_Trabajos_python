#desarrollar un programa en python que permita capturar alumnos (nua, nombre, Calificacion, generar lista de alimnos e imprimir alumno con mayor calificacion)
Alumnos = []
iter = 0
while(iter < 1):
    print("0 .- para capturar alumno")
    print("1.- para salir")
    iter = int(input())
    if iter == 0:
        alumno = {}
        alumno['NUA'] = input("inserte un NUA : ")
        alumno['Nombre'] = input("inserte un Nombre : ")
        alumno['Calificacion'] = float(input("inserte una calificacion : "))
        Alumnos.append(alumno)
mayor = Alumnos[0]['Calificacion']
alum = {}
for i in Alumnos:
      if i['Calificacion'] > mayor:
          mayor = i['Calificacion']
          alum = i
print(alum)
# enumerate
#for i, alumno in enumerate(Alumnos):
