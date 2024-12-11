import numpy as np

class Stack():

    DEFAULT_CAPACITY = 100

    def __init__(self, maxCap=DEFAULT_CAPACITY):
        self.stack = np.arange(maxCap, dtype=object)
        self.capacity = self.stack.size
        self.count = 0

    def push(self, value):
        if self.isFull():
            raise ValueError("Stack is full, push fail")
        else:
            self.stack[self.count] = value
            self.count += 1

    def pop(self):
        topVal = self.top()
        self.count -= 1
        return topVal

    def top(self):
        if self.isEmpty():
            raise ValueError("Stack is empty, top fail")
        else:
            topVal = self.stack[self.count - 1]
            return topVal

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def __str__(self):
        return f"Stack: count={self.count} cap={self.capacity} stack={self.stack[:self.count]}"

    def getCount(self):
        return self.count


def test():
    testStack = Stack()
    assert testStack.isEmpty()
    assert not testStack.isFull()
    assert testStack.getCount() == 0
    try:
        testStack.pop()
        assert False
    except ValueError:
        assert True
    try:
        testStack.top()
        assert False
    except ValueError:
        assert True

    testStack = Stack(3)
    assert testStack.getCount() == 0
    testStack.push(1)
    print(testStack)
    testStack.push("2")
    print(testStack)
    assert testStack.top() == "2"
    assert testStack.getCount() == 2
    assert not testStack.isFull()
    testStack.push(3)
    print(testStack)
    assert testStack.top() == 3
    assert testStack.getCount() == 3
    assert testStack.isFull()
    assert testStack.pop() == 3
    print(testStack)
    assert testStack.top() == "2"
    print(testStack)
    assert testStack.getCount() == 2
    assert not testStack.isFull()
    assert testStack.pop() == "2"
    print(testStack)
    assert testStack.pop() == 1
    print(testStack)
    assert testStack.getCount() == 0
    assert testStack.isEmpty()
    assert not testStack.isFull()

if __name__ == "__main__":
    test()