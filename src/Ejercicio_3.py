def leo_palabras():
    palabras = []
    palabraIng = input("Ingrese las palabras a censurar separadas por comas.\n").lower()
    palabras = palabraIng.split(",")
    return palabras

def censuro(palabras,review):
    for word in review.split():
#Convierto la palabra actual a minusculas para poder ver si existe dentro de la lista palabras.
        if word.lower() in palabras:
            review = review.replace(word, "*"*len(word))
    return review

