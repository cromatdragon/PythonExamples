#!/usr/bin/env python3
# Ejercicio: mostrar por pantalla la letra correspondiente a un número
# de DNI dado por teclado.

import subprocess

letras="TRWAGMYFPDXBNJZSQVHLCKE"
dni=""

# Si el DNI introducido no tiene la longitud correcta, volvemos a pedirlo
while len(dni) != 8:
	subprocess.call("clear")
	print("Vamos a calcular la letra de un DNI que me des por teclado.\n")
	dni=input("¿Que DNI quieres calcular?: ")

ndni=int(dni)%23 # Convertimos y calculamos el resto

print("\nLa letra del DNI "+dni+" es "+letras[ndni])
