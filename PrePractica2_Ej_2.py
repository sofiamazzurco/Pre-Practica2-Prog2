#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

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

impares=[]
for numero in numeros:
    if numero%2!=0 :
        impares.append(numero)
print("La lista de los impares es:")
print(impares)


#FIN
#:)