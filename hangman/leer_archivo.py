def readWords():
    with open('lemario.txt', 'r', encoding='utf8') as file:
        words = file.readlines()

    return words


if __name__ == '__main__':
    words = readWords()
    print('Cantidad de palabras: ', len(words))
