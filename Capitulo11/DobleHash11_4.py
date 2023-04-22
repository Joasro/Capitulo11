import random
def multiplicativeHash(key):
    # Función de hashing multiplicativa
    Valorhash = 0
    byteMask = 0xFF
    pr1 = 53
    pr2 = 89
    while key > 0:
        byte = key & byteMask
        Valorhash = Valorhash * pr1 + (byte + pr2)
        key >>= 8
    return Valorhash

def doubleHashProbe(start, key, size):
    yield start % size 
    step = multiplicativeHash(key) % 19 + 1
    for i in range(1, size):
        yield (start + i * step) % size

def insertKeys():

    tableSize = 23
    smallPrime = 19
    hashTable = [None] * tableSize
    keys = [random.randint(0, 99999) for _ in range(20)]
    for key in keys:
        index = multiplicativeHash(key) % tableSize
        if hashTable[index] is None:
            hashTable[index] = key
            print(f"{key} se inserto en la posición {index}")
        else:
            print(f"Colisión para {key} en la posición {index}")
            for i in doubleHashProbe(index, key, tableSize):
                if hashTable[i] is None:
                    hashTable[i] = key
                    print(f"{key} se inserto en la posición {i}")
                    break
    print(hashTable)