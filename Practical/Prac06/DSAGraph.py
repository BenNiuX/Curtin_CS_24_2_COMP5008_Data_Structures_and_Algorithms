import numpy as np

from DSALinkedList import LinkedList
from DSAGraphVertex import GraphVertex
from DSAQueue import Queue
from DSAStack import Stack

class DSAGraph():

    DIRECTED = 0
    UNDIRECTED = 1

    def __init__(self, direct=UNDIRECTED):
        self.vertices = LinkedList()
        self.isDirect = direct == self.DIRECTED

    def addVertex(self, label, value=0):
        if self.hasVertex(label):
            raise ValueError(f"Vertex: {label} already exists")
        vertex = GraphVertex(label, value)
        self.vertices.insertLast(vertex)

    def deleteVertex(self, label):
        delVertex = self.getVertex(label)
        if delVertex:
            self.vertices.remove(delVertex)
            vertexNode = self.vertices.head
            while vertexNode is not None:
                vertexNode.value.list.remove(delVertex)
                vertexNode = vertexNode.next
        else:
            raise ValueError(f"Vertex: {label} not exists")

    def addEdge(self, label1, label2):
        labels = [label1, label2]
        vers = []
        for label in labels:
            if not self.hasVertex(label):
                self.addVertex(label)
            vers.append(self.getVertexNode(label))
        vers[0].value.list.insertLast(vers[1].value)
        if not self.isDirect:
            vers[1].value.list.insertLast(vers[0].value)

    def deleteEdge(self, label1, label2):
        ver1 = self.getVertex(label1)
        ver2 = self.getVertex(label2)
        if ver1 and ver2:
            retNode = ver1.list.remove(ver2)
            if not retNode:
                raise ValueError(f"Input edge error")
            if not self.isDirect:
                ver2.list.remove(ver1)
        else:
            raise ValueError(f"Vertex {label1} or {label2} wrong")

    def hasVertex(self, label):
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            if vertexNode.value.label == label:
                return True
            vertexNode = vertexNode.next
        return False

    def getVertexCount(self):
        count = 0
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            count += 1
            vertexNode = vertexNode.next
        return count

    def getEdgeCount(self):
        count = 0
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            edgeNode = vertexNode.value.list.head
            while (edgeNode is not None):
                count += 1
                edgeNode = edgeNode.next
            vertexNode = vertexNode.next
        if not self.isDirect:
            count = (int) (count / 2)
        return count

    def getVertex(self, label):
        node = self.getVertexNode(label)
        if node:
            return node.value
        return None

    def getVertexNode(self, label):
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            if vertexNode.value.label == label:
                return vertexNode
            vertexNode = vertexNode.next
        return None

    def getAdjacent(self, label):
        if self.hasVertex(label):
            vertex = self.getVertex(label)
            return vertex.list
        return None

    def isAdjacent(self, label1, label2):
        if self.hasVertex(label1) and self.hasVertex(label2):
            adjacents = self.getAdjacent(label1)
            if adjacents:
                itemNode = adjacents.head
                while (itemNode is not None):
                    if itemNode.value.label == label2:
                        return True
                    itemNode = itemNode.next
        return False

    def getDirectStr(self):
        return "DIRECT" if self.isDirect else "UNDIRECT"

    def displayAsList(self):
        vertexNode = self.vertices.head
        print(f"\r\nDisplay as list, {self.getDirectStr()}," +
            f" vertex count={self.getVertexCount()} edge count={self.getEdgeCount()}")
        while (vertexNode is not None):
            print(f"  V: {vertexNode.value.label} [", end=" ")
            edgeNode = vertexNode.value.list.head
            while (edgeNode is not None):
                print(edgeNode.value.label, end=" ")
                edgeNode = edgeNode.next
            print("]")
            vertexNode = vertexNode.next

    def _getIndexOfLabel(self, label, labelLookup):
        length = labelLookup.size
        for i in range(length):
            if labelLookup[i] == label:
                return i
        raise KeyError(f"Can't find label: {label}")

    def displayAsMatrix(self):
        count = self.getVertexCount()
        labelLookup = np.empty(count, dtype='U')
        adjacencyMatrix = np.zeros((count, count), dtype=int)
        vertexNode = self.vertices.head
        labelIndex = 0
        while (vertexNode is not None):
            labelLookup[labelIndex] = vertexNode.value.label
            labelIndex += 1
            vertexNode = vertexNode.next
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            i = self._getIndexOfLabel(vertexNode.value.label, labelLookup)
            adjacencyMatrix[i][i] = vertexNode.value.value
            edgeNode = vertexNode.value.list.head
            while (edgeNode is not None):
                j = self._getIndexOfLabel(edgeNode.value.label, labelLookup)
                adjacencyMatrix[i][j] += 1
                edgeNode = edgeNode.next
            vertexNode = vertexNode.next
        print(f"\r\nDisplay as matrix, {self.getDirectStr()}," \
            f" vertex count={self.getVertexCount()} edge count={self.getEdgeCount()}")
        print("  ", end="")
        for i in range(count):
            print(labelLookup[i], end=" ")
        print()
        for i in range(count):
            print(labelLookup[i], end=" ")
            for j in range(count):
                print(adjacencyMatrix[i][j], end=" ")
            print()

    def clearVisited(self):
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            vertexNode.value.clearVisited()
            vertexNode = vertexNode.next

    def dumpSearch(self, q):
        print("{ ", end="")
        while not q.isEmpty():
            t1 = q.dequeue()
            t2 = q.dequeue()
            print(f"({t1.value.label},{t2.value.label})", end=" ")
        print("}")

    def breadthFirstSearch(self):
        self.sort()
        T = Queue()
        Q = Queue()
        self.clearVisited()
        vertexNode = self.vertices.head
        if vertexNode:
            vertexNode.value.setVisited()
            Q.enqueue(vertexNode)
            while not Q.isEmpty():
                v = Q.dequeue()
                w = v.value.list.head
                while w is not None:
                    if not w.value.visited:
                        T.enqueue(v)
                        T.enqueue(w)
                        w.value.setVisited()
                        Q.enqueue(w)
                    w = w.next
        print("BFS: ", end="")
        self.dumpSearch(T)

    def getUnvisited(self, adjList):
        node = adjList.head
        while node is not None:
            if not node.value.visited:
                return node
            node = node.next
        return None

    def depthFirstSearch(self):
        self.sort()
        T = Queue()
        S = Stack()
        self.clearVisited()
        vertexNode = self.vertices.head
        if vertexNode:
            vertexNode.value.setVisited()
            v = vertexNode
            S.push(v)
            while True:
                w = self.getUnvisited(v.value.list)
                while w is not None:
                    if not w.value.visited:
                        T.enqueue(v)
                        T.enqueue(w)
                        w.value.setVisited()
                        S.push(w)
                        v = w
                        w = self.getUnvisited(v.value.list)
                try:
                    v = S.pop()
                except ValueError as e:
                    break
        print("DFS: ", end="")
        self.dumpSearch(T)

    def degree(self):
        raise NotImplementedError("degree not implement")

    def hasValue(self, value):
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            if vertexNode.value.value == value:
                return True
            vertexNode = vertexNode.next
        return False

    def nextVertex(self):
        raise NotImplementedError("degree not implement")

    def orderList(self, linkList):
        node = linkList.head
        values = []
        while node:
            values.append(node.value)
            node = node.next
        values.sort(key=getLabel)
        orderedList = LinkedList()
        for value in values:
            orderedList.insertLast(value)
        return orderedList

    def sort(self):
        self.vertices = self.orderList(self.vertices)
        vertexNode = self.vertices.head
        while vertexNode is not None:
            edgeList = vertexNode.value.list
            vertexNode.value.list = self.orderList(edgeList)
            vertexNode = vertexNode.next

def getLabel(vertexNode):
    return vertexNode.label

def test():
    graph = DSAGraph()
    graph.displayAsList()
    assert graph.getVertexCount() == 0
    assert graph.getEdgeCount() == 0
    graph.addVertex("A")
    graph.addVertex("B")
    graph.displayAsList()
    assert graph.getVertex("A") is not None
    assert graph.getVertex("B") is not None
    assert graph.getVertexCount() == 2
    graph.addEdge("A", "B")
    graph.displayAsList()
    assert graph.getEdgeCount() == 1
    graph.addEdge("A", "C")
    graph.displayAsList()
    assert graph.getVertexCount() == 3
    assert graph.getEdgeCount() == 2
    assert graph.getVertex("C") is not None
    graph.addEdge("B", "C")
    graph.displayAsList()
    assert graph.getEdgeCount() == 3
    graph.deleteEdge("B", "C")
    graph.displayAsList()
    assert graph.getEdgeCount() == 2
    graph.deleteVertex("C")
    graph.displayAsList()
    assert graph.getVertexCount() == 2
    assert graph.getEdgeCount() == 1
    graph.sort()
    graph.depthFirstSearch()
    graph.breadthFirstSearch()
    pass


OPTIONS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 's', 'q']
OPTION_DESCS = [
    "Add node",
    "Delete node",
    "Add edge",
    "Delete edge",
    "Display as List",
    "Display as Matrix",
    "Breadth First Search",
    "Depth First Search",
    "Sort",
    "Quit"
]

def usage():
    print("\r\n==================================")
    print("Interactive Menu for DSAGraph")
    for i,opt in enumerate(OPTIONS):
        print(f"  ({opt}) {OPTION_DESCS[i]}")
    print("==================================\r\n")

def interactive():
    usage()
    userInput = ''
    userInput = input(f"\r\nCreate a direct graph?: (y/N)")
    isDirect = userInput == 'y'
    graph = DSAGraph(DSAGraph.DIRECTED if isDirect else DSAGraph.UNDIRECTED)
    while userInput != OPTIONS[-1]:
        userInput = input(f"\r\nPlease input options: {', '.join(OPTIONS)}: ")
        if userInput == OPTIONS[0]:
            item = input(f"Please input the node label: ")
            try:
                graph.addVertex(item)
            except ValueError as e:
                print(e)
        elif userInput == OPTIONS[1]:
            item = input(f"Please input the node label: ")
            try:
                graph.deleteVertex(item)
                print(f"Delete node: '{item}' success")
            except ValueError as e:
                print(e)
        elif userInput == OPTIONS[2]:
            item = input(f"Please input the edge like LABEL1 LABEL2: ")
            items = item.split()
            if len(items) == 2:
                graph.addEdge(items[0], items[1])
            else:
                print("Input error")
        elif userInput == OPTIONS[3]:
            item = input(f"Please input the edge like LABEL1 LABEL2: ")
            items = item.split()
            if len(items) == 2:
                try:
                    graph.deleteEdge(items[0], items[1])
                    print(f"Delete edge: {items[0]} {items[1]} success")
                except ValueError as e:
                    print(e)
            else:
                print("Input error")
        elif userInput == OPTIONS[4]:
            graph.displayAsList()
        elif userInput == OPTIONS[5]:
            graph.displayAsMatrix()
        elif userInput == OPTIONS[6]:
            graph.breadthFirstSearch()
        elif userInput == OPTIONS[7]:
            graph.depthFirstSearch()
        elif userInput == OPTIONS[8]:
            graph.sort()
        elif userInput == OPTIONS[9]:
            print("!!!BYE BYE!!!")
        else:
            usage()

if __name__ == "__main__":
    test()
    interactive()