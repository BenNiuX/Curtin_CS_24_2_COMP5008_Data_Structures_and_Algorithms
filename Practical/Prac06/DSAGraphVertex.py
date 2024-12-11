from DSALinkedList import LinkedList

class GraphVertex():

    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.visited = False
        self.list = LinkedList()
        pass

    def getAdjacent(self, label):
        pass

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def __str__(self):
        return f"GraphVertex: label={self.label} value={self.value}"


def test():
    pass

if __name__ == "__main__":
    test()