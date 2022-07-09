#funciones def es definir, creas una funcion, creas la variable nombre por ejemplo, aplicas el return con lo que quieres que salga, creas la variable resultado e imprimes resultado
def yoFuncion():
    nombre = "Aaron"
    return "Hola " + nombre + "!"

resultado = yoFuncion()
print(resultado)

#Este es un ejemplo de como poner 2 numeros para sumarlos o restarlos si ndefino a y b lo puedo poner dentro de mi funcion para que haga la oepracion, sino, solo meter los digitos como 15, 50 ya que serian los numeros 1 y 2 de los parametros de la funcion de arriba (numero1, numero2)
def laOperacion(numero1, numero2):
    return numero1 - numero2
a = 50
b = 40
resalta = laOperacion(4930, 84927)
print(resalta)


#Arrays primero haces una varibale como miLista, siempre recordar que dependiendo cuantos numeros tiene el arreglo restarlo 1, a lo que me refiero es que si quieres ver la posicion 1 tendrias que poner 0, ya que empieza con 0 la primera posicion, asi que si un arreglo de es de tres o mas, se tendria que poner print(miLista[2]) para ver el lugar del digito del arreglo que seria la posicion 3
miLista = [1, 2, 3, 4, 5, 6, 7]

i = 0
for element in miLista:
    miLista[i] +=5
    i +=1

print(miLista)


#funcion que reciba lista y devuelve lista con solo numeros positivos, en "positivos = []" se crea porque ahi se alamcenaran los numeros positivos, por eso la lista vacia
def numerosPositivos(lista):
    positivos = []
    for elem in lista:
        if elem >=0:
            positivos.append(elem)
    return positivos

resultado = numerosPositivos([5, 6, -5, 80, 25])
print(resultado)



listaDeMultiplicacion = [i * i for i in range(11)]
print(listaDeMultiplicacion)

listaDeMultiplicacionOrden = [(i,i * i) for i in range(11)]
print(listaDeMultiplicacionOrden)

multiplica = lambda a,b: a*b 
resolve = multiplica (2,8)
print(resolve)