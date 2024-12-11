from DSALinkedList import DSALinkedList


class DSAStack():
    """
    DSAStack is used to define a stack data abstract type.
    """

    def __init__(self):
        self.stack = DSALinkedList()
        self.count = 0

    def push(self, value):
        """
        Push a new value into the stack.
        """
        self.stack.insertFirst(value)
        self.count += 1

    def pop(self):
        """
        Pop a value from the stack.
        """
        # self.stack.peekFirst()
        topVal = self.stack.removeFirst()
        self.count -= 1
        return topVal

    def top(self):
        """
        Peek the top value in the stack.
        """
        return self.stack.peekFirst()

    def isEmpty(self):
        """
        Check if the stack is empty.
        """
        return self.stack.isEmpty()

    def getCount(self):
        """
        Get the item count of the stack.
        """
        return self.count

    def __str__(self):
        return f"Stack: count={self.count} stack={self.stack}"
