#!/usr/bin/env python3
# Ejercicio: Implementar un programa para jugar al rojo, amarillo y verde.
# El programa genera tres dígitos aleatorios entre el 0 y el 9. A estos
# dígitos se le asignan las posiciones 1, 2 y 3. El objetivo del juego
# es adivinar los dígitos así como su posición en un número de intentos
# máximo. Para cada intento, el jugador proporciona 3 números para las
# posiciones 1, 2 y 3. El programa responde con una pista que será rojo,
# amarillo o verde. Si un número está en la posición correcta, responde
# con el color verde, si el número es correcto, pero no lo es la posición,
# el color será amarillo, si no coincide, será rojo.

import subprocess # Módulo para usar comandos del sistema
import random # Módulo para generar números aleatorios
 
def validar(elemento): # Creamos la función para validar
		flag = 0
		while flag == 0:
			subprocess.call('clear')
			variable=input("Introduce el "+elemento+" número: ")
			if len(variable) > 1 or len(variable) < 1:
				input("\n\x1b[31m¡ERROR!\x1b[0m Solo te pido un número.")
			elif str.isdigit(variable) == False:
				input("\n\x1b[31m¡ERROR!\x1b[0m No has escrito un número.")
			else:
				flag = 1
				return int(variable)
 
# Creamos la función para mostrar el resultado
def mostrar_resultado(opcion,l_random):
	subprocess.call('clear')
	if opcion == 1:
		print("\x1b[32m¡¡Acertaste!!\x1b[0m los números eran "
		+str(l_random[0])+" "+str(l_random[1])+" "+str(l_random[2]))
	else:
		print("\x1b[31m¡Has fallado los cinco intentos!\x1b[0mn Los números eran "
		+str(l_random[0])+" "+str(l_random[1])+" "+str(l_random[2]))
 
# Declaramos las variables necesarias
lista = [] # Creamos una lista vacia...
l_random = [] # ... otra para los aleatorios
posicion = ["primer","segundo","tercer"] # y otra con elementos
opcion = contador = 0
 
while contador < 3: # Generamos los nº aleatorios
	l_random.append(random.randint(0,9))
	contador = contador + 1
 
input("""Comienza el juego. Adivina tres números, del 0 al 9
 y la posición de los mismos. Si el número es el correcto, y 
 está en la posición correcta, se mostrará en verde; si el 
 número es el correcto, pero no la posición, será amarillo 
 y si no hay el númmero, rojo.\n\n""")
 
contador = 0
while contador < 5:
	subprocess.call('clear')
 
	x = 0
	for elemento in posicion:
		lista.insert(x,validar(elemento))
		x = x + 1
 
# Comparamos el primer número	
	if lista[0] == l_random[0]: 
			print("\x1b[32mVerde\x1b[0m "+ str(lista[0]))
	elif lista[0] == l_random[1] or lista[0] == l_random[2]:
			print("\x1b[33mAmarillo\x1b[0m "+str(lista[0]))
	else:
			print("\x1b[31mRojo\x1b[0m "+str(lista[0]))
# Comparamos el segundo número
	if lista[1] == l_random[1]: 
			print("\x1b[32mVerde\x1b[0m "+ str(lista[1]))
	elif lista[1] == l_random[0] or lista[1] == l_random[2]:
			print("\x1b[33mAmarillo\x1b[0m "+str(lista[1]))
	else:
			print("\x1b[31mRojo\x1b[0m "+str(lista[1]))
# Comparamos el tercer número			
	if lista[2] == l_random[2]: 
			print("\x1b[32mVerde\x1b[0m "+ str(lista[2]))
	elif lista[2] == l_random[1] or lista[2] == l_random[0]:
			print("\x1b[33mAmarillo\x1b[0m "+str(lista[2]))
	else:
			print("\x1b[31mRojo\x1b[0m "+str(lista[2]))
# Condicional para saber si hemos acertado
	if lista[0] == l_random[0] :
			if lista[1] == l_random[1] and lista[2] == l_random[2]:
				contador=4
				opcion=1
	contador = contador + 1
	input()
 
mostrar_resultado(opcion,l_random)
