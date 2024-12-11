from DSALinkedList import DSALinkedList


class DSAQueue():
    """
    DSAQueue is used to define a queue data abstract type.
    """

    def __init__(self):
        self.queue = DSALinkedList()
        self.count = 0

    def enqueue(self, value):
        """
        Enqueue a new value into the queue.
        """
        self.queue.insertLast(value)
        self.count += 1

    def dequeue(self):
        """
        Dequeue a value from the queue.
        """
        # self.queue.peekFirst()
        retVal = self.queue.removeFirst()
        self.count -= 1
        return retVal

    def peek(self):
        """
        Peek the first value in the queue.
        """
        return self.queue.peekFirst()

    def isEmpty(self):
        """
        Check if the queue is empty.
        """
        return self.queue.isEmpty()

    def getCount(self):
        """
        Get the item count of the queue.
        """
        return self.count

    def __str__(self):
        return f"Queue: count={self.count} queue={self.queue}"
