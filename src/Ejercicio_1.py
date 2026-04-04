def Stats(text):
    texto = text.split(".")
    nested_words = [word.split() for i, word in enumerate(texto)]
    word_in_sentence = [element for sublist in nested_words for element in sublist]
    prom = len(word_in_sentence)/len(texto)
    return texto, nested_words, word_in_sentence, prom