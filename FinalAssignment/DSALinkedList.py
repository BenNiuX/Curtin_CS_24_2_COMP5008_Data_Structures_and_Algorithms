class DSALinkedList():
    """
    DSALinkedList is used to define a linked list data abstract type.
    """

    class _DSALinkedNode:
        """
        _DSALinkedNode is used to define a node used in a linked list.
        """

        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

        def state(self):
            """
            Return the state string of the node.
            """
            return f"Not_None? next={self.next is not None}" \
                   f" prev={self.prev is not None}"

        def __str__(self):
            return f"LinkedNode: value={self.value} {self.state()}"

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, value):
        """
        Insert a new value at the first position of the linked list.
        """
        newNd = DSALinkedList._DSALinkedNode(value)
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
        """
        Insert a new value at the last position of the linked list.
        """
        newNd = DSALinkedList._DSALinkedNode(value)
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
        """
        Remove the first node from the linked list.
        """
        retVal = self.peekFirst()
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return retVal

    def removeLast(self):
        """
        Remove the last node from the linked list.
        """
        retVal = self.peekLast()
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return retVal

    def peekFirst(self):
        """
        Return the value of the first node in the linked list.
        """
        if self.isEmpty():
            raise ValueError("LinkedList is empty")
        else:
            return self.head.value

    def peekLast(self):
        """
        Return the value of the last node in the linked list.
        """
        if self.isEmpty():
            raise ValueError("LinkedList is empty")
        else:
            return self.tail.value

    def find(self, valueToFind):
        """
        Find the node with the input value in the linked list.
        """
        node = self.head
        while node:
            if valueToFind == node.value:
                return node
            node = node.next

    def remove(self, valueToFind):
        """
        Remove the node with the input value from the linked list.
        """
        head = self.head
        tail = self.tail
        retNode = None
        if self.head is None:
            return retNode
        if valueToFind == head.value:
            retNode = head
            self.head = head.next
            if self.head:
                self.head.prev = None
        elif valueToFind == tail.value:
            retNode = tail
            self.tail = tail.prev
            if self.tail:
                self.tail.next = None
        else:
            prevNode = self.head
            currNode = self.head.next
            while currNode:
                if valueToFind == currNode.value:
                    prevNode.next = currNode.next
                    currNode.next.prev = prevNode
                    retNode = currNode
                    break
                prevNode = currNode
                currNode = currNode.next
        return retNode

    def peek(self, valueToFind):
        raise NotImplementedError("Not implemented")

    def isEmpty(self):
        """
        Check if the linked list is empty.
        """
        return self.head is None

    def dump(self):
        """
        Dump the linked list.
        """
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
