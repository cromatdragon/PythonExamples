#!/usr/bin/env python3
# Ejercicio: este ejercicio nos pide que, dados tres número positivos
# por teclado, averigüemos cual es el mayor, el menor y el mediano.


# Importamos este módulo para poder usar comandos del sistema
import subprocess

# Declaramos las variables necesarias
linea1="Dados tres números positivos por teclado, indicar "
linea2="\n cual es el mayor, el menor y el mediano."
n3=n2=n1=-1

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

# Comenzamos con la tercera validación
while n3 < 0 :
	subprocess.call('clear')
	n3=float(input("Introduce el tercer número que no sea negativo: "))
	
if n1>n2 and n1>n3 : # Primera comprobación
	mayor=n1
	if n2>n3 : mediano=n2;pequeno=n3
	else : mediano=n3;pequeno=n2
elif n2>n1 and n2>n3 : # Segunda comprobación		
	mayor=n2
	if n1>n3 : mediano=n1;pequeno=n3
	else : mediano=n3;pequeno=n1
else : # Tercera comprobación
	mayor=n3
	if n1>n2 : mediano=n1;pequeno=n2
	else : mediano=n2;pequeno=n1

# Mostramos por pantalla el resultado
print("El mayor es " +str(round(mayor,2))+
" el mediano es "+str(round(mediano,2))+
" y el pequeño es "+str(round(pequeno,2)))
