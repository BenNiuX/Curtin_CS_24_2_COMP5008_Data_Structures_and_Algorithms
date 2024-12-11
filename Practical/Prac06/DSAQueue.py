# Cite from DSA Prac03

from DSALinkedList import LinkedList

class Queue():

    def __init__(self):
        self.queue = LinkedList()
        self.count = 0

    def enqueue(self, value):
        self.queue.insertLast(value)
        self.count += 1

    def dequeue(self):
        # self.queue.peekFirst()
        retVal = self.queue.removeFirst()
        self.count -= 1
        return retVal

    def peek(self):
        return self.queue.peekFirst()

    def isEmpty(self):
        return self.queue.isEmpty()

    def getCount(self):
        return self.count

    def __str__(self):
        return f"Queue: count={self.count} queue={self.queue}"


def test():
    testQueue = Queue()
    assert testQueue.isEmpty()
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
    testQueue.enqueue(3)
    print(testQueue)
    assert testQueue.peek() == 1
    assert testQueue.getCount() == 3
    testQueue.enqueue(4)
    assert testQueue.dequeue() == 1

    print(testQueue)
    assert testQueue.peek() == "2"
    assert testQueue.getCount() == 3
    testQueue.enqueue(5)

    print(testQueue)
    assert testQueue.getCount() == 4
    assert testQueue.dequeue() == "2"

    print(testQueue)
    assert testQueue.peek() == 3
    assert testQueue.dequeue() == 3

    print(testQueue)
    assert testQueue.getCount() == 2
    assert testQueue.dequeue() == 4

    print(testQueue)
    assert testQueue.getCount() == 1
    assert testQueue.dequeue() == 5
    assert testQueue.isEmpty()


if __name__ == "__main__":
    test()