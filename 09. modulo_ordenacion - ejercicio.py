#!/usr/bin/env python3
# Ejercicio: aplicar el módulo creado en pasos anteriores para hacer
# la llamada a las distintas funciones

import subprocess
import sys
import modulo_ordenacion

def recoger_datos():
	total=int(input("¿Cuantos elementos quieres añadir? "))
	for contador in range(0,total):
		lista.insert(contador,int(input("Añade el elemento número "+str(contador+1)+": ")))

	print("Esta es la lista sin ordenar: ",lista)

while 1: # Bucle infinito
	# Creo una lista con los nombres de los algoritmos, para ser más específicos en la
	# salida de datos
	algoritmos=["Selección", "Inserción", "Mezcla", "Cocktail", "Shellsort", "Burbuja"]
	lista=[]

	subprocess.call("clear") # Limpiamos la pantalla
	print("Elige una opción")
	print("***********************************")
	print(" 1) - Método de selección")
	print(" 2) - Método de inserción")
	print(" 3) - Método de mezcla")
	print(" 4) - Método cocktail")
	print(" 5) - Método shell")
	print(" 6) - Método burbuja")
	print(" 0) - Salir del programa")
	print("***********************************")
	opcion=int(input("¿Que opción escoges? "))
	
	subprocess.call("clear")
	
	if opcion == 0: # Salimos del programa
		sys.exit(0)
	elif opcion == 1: # Usamos el algoritmo de selección
		recoger_datos()
		lista=modulo_ordenacion.selectionsort(lista)
	elif opcion == 2: # Usamos el algoritmo de inserción
		recoger_datos()
		lista=modulo_ordenacion.insertionsort(lista)
	elif opcion == 3: # Usamos el algoritmo de mezcla
		recoger_datos()
		lista=modulo_ordenacion.mergesort(lista)
	elif opcion == 4: # Usamos el algoritmo de cocktail
		recoger_datos()
		lista=modulo_ordenacion.cocktailsort(lista)
	elif opcion == 5: # Usamos el algoritmo de shellsort
		recoger_datos()
		lista=modulo_ordenacion.shellsort(lista)
	elif opcion == 6: # Usamos el algoritmo de burbuja
		recoger_datos()
		lista=modulo_ordenacion.bubblesort(lista)
	else: # Si tecleamos cualquier otra cosa, saldrá este mensaje
		input("Has escrito una opción no válida. Por favor, inténtalo de nuevo")
	
	print("Esta es la lista ordenada por el método de "+algoritmos[opcion-1]+" : ",lista)
	input()
