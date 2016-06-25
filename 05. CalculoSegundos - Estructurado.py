#!/usr/bin/env python3
# Ejercicio: En este ejercicio, debemos ingresar un número en segundos, 
# y nos calculará el total de horas, minutos y segundos que lo componen.
# Sabemos que 1 hora son 60 minutos, y cada minuto, 60 segundos.

# Importamos este módulo para poder usar comandos del sistema
import subprocess
 
# Declaramos las variables necesarias
enunciado="""Dados los segundos por teclado, calcular cuantas horas
segundos y minutos representan"""
segundos=0
 
# Mostramos el enunciado
input(enunciado)
 
# Comenzamos con la validación
while segundos < 1 :
	subprocess.call('clear')
	segundos=int(input("\n¿Cuantos segundos quieres calcular?: "))
 
subprocess.call('clear')
 
# Calculamos y mostramos el resultado
print(str(round(segundos))+" segundos son:\n\n"+str(round(segundos/3600))+" horas\n")
print(str(round((segundos%3600)/60))+" minutos\n")
print(str(round((segundos%3600)%60))+" segundos")
