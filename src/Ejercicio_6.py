def cantidad_hashtags(posts):
    frecuencias = {}
#Separo las frases en una lista de palabras.
    for publicacion in posts:
        words = publicacion.split()
#Verifico que palabras de la lista poseen un #
        for word in words:
            if word.startswith("#"):
                if word in frecuencias:
                    frecuencias[word] += 1
                else:
                    frecuencias[word] = 1
#Ordeno el diccionario con un orden de mayor a menor en base a la cantidad de veces que aparecieron.
    dict_ord = dict(sorted(frecuencias.items(), key= lambda x: x[1], reverse = True))
    for clave, valor in dict_ord.items():
        if(valor>1):
            print(clave, valor)

    print(f"Total de hashtags unicos: {len(frecuencias)}")