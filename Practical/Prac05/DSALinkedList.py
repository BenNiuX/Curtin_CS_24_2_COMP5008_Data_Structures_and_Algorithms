# Cite from Prac04

class LinkedList():

    class _LinkedNode:

        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

        def state(self):
            return f"Not_None? next={self.next is not None} prev={self.prev is not None}"

        def __str__(self):
            return f"LinkedNode: value={self.value} {self.state()}"

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, value):
        newNd = LinkedList._LinkedNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            # if self.head.next is None and self.tail.prev is None:
            #     self.tail.prev = newNd
            self.head.prev = newNd
            newNd.next = self.head
            newNd.prev = None
            self.head = newNd

    def insertLast(self, value):
        newNd = LinkedList._LinkedNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            # if self.head.next is None and self.tail.prev is None:
            #     self.head.next = newNd
            self.tail.next = newNd
            newNd.prev = self.tail
            newNd.next = None
            self.tail = newNd

    def insertBefore(self, valueToFind):
        raise NotImplementedError("Not implemented")

    def removeFirst(self):
        retVal = self.peekFirst()
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return retVal

    def removeLast(self):
        retVal = self.peekLast()
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return retVal

    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("LinkedList is empty")
        else:
            return self.head.value

    def peekLast(self):
        if self.isEmpty():
            raise ValueError("LinkedList is empty")
        else:
            return self.tail.value

    def find(self, valueToFind):
        raise NotImplementedError("Not implemented")

    def remove(self, valueToFind):
        raise NotImplementedError("Not implemented")

    def peek(self, valueToFind):
        raise NotImplementedError("Not implemented")

    def isEmpty(self):
        return self.head is None

    def dump(self):
        retStr = "{"
        currNd = self.head
        while currNd is not None:
            retStr = f"{retStr} {currNd.value}"
            currNd = currNd.next
        retStr += " }"
        return retStr

    def __str__(self):
        retStr = f"LinkedList: head={self.head}, tail={self.tail}, empty={self.isEmpty()}"
        currNd = self.head
        while currNd is not None:
            retStr = f"{retStr}\r\n  {currNd}"
            currNd = currNd.next
        return retStr

def test():
    testLinkedList = LinkedList()
    assert testLinkedList.isEmpty()
    print(testLinkedList)
    try:
        testLinkedList.removeFirst()
        assert False
    except ValueError:
        assert True
    try:
        testLinkedList.removeLast()
        assert False
    except ValueError:
        assert True
    try:
        testLinkedList.peekFirst()
        assert False
    except ValueError:
        assert True
    try:
        testLinkedList.peekLast()
        assert False
    except ValueError:
        assert True
    testLinkedList.insertFirst(1)
    print(testLinkedList)
    assert not testLinkedList.isEmpty()
    assert testLinkedList.peekFirst() == 1
    assert testLinkedList.peekLast() == 1
    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is None
    assert testLinkedList.tail.prev is None
    assert testLinkedList.tail.next is None
    testLinkedList.insertLast(2)
    print(testLinkedList)
    assert testLinkedList.peekFirst() == 1
    assert testLinkedList.peekLast() == 2
    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is not None
    assert testLinkedList.tail.prev is not None
    assert testLinkedList.tail.next is None
    assert testLinkedList.removeLast() == 2
    print(testLinkedList)

    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is None
    assert testLinkedList.tail.prev is None
    assert testLinkedList.tail.next is None
    assert testLinkedList.peekLast() == 1
    testLinkedList.insertLast(3)
    print(testLinkedList)
    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is not None
    assert testLinkedList.tail.prev is not None
    assert testLinkedList.tail.next is None
    assert testLinkedList.peekFirst() == 1
    assert testLinkedList.peekLast() == 3
    assert testLinkedList.peekFirst() == 1
    testLinkedList.insertLast(4)
    print(testLinkedList)
    assert testLinkedList.removeFirst() == 1
    print(testLinkedList)
    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is not None
    assert testLinkedList.tail.prev is not None
    assert testLinkedList.tail.next is None
    assert not testLinkedList.isEmpty()
    assert testLinkedList.removeFirst() == 3
    print(testLinkedList)
    assert testLinkedList.head.prev is None
    assert testLinkedList.head.next is None
    assert testLinkedList.tail.prev is None
    assert testLinkedList.tail.next is None
    assert not testLinkedList.isEmpty()
    assert testLinkedList.removeFirst() == 4
    print(testLinkedList)
    assert testLinkedList.isEmpty()
    testLinkedList.insertFirst(1)
    print(testLinkedList)
    testLinkedList.insertFirst(2)
    print(testLinkedList)
    testLinkedList.insertFirst(3)
    print(testLinkedList)

OPTIONS = ['a1', 'a2', 'b1', 'b2', 'c', 'd', 'q']
OPTION_DESCS = [
    "InsertFirst on the list",
    "InsertLast on the list",
    "RemoveFirst on the list",
    "RemoveLast on the list",
    "Clear the list",
    "Display the list",
    "Quit"
]

def usage():
    print("\r\n==================================")
    print("Interactive Menu for DSALinkedList")
    for i,opt in enumerate(OPTIONS):
        print(f"  ({opt}) {OPTION_DESCS[i]}")
    print("==================================\r\n")

def interactive():
    usage()
    userInput = ''
    linkList = LinkedList()
    while userInput != 'q':
        userInput = input(f"\r\nPlease input options: {', '.join(OPTIONS)}: ")
        if userInput == OPTIONS[0]:
            item = input(f"Please input item: ")
            try:
                linkList.insertFirst(item)
            except ValueError as e:
                print(e)
            print(linkList.dump())
        elif userInput == OPTIONS[1]:
            item = input(f"Please input item: ")
            try:
                linkList.insertLast(item)
            except ValueError as e:
                print(e)
            print(linkList.dump())
        elif userInput == OPTIONS[2]:
            try:
                item = linkList.removeFirst()
                print(f"Remove item: {item}")
            except ValueError as e:
                print(e)
            print(linkList.dump())
        elif userInput == OPTIONS[3]:
            try:
                item = linkList.removeLast()
                print(f"Remove item: {item}")
            except ValueError as e:
                print(e)
            print(linkList.dump())
        elif userInput == OPTIONS[4]:
            print(f"!!!Clear list!!!")
            linkList = LinkedList()
            print(linkList.dump())
        elif userInput == OPTIONS[5]:
            print(linkList.dump())
        elif userInput == OPTIONS[6]:
            print("!!!BYE BYE!!!")
        else:
            usage()


if __name__ == "__main__":
    test()
    interactive()