import random

class HashTable:
    def __init__(self, size, probe):
        self.size = size                 
        self.probe = probe               
        self.table = [None] * self.size   
        self.count = 0                    

    def hash_function(self, key):
        return key % self.size             

    def insert(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            hash_value = self.probe(hash_value)    
        self.table[hash_value] = key               
        self.count += 1                            

    def search(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value] == key:      
                return hash_value
            hash_value = self.probe(hash_value)
        return None

    def displaced_keys(self):
        displaced = 0
        for key in self.table:
            if key is not None and self.hash_function(key) != self.table.index(key):
                displaced += 1
        return displaced

def linear_probe(index):
    return (index + 1) % ht.size                    

def quadratic_probe(index):
    return (index + 1 ** 2) % ht.size                

def double_hash_probe(index):
    return (index + hash(index)) % ht.size           

# Funciones de plegado
def fold_three_digits(key):
    result = 0
    while key > 0:
        result += key % 1000  
        key //= 1000 
    return result 

def fold_two_digits(key):
    result = 0
    while key > 0:
        result += key % 100 
        key //= 100 
    return result 

def fold_k_digits(key, k):
    str_key = str(key) 
    groups = [str_key[i:i+k] for i in range(0, len(str_key), k)] 
    folded = sum(int(group) for group in groups)
    return folded 


key_set = random.sample(range(10000000000), 1000)


max_load_factors = [0.5, 0.7, 0.9]
probe_types = [linear_probe, quadratic_probe, double_hash_probe]


for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe) 
        for i in range(int(103 * load_factor)):  
            key = fold_three_digits(key_set[i]) 
            ht.insert(key) 
        displaced = ht.displaced_keys() 
        print("Folding con tres dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))


for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe)
        for i in range(int(103 * load_factor)):
            key = fold_two_digits(key_set[i])
            ht.insert(key)
        displaced = ht.displaced_keys()
        print("Folding con dos dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))