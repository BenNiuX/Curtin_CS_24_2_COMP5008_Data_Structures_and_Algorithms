import numpy as np

from DSAVehicle import Vehicle


class DSAHashTable:
    """
    DSAHashTable is used to define a hash table data abstract type.
    """

    class _DSAHashEntry:
        """
        _DSAHashEntry is used to define a hash entry in a hash table.
        """

        STATE_NEVER_USED = 0
        STATE_USED = 1
        STATE_FORM_USED = -1

        def __init__(self, key="", value=None, state=STATE_NEVER_USED):
            self.key = key
            self.value = value
            self.state = state

        def __str__(self):
            return f"HashEntry: key={self.key} value={self.value}" \
                   f" state={self.state}"

    MAX_STEP = 13
    DUMP_MAX_ITEM_NUM = 20
    THRESHOLD_LOW = 0.2
    THRESHOLD_HIGH = 0.6

    def __init__(self, size):
        self.initHashArray(size)
        self.count = 0
        self.resizing = False

    def initHashArray(self, size):
        """
        Init the hash array with a given size.
        """
        actualSize = self._nextPrime(size)
        self.hashArray = np.arange(actualSize, dtype=object)
        for i in range(actualSize):
            self.hashArray[i] = DSAHashTable._DSAHashEntry()

    def search(self, key):
        """
        Search a value by the given key.
        """
        try:
            hashIdx = self._findKey(key)
            ret = self.hashArray[hashIdx].value
            return ret
        except KeyError:
            return None

    def insert(self, vehicle):
        """
        Insert a vehicle into the hash table.
        """
        hashIdx, override = self._findEmpty(vehicle.vid)
        self.hashArray[hashIdx].state = DSAHashTable._DSAHashEntry.STATE_USED
        self.hashArray[hashIdx].key = vehicle.vid
        self.hashArray[hashIdx].value = vehicle
        if not self.resizing and not override:
            self.count += 1
            self._resize()

    def delete(self, key):
        """
        Delete a vehicle by the given key.
        """
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
        """
        Get the load factor of the hash table.
        """
        return round(self.count / self.hashArray.size, 2)

    def export(self):
        """
        Export all vehicles in the hash table to an array.
        """
        vehicles = np.arange(self.count, dtype=Vehicle)
        idx = 0
        for i in range(self.hashArray.size):
            entity = self.hashArray[i]
            if entity.state == DSAHashTable._DSAHashEntry.STATE_USED:
                vehicles[idx] = entity.value
                idx += 1
        return vehicles

    def _resize(self):
        """
        Resize the array in the hash table by the load factor.
        """
        self.resizing = True
        lf = self.getLoadFactor()
        size = self.hashArray.size
        new_size = size
        if lf > self.THRESHOLD_HIGH:
            # Double size
            new_size = size * 2
        elif lf < self.THRESHOLD_LOW:
            # Half size
            new_size = int(size / 2)
        if new_size != size:
            hashArrayBak = self.hashArray
            self.initHashArray(new_size)
            for i in range(size):
                if hashArrayBak[i].state == DSAHashTable._DSAHashEntry.STATE_USED:
                    self.insert(hashArrayBak[i].value)
            # print(f"resize, old lf: {lf}, new lf: {self.getLoadFactor()}")
        self.resizing = False

    # Prop 1: Hash indexes must fit table
    # Prop 2: Fast to compute
    # Prop 3: Repeatable
    # Prop 4: Distributes keys evenly
    def _hash(self, key):
        """
        Hash the key to an index in the hash table.
        """
        hashIdx = 0
        for i in range(len(key)):
            hashIdx = (33 * hashIdx) + ord(key[i])
        return hashIdx % self.hashArray.size

    def _stepHash(self, key):
        """
        Step hash method to avoid duplicated index.
        """
        num = 0
        for i in range(len(key)):
            num += ord(key[i])
        hashStep = self.MAX_STEP - (num % self.MAX_STEP)
        if hashStep == 0:
            hashStep += 1
        return hashStep

    def _nextPrime(self, size):
        """
        Get the next prime number by the given value.
        """
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
        """
        Check if the hash table contains the given key.
        """
        try:
            self._findKey(key)
            return True
        except KeyError:
            return False

    def _checkKey(self, idx, key):
        """
        Check if the key is in the hash table by the given index.
        """
        if self.hashArray[idx].state == DSAHashTable._DSAHashEntry.STATE_USED:
            return self.hashArray[idx].key == key

    def _findKey(self, key):
        """
        Find the index in the hash table from the key.
        """
        hashIdx = self._hash(key)
        if self._checkKey(hashIdx, key):
            return hashIdx
        origIdx = hashIdx
        step = self._stepHash(key)
        while True:
            hashIdx += step
            hashIdx = hashIdx % self.hashArray.size
            if hashIdx == origIdx:
                raise KeyError("Can't find available idx")
            if self._checkKey(hashIdx, key):
                return hashIdx

    def _checkEmpty(self, idx, key):
        """
        Check if the index is useful in the hash table.
        """
        if self.hashArray[idx].state != DSAHashTable._DSAHashEntry.STATE_USED:
            return True, False
        elif self.hashArray[idx].state == DSAHashTable._DSAHashEntry.STATE_USED:
            if self.hashArray[idx].key == key:
                # duplicate key, override it
                return True, True
        return False, False

    def _findEmpty(self, key):
        """
        Find an empty index in the hash table by the input key.
        """
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
                raise KeyError("Can't find available idx")
            empty, override = self._checkEmpty(hashIdx, key)
            if empty:
                return hashIdx, override

    def display(self):
        """
        Display the hash table.
        """
        print(str(self))

    def __str__(self):
        dumps = []
        dumps.append(f"Count: {self.count} Size: {self.hashArray.size}"
                     f" LF: {self.getLoadFactor()} Low: {self.THRESHOLD_LOW}"
                     f" High: {self.THRESHOLD_HIGH}")
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
