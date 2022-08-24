#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.
#INICIO
print("Ingrese dos numeros:")
num1 = int(input("Introduce el primer numero:"))
num2 = int(input("Introduce el segundo numero:"))

try:
  resultado=num1/num2
  print(resultado)
except ZeroDivisionError as exception:
  print("No se puede dividir por cero.")

#FIN