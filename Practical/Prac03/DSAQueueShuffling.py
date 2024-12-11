from DSAQueue import Queue

class QueueShuffling(Queue):

    def __init__(self, maxCap=Queue.DEFAULT_CAPACITY):
        super().__init__(maxCap)
 
    def moveForward(self):
        for index in range(0, self.count):
            self.queue[index] = self.queue[index + 1]

    def enqueue(self, value):
        if self.isFull():
            raise ValueError("Queue is full, enqueue fail")
        else:
            self.queue[self.count] = value
            self.count += 1

    def dequeue(self):
        peekVal = self.peek()
        self.count -= 1
        self.moveForward()
        return peekVal

    def peek(self):
        if self.isEmpty():
            raise ValueError("Queue is empty, peek fail")
        else:
            peekVal = self.queue[0]
            return peekVal

    def __str__(self):
        return f"QueueShuffling: count={self.count} cap={self.capacity} queue={self.queue[:self.count]}"


def test():
    testQueue = QueueShuffling(3)
    print(testQueue)
    assert testQueue.getCount() == 0
    try:
        testQueue.dequeue()
        assert False
    except ValueError:
        assert True
    testQueue.enqueue(1)
    print(testQueue)
    testQueue.enqueue("2")
    print(testQueue)
    assert testQueue.peek() == 1
    assert testQueue.getCount() == 2
    assert not testQueue.isFull()
    testQueue.enqueue(3)
    print(testQueue)
    assert testQueue.peek() == 1
    assert testQueue.getCount() == 3
    assert testQueue.isFull()
    try:
        testQueue.enqueue(4)
        assert False
    except ValueError:
        assert True
    assert testQueue.dequeue() == 1
    print(testQueue)
    assert testQueue.peek() == "2"
    assert testQueue.getCount() == 2
    assert not testQueue.isFull()
    testQueue.enqueue(4)
    print(testQueue)
    assert testQueue.getCount() == 3
    assert testQueue.dequeue() == "2"
    print(testQueue)
    assert testQueue.peek() == 3
    assert testQueue.dequeue() == 3
    print(testQueue)
    assert testQueue.getCount() == 1
    assert testQueue.dequeue() == 4
    print(testQueue)
    assert testQueue.getCount() == 0
    assert testQueue.isEmpty()
    assert not testQueue.isFull()

if __name__ == "__main__":
    test()