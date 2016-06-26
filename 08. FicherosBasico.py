#!/usr/bin/env python3
# Ejercicio: Crear un programa que pueda leer y escribir contenido en
# un fichero
 
import subprocess
import sys
 
try: # Verificamos que no existan excepciones
	fichero=open("leeme.txt","wt+")
 
except: # Si surge algún error...
	fichero.close # ... cerramos el fichero
	input("A surgido un error al abrir/crear el fichero")
 
else: # Si no existe ninguna excepción, ejecutará las siguientes lineas
	while 1: # Bucle infinito
		subprocess.call("clear")
		print("Elige una opción")
		print("************************************")
		print(" 1) - Añadir contenido al fichero")
		print(" 2) - Leer el contenido del fichero")
		print(" 0) - Salir del programa")
		print("************************************")
		try:
			opcion=int(input("¿Que opción escoges? "))
			subprocess.call("clear")
			
		except ValueError: # si tecleamos un caracter no numérico...
			input("\nERROR. No has tecleado un valor numérico.")
			
		else:
			if opcion == 0:
				fichero.close # cerramos el fichero
				print("\nSaliendo del programa. Hasta la próxima.")
				sys.exit(0) # salimos del programa
			elif opcion == 1:
				linea=input("Escribe lo que quieras almacenar en el archivo: ")
				fichero.write(linea)
			elif opcion == 2:
				fichero.seek(0) # movemos el puntero al inicio del fichero
				linea=fichero.read()
				input(linea)
			else:
				input("La opción no es válida, vuelve a intentarlo.")
