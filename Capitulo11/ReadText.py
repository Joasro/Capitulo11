import string

# Abre el archivo de texto y lo lee
with open('bloc.txt', 'r') as file:
    text = file.read()

# Inicializa un diccionario vacío para contar las palabras
word_count = {}

# Convierte el texto a minúsculas y elimina los signos de puntuación
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# Separa el texto en palabras y las cuenta
for word in text.split():
    # Si la palabra no está en el diccionario, se agrega con un valor de 1
    if word not in word_count:
        word_count[word] = 1
    # Si la palabra ya está en el diccionario, se incrementa su valor en 1
    else:
        word_count[word] += 1

# Imprime la lista de palabras y sus conteos
for word, count in word_count.items():
    print(f'{word}: {count}')

