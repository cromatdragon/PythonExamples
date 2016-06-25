#!/usr/bin/env python3

# Ejercicio: Debemos pedir dos números por teclado, realizando la suma,
# resta, multiplicación y división mostrando el resultado por la pantalla.
# No podemos ingresar número negativos.

# Importamos este módulo para poder usar comandos del sistema
import subprocess

# Declaramos las variables necesarias
linea1="Calcular la suma, resta, multiplicación y división"
linea2=" de dos números dados por teclado."
n2=n1=-1

# Mostramos el enunciado
input(linea1+linea2)

# Comenzamos con la primera validación
while n1 < 0 :
	subprocess.call('clear')
	n1=float(input("Introduce el primer número que no sea negativo: "))


# Comenzamos con la segunda validación
while n2 < 0 :
	subprocess.call('clear')
	n2=float(input("Introduce el segundo número que no sea negativo: "))
	
# Calculamos la suma
print("La suma de "+str(round(n1,2))+" y de "+str(round(n2,2))+" es igual a: "+str(round(n1+n2,2)))
# Calculamos la resta
print("La resta de "+str(round(n1,2))+" y de "+str(round(n2,2))+" es igual a: "+str(round(n1-n2,2)))
# Calculamos la multiplicación
print("La multiplicación de "+str(round(n1,2))+" y de "+str(round(n2,2))+" es igual a: "+str(round(n1*n2,2)))
# Calculamos la división
print("La división de "+str(round(n1,2))+" y de "+str(round(n2,2))+" es igual a: "+str(round(n1/n2,2)))
