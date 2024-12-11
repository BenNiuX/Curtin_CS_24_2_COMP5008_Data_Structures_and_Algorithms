import csv
import numpy as np

class DSAHeap:

    class _DSAHeapEntry:

        def __init__(self, priority, value):
            self.priority = priority
            self.value = value

        def __str__(self):
            return f"HeapEntry: priority={self.priority} value={self.value}"


    def __init__(self, size):
        self.heapArray = np.arange(size, dtype=object)
        self.count = 0

    def add(self, priority, value):
        self.heapArray[self.count] = DSAHeap._DSAHeapEntry(priority, value)
        self.count += 1
        self._trickleUp(self.heapArray, self.count - 1)

    def remove(self):
        ret = None
        if self.count > 0:
            ret = self.heapArray[0]
            self.count -= 1
            self.heapArray[0] = self.heapArray[self.count]
            self.heapArray[self.count] = None
            self._trickleDown(self.heapArray, 0, self.count)
        return ret

    def display(self):
        level = 0
        startIdx = 0
        count = 0
        print("Display as tree:")
        for i in range(self.count):
            level = i
            count = 2**level
            if startIdx >= self.count:
                break
            for j in range(count):
                if startIdx + j >= self.count:
                    break
                print(self.heapArray[startIdx + j].priority, end=" ")
            print()
            startIdx = count + startIdx

    def _trickleUp(self, heapArray, curIdx):
        parentIdx = int((curIdx - 1) / 2)
        if curIdx > 0:
            if heapArray[curIdx].priority > heapArray[parentIdx].priority:
                tmp = heapArray[parentIdx]
                heapArray[parentIdx] = heapArray[curIdx]
                heapArray[curIdx] = tmp
                self._trickleUp(heapArray, parentIdx)

    def _trickleDown(self, heapArray, curIdx, numItems):
        lIdx = curIdx * 2 + 1
        rIdx = lIdx + 1
        if lIdx < numItems:
            largeIdx = lIdx
            if rIdx < numItems:
                if heapArray[lIdx].priority < heapArray[rIdx].priority:
                    largeIdx = rIdx
            if heapArray[largeIdx].priority > heapArray[curIdx].priority:
                tmp = heapArray[largeIdx]
                heapArray[largeIdx] = heapArray[curIdx]
                heapArray[curIdx] = tmp
                self._trickleDown(heapArray, largeIdx, numItems)

    def heapify(self, heapArray, numItems):
        for i in range(int(numItems/2)-1, -1, -1):
            self._trickleDown(heapArray, i, numItems)

    def heapSort(self, heapArray, numItems):
        self.heapify(heapArray, numItems)
        for i in range(numItems-1, 0, -1):
            tmp = heapArray[0]
            heapArray[0] = heapArray[i]
            heapArray[i] = tmp
            self._trickleDown(heapArray, 0, i)

    def __str__(self):
        dumps = []
        dumps.append(f"Count: {self.count} Size: {self.heapArray.size}")
        for i in range(self.count):
            dumps.append(" " + str(self.heapArray[i]))
        return "\r\n".join(dumps)

def testBasic():
    print("=====TEST basic function")
    testHeap = DSAHeap(10)
    print(testHeap)
    testHeap.add(10, "10")
    print(testHeap)
    assert testHeap.count == 1
    assert testHeap.heapArray[0].priority == 10
    assert testHeap.heapArray[0].value == "10"
    testHeap.add(11, "11")
    testHeap.add(12, "12")
    print(testHeap)
    assert testHeap.heapArray[0].priority == 12
    assert testHeap.heapArray[0].value == "12"
    assert testHeap.heapArray[1].priority == 10
    assert testHeap.heapArray[1].value == "10"
    assert testHeap.heapArray[2].priority == 11
    assert testHeap.heapArray[2].value == "11"
    testHeap.add(9, "9")
    print(testHeap)
    testHeap.display()
    item = testHeap.remove()
    print(testHeap)
    assert item.priority == 12
    item = testHeap.remove()
    print(testHeap)
    assert item.priority == 11
    item = testHeap.remove()
    print(testHeap)
    assert item.priority == 10
    item = testHeap.remove()
    print(testHeap)
    assert item.priority == 9

def testAddRemove():
    print("=====TEST add and remove")
    testHeap = DSAHeap(100)
    testHeap.add(82, "")
    testHeap.add(70, "")
    testHeap.add(51, "")
    testHeap.add(63, "")
    testHeap.add(55, "")
    testHeap.add(37, "")
    testHeap.add(10, "")
    testHeap.add(43, "")
    testHeap.add(27, "")
    testHeap.add(30, "")
    testHeap.add(34, "")
    testHeap.display()
    testHeap.add(95, "")
    testHeap.display()
    testHeap.remove()
    testHeap.display()

def testSort():
    print("=====TEST sort")
    testHeap = DSAHeap(2)
    heapArray = np.arange(9, dtype=object)
    items = [(5,5),(4,4),(1,1),(11,11),(10,10),(3,3),(2,2),(16,16),(12,12)]
    for i,item in enumerate(items):
        heapArray[i] = DSAHeap._DSAHeapEntry(item[0], item[1])
    for i in range(heapArray.size):
        print(heapArray[i])
    testHeap.heapify(heapArray, heapArray.size)
    print("After heapify")
    for i in range(heapArray.size):
        print(heapArray[i])
    testHeap.heapSort(heapArray, heapArray.size)
    print("After heapSort")
    for i in range(heapArray.size):
        print(heapArray[i])

def testCsv():
    print("=====TEST RandomNames7000")
    heapArray = np.arange(7000, dtype=object)
    key_record = {}
    with open('RandomNames7000.csv') as csvFile:
        items = csv.reader(csvFile)
        for idx, item in enumerate(items):
            # print(idx, item)
            if item[0] in key_record:
                # print(f"Dup key: {item[0]}, old val: {key_record[item[0]]}, new val: {item[1]}")
                pass
            heapArray[idx] = DSAHeap._DSAHeapEntry(int(item[0]), item[1])
            key_record[item[0]] = item[1]
    print("Before sort")
    for i in range(10):
        print(i, heapArray[i])
    print("... ...")
    testHeap = DSAHeap(2)
    testHeap.heapSort(heapArray, heapArray.size)
    print("After sort")
    for i in range(10):
        print(i, heapArray[i])
    print("... ...")

if __name__ == "__main__":
    testBasic()
    testAddRemove()
    testSort()
    testCsv()
