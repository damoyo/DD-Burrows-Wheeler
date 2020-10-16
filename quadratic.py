class QuadraticProbingTable:

    def __init__(self, size):
        self.count = 0
        self.array = [None] * size
        self.tablesize = size

    def __len__(self):
        return self.count

    def new_hash(self, word):
        value = 0
        a = 31415
        b = 27183
        for i in range(len(word)):
            value = (value * a + ord(word[i])) % self.tablesize
            a = a * b % (self.tablesize)
        return value

    def insert (self, key):
        position = self.new_hash(key)
        for i in range(self.tablesize):
            if self.array[position] is None:  # found empty slot add key and 1
                self.array[position] = (key, 1)
                self.count += 1
                return
            elif self.array[position][0] == key:  # found key add plus one to the tuple
                addition = self.array[position][1] + 1
                self.array[position] = (key, addition)
                return
            else:  # not found, try next
                position = (position + 1) % self.tablesize

        #self.rehash()
        #self.insert(key, data)

    def lookup(self, key):
        position = self.new_hash(key)
        for i in range(self.tablesize):
            if self.array[position] is None:  # found empty slot
                raise KeyError
            elif self.array[position][0] == key:  # found key
                return self.array[position]
            else:  # not found, try next
                position = (position + 1) % self.tablesize
        raise KeyError(key)

    def delete(self, key):
        position = self.new_hash(key)
        if self.array[position] is None:  # found empty slot
            raise KeyError
        elif self.array[position][0] == key:  # found key then subtract 1 or delete key
            if self.array[position][1] == 0:
                self.array[position] = None
                self.count -= 1
                return
            else:
                subtraction = self.array[position][1] - 1
                self.array[position] = (key, subtraction)
                print('Delete (Subtraction) successful')
                return