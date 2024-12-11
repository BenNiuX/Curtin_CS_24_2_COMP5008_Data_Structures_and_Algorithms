import numpy as np

class Queue():

    DEFAULT_CAPACITY = 100

    def __init__(self, maxCap=DEFAULT_CAPACITY):
        self.queue = np.arange(maxCap, dtype=object)
        self.capacity = self.queue.size
        self.count = 0

    def enqueue(self, value):
        raise NotImplementedError("Should be implemented by child class")

    def dequeue(self):
        raise NotImplementedError("Should be implemented by child class")

    def peek(self):
        raise NotImplementedError("Should be implemented by child class")

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def getCount(self):
        return self.count


def test():
    testQueue = Queue()
    assert testQueue.isEmpty()
    assert not testQueue.isFull()
    assert testQueue.getCount() == 0
    try:
        testQueue.enqueue(1)
        assert False
    except NotImplementedError:
        assert True
    try:
        testQueue.dequeue()
        assert False
    except NotImplementedError:
        assert True
    try:
        testQueue.peek()
        assert False
    except NotImplementedError:
        assert True

if __name__ == "__main__":
    test()