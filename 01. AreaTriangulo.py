#!/usr/bin/env python3

# Ejercicio: Este ejercicio nos pide calcular el área de un triángulo.
# Debemos pedir por pantalla los datos necesarios, aplicar la ecuación 
# y mostrar el resultado de la misma por pantalla, sabiendo que la
# ecuación para calcular el área de un triángulo es base * altura / 2
 
print("Este programa calcula el área de un triángulo\n")
input()
 
# Pedimos y almacenamos la base
print("\nPorfavor, teclea la base del triángulo: ")
base=float(input())
# Pedimos y almacenamos la altura
print("\nPorfavor, ahora teclea la altura del triángulo: ")
altura=float(input())
# Aplicamos la fórmula
superficie=base*altura/2
# Mostramos el resultado por pantalla
print("\nEl área del triángulo de base "+ str(base) +" y de altura "+ str(altura) +" es "+ str(superficie))
