"""
Practica 4 - Desarrollo de aplicaciones web

Resumen
--------
Este software consiste en una emulación del juego del ahorcado. Al iniciar
el script y una palabra es elegida al azar, la cual deberá ser adivinada.
El usuario tiene 6 oportunidades (cabeza, brazos, torso y piernas), las
letras repetidas no cuentan como oportunidad perdida ya sea que sean correctas
o incorrectas, al completar la palabra el usuario gana el juego de lo contrario
terminá ahorcado.

Dependencias
------------
+ python3.5
+ lemario.txt
"""

import random
import click

MAXTRIES = 6

HANGMAN_ART = (
    """
       _________
        |/
        |
        |
        |
        |
        |
        |___
    """,
    """
       _________
        |/   |
        |   (_)
        |
        |
        |
        |
        |___
    """,
    """
       ________
        |/   |
        |   (_)
        |    |
        |    |
        |
        |
        |___
    """,
    """
       _________
        |/   |
        |   (_)
        |   /|
        |    |
        |
        |
        |___
    """,
    """
       _________
        |/   |
        |   (_)
        |   /|\\
        |    |
        |
        |
        |___
    """,
    """
       ________
        |/   |
        |   (_)
        |   /|\\
        |    |
        |   /
        |
        |___
    """,
    """
       ________
        |/   |
        |   (_)
        |   /|\\
        |    |
        |   / \\
        |
        |___
    """,
)


def pick_random_word():
    """
    Esta función elige una palabra al azar del diccionario
    """
    # abre el diccionario
    with open("lemario.txt", "r", encoding="utf8") as file:
        words = file.readlines()

    # genera un indice aleatorio
    # -1 porque len(words) no es un indice valido en la lista `words`
    index = random.randint(0, len(words) - 1)

    # toma la palabra que se encuentra en ese indice,
    # remueve el retorno de carro (strip) y convierte a mayúsculas (upper)
    word = words[index].strip().upper()
    return word


def ask_user_for_next_letter():
    """
    Esta función le pide al usuario la siguiente
    letra
    """
    letter = input("Adivina la siguiente letra: ")
    # TODO .. validate that the user enters only one letter
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    """
    Función que genera el diagrama de letras adivinadas y ocultas
    """
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)


def clean_screen():
    # Limpiar pantalla (se usa el modulo click para soportar multiplataforma)
    click.clear()


def main():
    """
    Función principal de la aplicación
    """
    clean_screen()

    word = pick_random_word()
    letters_to_guess = set(word)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()

    print("Bienvenido al juego del ahorcado!")
    while len(letters_to_guess) > 0 and len(incorrect_letters_guessed) < MAXTRIES:

        word_string = generate_word_string(word, correct_letters_guessed)
        print("\n\n\n\n")
        print(word_string)
        print("Quedan {} intentos".format(MAXTRIES - len(incorrect_letters_guessed)))
        print(HANGMAN_ART[len(incorrect_letters_guessed)])

        guess = ask_user_for_next_letter()

        # limpia pantalla
        clean_screen()

        # Revisar si ya se adivino esa
        # letra
        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            # imprime un mensaje
            print("Ya se adivino esa letra.")
            continue

        # si la respuesta es correcta
        if guess in letters_to_guess:
            # actualizar la lista letters_to_guess de letras por adivinar
            letters_to_guess.remove(guess)
            # actualizar la lista letters de letras adivinadas
            correct_letters_guessed.add(guess)
        else:
            # solo actualizar la lista de respuestas incorrectas
            # si se adivino incorrectamente
            incorrect_letters_guessed.add(guess)

    # Decirle al usuario si gano o perdió
    if len(letters_to_guess) == 0:
        print("Felicitaciones! Adivinaste correctamente {}".format(word))
    else:
        print("Lo siento, la palabra era {}".format(word))


if __name__ == "__main__":
    main()
