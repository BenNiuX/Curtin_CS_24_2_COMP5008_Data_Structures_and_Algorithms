# Cite from DSA Prac03

from DSALinkedList import LinkedList

class Stack():

    def __init__(self):
        self.stack = LinkedList()
        self.count = 0

    def push(self, value):
        self.stack.insertFirst(value)
        self.count += 1

    def pop(self):
        # self.stack.peekFirst()
        topVal = self.stack.removeFirst()
        self.count -= 1
        return topVal

    def top(self):
        return self.stack.peekFirst()

    def isEmpty(self):
        return self.stack.isEmpty()

    def __str__(self):
        return f"Stack: count={self.count} stack={self.stack}"

    def getCount(self):
        return self.count


def test():
    testStack = Stack()
    assert testStack.isEmpty()
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

    testStack = Stack()
    assert testStack.getCount() == 0
    testStack.push(1)
    print(testStack)
    testStack.push("2")
    print(testStack)
    assert testStack.top() == "2"
    assert testStack.getCount() == 2
    testStack.push(3)
    print(testStack)
    assert testStack.top() == 3
    assert testStack.getCount() == 3
    assert testStack.pop() == 3
    print(testStack)
    assert testStack.top() == "2"
    print(testStack)
    assert testStack.getCount() == 2
    assert testStack.pop() == "2"
    print(testStack)
    assert testStack.pop() == 1
    print(testStack)
    assert testStack.getCount() == 0
    assert testStack.isEmpty()

if __name__ == "__main__":
    test()