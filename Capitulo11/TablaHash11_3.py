import random

class HashTable:
    def __init__(self, size=128):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.used_cells = 0
        
    def __len__(self):
        return self.used_cells
    
    def __contains__(self, key):
        return self.get(key) is not None
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size
    
    def __getitem__(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self.rehash(index)
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self.rehash(index)
        self.keys[index] = key
        self.values[index] = value
        self.used_cells += 1
        if self.used_cells > self.size // 2:
            self.__growTable()
        
    def __growTable(self):
        old_keys = self.keys
        old_values = self.values
        self.size *= 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.used_cells = 0
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self[old_keys[i]] = old_values[i]
    
    def __delitem__(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.used_cells -= 1
                return
            index = self.rehash(index)
        raise KeyError(key)

def test_hash_table():
    random.seed(1)
    load_factors = [0.5, 0.8, 0.9]
    probe_sequences = ['linear', 'quadratic', 'double']
    for lf in load_factors:
        for ps in probe_sequences:
            print(f"Probando load_factor={lf} y probe_sequence={ps}...")
            ht = HashTable(size=128)
            num_keys = int(lf * ht.size)
            for i in range(num_keys):
                key = random.randint(0, 10**7)
                ht[key] = i
            print(f"\tTamaño de la tabla después de insertar {num_keys} claves: {len(ht)}")
            try:
                for i in range(num_keys):
                    key = random.randint(0, 10**7)
                    ht[key] = i
                print(f"\tTamaño de la tabla después de insertar {num_keys} claves más: {len(ht)}")
            except Exception as e:
                print(f"\tERROR: se encontró una excepción {type(e).__name__} al insertar una clave:")
                print(f"\t\t{str(e)}")
test_hash_table()