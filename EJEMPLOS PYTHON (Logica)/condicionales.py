#condiciones como if... else

if(11 > 9): 
    print("La condicion se logro")
    print("Hurra")
else: 
    print("La condicion no se logro")
    print("Sad")

numero = -9
if numero > 0: #aqui pregunta si numero es mayor a 0
    print("el numero es positivo")
elif numero == 0: #Esta seria una condicion secundaria (si numero es igual a 0)
    print("numero es cero")
else: 
    print("el numero es negativo")

a = 10
b = 20
if a != b or a > b: # != (significa distinto de), otro metodo tambien podria ser if a != b and a > b: que serian que se tiene que cumplir las dos condiciones, para que una condicon u otra se pueda cumplir se puede poner if a != b or a > b:
    print("Condicion cumplida")
else:
    print("No se cumplio la condicion")