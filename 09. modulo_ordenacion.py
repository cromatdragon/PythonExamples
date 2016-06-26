# Módulo con los seis algoritmos de ordenación usados en el blog
# blog.cromat-dragon.net by CromatDragon

# Función que aplica el algoritmo Shellshort
def shellsort(lista):
	indice=int(len(lista)/2)
	while(indice > 0):
		for contador in range(indice,len(lista)):
			temporal=contador
			indice2=lista[contador]
			while((temporal >= indice) and (lista[temporal-indice] > indice2)):
				lista[temporal]=lista[temporal-indice]
				temporal=temporal-indice
			lista[temporal]=indice2
		if(indice == 2):
			indice=1
		else:
			indice=int(indice/2.2)
	return lista

# Función que aplica el algoritmo Selectionsort
def selectionsort(lista):
	for primero in range(0,len(lista)-1): 
		elemento = lista[primero] # Almacenamos el primer número...
		segundo = primero # ... y su indice

		# Comenzamos aplicando el algoritmo de selección
		for tercero in range(primero,len(lista)):
			if lista[tercero] < elemento:
				segundo = tercero
				elemento = lista[tercero]
		lista[segundo] = lista[primero]
		lista[primero] = elemento
	return lista

# Función que aplica el algoritmo Mergesort
def mergesort(lista):
	if len(lista) == 1:
		return lista
	else:
		medio = len(lista)//2
		izquierda = mergesort(lista[:medio])
		derecha = mergesort(lista[medio:])
		
		if not len(izquierda) or not len(derecha):
			return izquierda or derecha
		  
		temporal = []
		cont1 = cont2 = 0

		while (len(temporal) < len(derecha)+len(izquierda)):
			if izquierda[cont1] < derecha[cont2]:
				temporal.append(izquierda[cont1])
				cont1 += 1
			else:
				temporal.append(derecha[cont2])
				cont2 += 1

			if cont1 == len(izquierda) or cont2 == len(derecha):
				temporal.extend(izquierda[cont1:] or derecha[cont2:])
				break
		  
		return temporal

# Función que aplica el algoritmo Insertionsort
def insertionsort(lista):
	for primero in range(len(lista)): # iteramos sobre el largo de la lista
		indice = lista[primero]
		segundo = primero-1
		while (segundo >= 0 and lista[segundo] > indice):
			lista[segundo+1] = lista[segundo]
			segundo = segundo-1
		lista[segundo+1] = indice
	return lista

# Función que aplica el algoritmo Cocktailsort
def cocktailsort(lista):
    final = range(len(lista)-1)
    while True:
        for elemento in (final, reversed(final)):
            cambiado = False
            for cont1 in elemento:
                if lista[cont1] > lista[cont1+1]:
                    lista[cont1], lista[cont1+1] =  lista[cont1+1], lista[cont1]
                    cambiado = True
            if not cambiado:
                return lista

# Función que aplica el algoritmo Bubblesort
def bubblesort(lista):
    flag = True  
    while flag:  
        flag = False  
        for contador in range(len(lista)-1):  
            if lista[contador] > lista[contador+1]:  
                lista[contador], lista[contador+1] = lista[contador+1], lista[contador]  
                flag = True  
    return lista
