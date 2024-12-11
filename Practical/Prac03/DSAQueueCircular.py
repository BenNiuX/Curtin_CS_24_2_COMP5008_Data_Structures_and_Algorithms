from DSAQueue import Queue

class QueueCircular(Queue):

    def __init__(self, maxCap=Queue.DEFAULT_CAPACITY):
        super().__init__(maxCap)
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.isFull():
            raise ValueError("Queue is full, enqueue fail")
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            self.count += 1

    def dequeue(self):
        peekVal = self.peek()
        self.count -= 1
        self.head = (self.head + 1) % self.capacity
        return peekVal

    def peek(self):
        if self.isEmpty():
            raise ValueError("Queue is empty, peek fail")
        else:
            peekVal = self.queue[self.head]
            return peekVal

    def __str__(self):
        dumpData = []
        if self.count != 0:
            index = self.head
            dumpData.append(self.queue[index])
            index = (index + 1) % self.capacity
            while index != self.tail:
                dumpData.append(self.queue[index])
                index = (index + 1) % self.capacity
        return f"QueueCircular: count={self.count} cap={self.capacity}" \
                 + f" queue={dumpData} head={self.head} tail={self.tail}"


def test():
    testQueue = QueueCircular(3)
    assert testQueue.getCount() == 0
    try:
        testQueue.dequeue()
        assert False
    except ValueError:
        assert True
    
    print(testQueue)
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