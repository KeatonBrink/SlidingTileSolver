import math


def isPrime(x):
    s = int(math.sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True


class HashTable:
    def __init__(self, maxNames):
        maxNames = 2*maxNames + 1
        while not isPrime(maxNames):
            maxNames += 2
        self.HashTable = [None]*maxNames
        self.addedNames = 0

    def Delete(self, item):
        if not self.Exists(item):
            return False
        index = int(item) % len(self.HashTable)
        while not (self.HashTable[index] and self.HashTable[index] == item):
            index += 1
            if index == len(self.HashTable):
                index = 0
        self.HashTable[index] = False
        self.addedNames -= 1
        return True

    def Size(self):
        return self.addedNames

    def Insert(self, item):
        index = item[0] % len(self.HashTable)
        while self.HashTable[index]:
            index += 1
            if index == len(self.HashTable):
                index = 0
        self.addedNames += 1
        self.HashTable[index] = item
        return True

    def Traverse(self, callback):
        for elt in self.HashTable:
            if elt is not None:
                callback(elt)

    def Retrieve(self, item):
        index = int(item) % len(self.HashTable)
        while not (self.HashTable[index] and self.HashTable[index][0] == int(item)):
            index += 1
            if index == len(self.HashTable):
                index = 0
        return self.HashTable[index][1]

    def Exists(self, item):
        index = int(item) % len(self.HashTable)
        while True:
            if self.HashTable[index] is None:
                return False
            elif self.HashTable[index] and self.HashTable[index] == item:
                return True
            index += 1
            if index == len(self.HashTable):
                index = 0
