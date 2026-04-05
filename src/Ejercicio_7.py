import random
def amigo_inv():
    nombres = input("Porfavor ingrese los nombres de los participantes separados por comas. \n")
    nombres = nombres.strip(" ")
    #Genero primero un set, el cual no posee espacios en los nombres (Para asegurarme de que no
    #hayan errores) luego, creo una lista de los participantes. Descarto repetidos con set.
    lista = list(set(p.strip().lower() for p in nombres.split(",")))
    #Verifico condiciones
    if len(nombres)>3:
        no_copias = False
        mezclados = lista.copy()
        while not no_copias:
            random.shuffle(mezclados)
            #Verifico que nadie se asigne a si mismo.
            if not any(lista[i] == mezclados[i] for i in range(len(lista))):
                no_copias = True

    parejas = {}
    #Asigno
    for i, name in enumerate(lista):
        parejas[lista[i]] = mezclados[i]

    print(parejas)