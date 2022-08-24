#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print ("Ingrese una lista de 4 numeros:")
dimen=4
print(f"Voy a solicitarte {dimen} numeros:")
numeros=[]
for i in range(dimen):
    print("Ingrese el numero", i+1)
    numero=input("=")
    numero=int(numero)
    numeros.append(numero)
print(f"La lista es:")
print(numeros)

maxvalor=max(numeros)
print(f"El maximo valor con funcion es:")
print(maxvalor)

maxvalue=None
for numero in numeros:
    if(maxvalue is None or numero>maxvalue):
        maxvalue=numero
print(f"El maximo valor con comparacion es:")
print(maxvalue)

#FIN
#anda por favor