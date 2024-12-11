import csv
import numpy as np

class DSAHashTable:

    class _DSAHashEntry:

        STATE_NEVER_USED = 0
        STATE_USED = 1
        STATE_FORM_USED = -1

        def __init__(self, key="", value=None, state=STATE_NEVER_USED):
            self.key = key
            self.value = value
            self.state = state

        def __str__(self):
            return f"HashEntry: key={self.key} value={self.value} state={self.state}"

    MAX_STEP = 13
    DUMP_MAX_ITEM_NUM = 20
    THRESHOLD_LOW = 0.2
    THRESHOLD_HIGH = 0.6

    def __init__(self, size):
        self.initHashArray(size)
        self.count = 0
        self.resizing = False

    def initHashArray(self, size):
        actualSize = self._nextPrime(size)
        self.hashArray = np.arange(actualSize, dtype=object)
        for i in range(actualSize):
            self.hashArray[i] = DSAHashTable._DSAHashEntry()

    def get(self, key):
        try:
            hashIdx = self._findKey(key)
            ret = self.hashArray[hashIdx].value
            return ret
        except KeyError:
            return None

    def put(self, key, value):
        try:
            hashIdx, override = self._findEmpty(key)
            self.hashArray[hashIdx].state = DSAHashTable._DSAHashEntry.STATE_USED
            self.hashArray[hashIdx].key = key
            self.hashArray[hashIdx].value = value
            if not self.resizing and not override:
                self.count += 1
                self._resize()
            return True
        except KeyError:
            return False

    def remove(self, key):
        try:
            hashIdx = self._findKey(key)
            self.hashArray[hashIdx].state = DSAHashTable._DSAHashEntry.STATE_FORM_USED
            self.hashArray[hashIdx].key = ""
            self.hashArray[hashIdx].value = None
            if not self.resizing:
                self.count -= 1
                self._resize()
            return True
        except KeyError:
            return False

    def getLoadFactor(self):
        return round(self.count / self.hashArray.size, 2)

    def export(self):
        raise NotImplementedError("Not implemented")

    def _resize(self):
        self.resizing = True
        lf = self.getLoadFactor()
        size = self.hashArray.size
        new_size = size
        if lf > self.THRESHOLD_HIGH:
            # Double size
            new_size = size * 2
        elif lf < self.THRESHOLD_LOW:
            # Harf size
            new_size = int(size / 2)
        if new_size != size:
            hashArrayBak = self.hashArray
            self.initHashArray(new_size)
            for i in range(size):
                if hashArrayBak[i].state == DSAHashTable._DSAHashEntry.STATE_USED:
                    self.put(hashArrayBak[i].key, hashArrayBak[i].value)
            # print(f"resize, old lf: {lf}, new lf: {self.getLoadFactor()}")
        self.resizing = False

    # Prop 1: Hash indexes must fit table
    # Prop 2: Fast to compute
    # Prop 3: Repeatable
    # Prop 4: Distributes keys evenly
    def _hash(self, key):
        hashIdx = 0
        for i in range(len(key)):
            hashIdx = (33 * hashIdx) + ord(key[i])
        return hashIdx % self.hashArray.size

    def _stepHash(self, key):
        num = 0
        for i in range(len(key)):
            num += ord(key[i])
        hashStep = self.MAX_STEP - (num % self.MAX_STEP)
        if hashStep == 0:
            hashStep += 1
        return hashStep

    def _nextPrime(self, size):
        if size % 2 == 0:
            prime = size + 1
        else:
            prime = size
        prime -= 2
        isPrime = False
        while not isPrime:
            prime += 2
            i = 3
            isPrime = True
            while i * i <= prime and isPrime:
                if prime % i == 0:
                    isPrime = False
                else:
                    i += 2
        return prime

    def hasKey(self, key):
        try:
            self._findKey(key)
            return True
        except KeyError:
            return False

    def _checkKey(self, idx, key):
        if self.hashArray[idx].state == DSAHashTable._DSAHashEntry.STATE_USED:
            return self.hashArray[idx].key == key

    def _findKey(self, key):
        hashIdx = self._hash(key)
        if self._checkKey(hashIdx, key):
            return hashIdx
        origIdx = hashIdx
        step = self._stepHash(key)
        while True:
            hashIdx += step
            hashIdx = hashIdx % self.hashArray.size
            if hashIdx == origIdx:
                raise KeyError("Can't find avalible idx")
            if self._checkKey(hashIdx, key):
                return hashIdx

    def _checkEmpty(self, idx, key):
        if self.hashArray[idx].state != DSAHashTable._DSAHashEntry.STATE_USED:
            return True, False
        elif self.hashArray[idx].state == DSAHashTable._DSAHashEntry.STATE_USED:
            if self.hashArray[idx].key == key:
                # duplicate key, override it
                return True, True
        return False, False

    def _findEmpty(self, key):
        hashIdx = self._hash(key)
        empty, override = self._checkEmpty(hashIdx, key)
        if empty:
            return hashIdx, override
        origIdx = hashIdx
        step = self._stepHash(key)
        while True:
            hashIdx += step
            hashIdx = hashIdx % self.hashArray.size
            if hashIdx == origIdx:
                raise KeyError("Can't find avalible idx")
            empty, override = self._checkEmpty(hashIdx, key)
            if empty:
                return hashIdx, override

    def __str__(self):
        dumps = []
        dumps.append(f"Count: {self.count} Size: {self.hashArray.size} LF: {self.getLoadFactor()} Low: {self.THRESHOLD_LOW} High: {self.THRESHOLD_HIGH}")
        dump_idx = 0
        for i in range(self.hashArray.size):
            entity = self.hashArray[i]
            if entity.state == DSAHashTable._DSAHashEntry.STATE_USED:
                dumps.append(" " + str(entity))
                dump_idx += 1
                if dump_idx > self.DUMP_MAX_ITEM_NUM:
                    dumps.append('... ...')
                    break
        
        return "\r\n".join(dumps)

def testBasic():
    print("=====TEST basic function")
    testHash = DSAHashTable(5)
    print(testHash)
    testHash.put("1", 1)
    assert testHash.count == 1
    testHash.put("2", 2)
    assert testHash.count == 2
    print(testHash)
    assert testHash.get("1") == 1
    assert testHash.get("2") == 2
    testHash.put("3", 3)
    print(testHash)
    testHash.put("4", 4)
    print(testHash)
    testHash.put("5", 5)
    print(testHash)
    testHash.put("6", 6)
    print(testHash)
    testHash.put("7", 7)
    print(testHash)
    assert testHash.count == 7
    testHash.remove("1")
    print(testHash)
    assert testHash.count == 6
    testHash.remove("2")
    print(testHash)
    assert testHash.count == 5
    testHash.remove("3")
    print(testHash)
    assert testHash.count == 4
    testHash.remove("4")
    print(testHash)
    assert testHash.count == 3
    testHash.remove("5")
    print(testHash)
    assert testHash.count == 2
    testHash.remove("6")
    print(testHash)
    assert testHash.count == 1
    testHash.remove("7")
    print(testHash)
    assert testHash.count == 0
    assert not testHash.remove("9")
    assert testHash.get("9") is None

def testCsv():
    print("=====TEST RandomNames7000")
    testHash = DSAHashTable(5)
    key_record = {}
    with open('RandomNames7000.csv') as csvFile:
        items = csv.reader(csvFile)
        for idx, item in enumerate(items):
            # print(idx, item)
            if item[0] in key_record:
                print(f"Dup key: {item[0]}, old val: {key_record[item[0]]}, new val: {item[1]}")
            testHash.put(item[0], item[1])
            key_record[item[0]] = item[1]
        print(testHash)
    with open('RandomNames7000_out.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for i in range(testHash.hashArray.size):
            item = testHash.hashArray[i]
            if item.state == DSAHashTable._DSAHashEntry.STATE_USED:
                writer.writerow([item.key, item.value])

if __name__ == "__main__":
    testBasic()
    testCsv()

