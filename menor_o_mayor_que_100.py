# Escribir un programa que detecte si un número 
# leido desde el teclado ed mayor o menor que 100

numero = int(input("Ingrese un número : "))

if numero > 100:
  print("El numero es mayor que 100")
elif numero < 100:
  print("El numero es menor que 100")
elif numero == 100:
  print("El numero es igual a 100")