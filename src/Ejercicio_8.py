def input_word():
    word = input("Ingrese la contraseña a cifrar: \n")
    fixed_pos = int(input("Ingrese el desplazamiento: \n"))
    return word, fixed_pos

def cipher(word,fixed_pos):
    cipher_letter = 0
    cipher_word = ""
    for letter in word:
#Verifico si es alfanumerico y si es mayuscula o minuscula.
        if letter.isalpha():
#En ambos resto el caso limite mas bajo, que es "a" y "A" para operar en un rango del 0 al 25
#Y luego le sumo nuevamente el caso limite bajo para obtener el ascii correspondiente.
            if letter.isupper():
                cipher_letter = (ord(letter) - ord("A") + fixed_pos) % 26 + ord("A")
            else:
                cipher_letter = (ord(letter) - ord("a") + fixed_pos) % 26 + ord("a")
            cipher_word = cipher_word + chr(cipher_letter)
        else:
            cipher_word += letter
    return cipher_word

def decipher(cipher_word,fixed_pos):
    deciphered_word = ""
    cipher_letter = ""
    for letter in cipher_word:
        if letter.isalpha():
            if letter.isupper():
                cipher_letter = (ord(letter) - ord("A") - fixed_pos) % 26 + ord("A")
            else:
                cipher_letter = (ord(letter) - ord("a") - fixed_pos) % 26 + ord("a")
            deciphered_word = deciphered_word + chr(cipher_letter)
        else:
            deciphered_word += letter
    return deciphered_word