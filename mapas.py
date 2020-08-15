#toda funcion que no tenga un valor de regreso regresa un none
#parametros opcionales
#funcion que permita calcular una serie de fivonacci
def funcion(uno = 'juan'):
    return f'hola  {uno}'
def funcion2(a,b):
    return a+b

var = funcion('braulio')
var2 = funcion()
print(var)
print(var2)
print(funcion2(1.2,1.6))


