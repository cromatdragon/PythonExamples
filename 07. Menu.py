#!/usr/bin/env python3
# Ejemplo de menú

import subprocess
import sys
 
while 1: # Bucle infinito
	subprocess.call("clear")
	print("Elige una opción")
	print("***********************************")
	print(" 1) - Sumar dos números")
	print(" 2) - Restar dos números")
	print(" 3) - Dividir dos números")
	print(" 4) - Multiplicar dos números")
	print(" 0) - Salir del programa")
	print("***********************************")
	opcion=int(input("¿Que opción escoges? "))
	
	subprocess.call("clear")
	
	if opcion == 0:
		sys.exit(0)
	elif opcion == 1:
		input("Lanzaríamos la llamada a una función que sumara.")
	elif opcion == 2:
		input("Lanzaríamos la llamada a una función que restara.")
	elif opcion == 3:
		input("Lanzaríamos la llamada a una función que dividiera.")
	elif opcion == 4:
		input("Lanzaríamos la llamada a una función que multiplicara.")
