#parametros de lista
def sumar (*arg):
    suma =0
    for item in arg:
        suma += item
    return suma
def introducir(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])
if __name__ == "__main__":
     print(sumar(10,30,50,70,90, 100))
     introducir(nombre = "braulio", apellido ="pedro", a =10, b = 40)
