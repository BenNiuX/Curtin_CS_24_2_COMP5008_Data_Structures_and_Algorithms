import copy
import numpy as np

from DSALinkedList import DSALinkedList
from DSAQueue import DSAQueue
from DSAStack import DSAStack


class DSAGraph():
    """
    DSAGraph is used to define a graph data abstract type.
    """

    class _DSAGraphVertex():
        """
        _DSAGraphVertex is used to define a vertex in a graph.
        """

        def __init__(self, label, value):
            self.label = label
            self.value = value
            self.visited = False
            self.list = DSALinkedList()

        def setVisited(self):
            """
            Set the visited flag.
            """
            self.visited = True

        def clearVisited(self):
            """
            Clear the visited flag.
            """
            self.visited = False

        def __str__(self):
            return f"GraphVertex: label={self.label} value={self.value}"

    class _DSAGraphEdge():
        """
        _DSAGraphEdge is used to define an edge in a graph.
        """

        def __init__(self, label1, label2, value):
            self.label1 = label1
            self.label2 = label2
            self.value = value

        def __str__(self):
            return f"GraphEdge: label1={self.label1} label2={self.label2}" \
                   f" value={self.value}"

    DIRECTED = 0
    UNDIRECTED = 1

    def __init__(self, direct=UNDIRECTED):
        self.vertices = DSALinkedList()
        self.edges = DSALinkedList()
        self.isDirect = direct == self.DIRECTED

    def addVertex(self, label, value=0):
        """
        Add a new vertex to the graph.
        """
        if self.hasVertex(label):
            raise ValueError(f"Vertex: {label} already exists")
        vertex = DSAGraph._DSAGraphVertex(label, value)
        self.vertices.insertLast(vertex)

    def deleteVertex(self, label):
        """
        Delete a vertex from the graph.
        """
        delVertex = self.getVertex(label)
        if delVertex:
            self.vertices.remove(delVertex)
            vertexNode = self.vertices.head
            while vertexNode is not None:
                vertexNode.value.list.remove(delVertex)
                vertexNode = vertexNode.next
            edgeNode = self.edges.head
            while edgeNode is not None:
                edge = edgeNode.value
                if edge.label1 == label or edge.label2 == label:
                    self.edges.remove(edge)
                edgeNode = edgeNode.next
        else:
            raise ValueError(f"Vertex: {label} not exists")

    def addEdge(self, label1, label2, value=0):
        """
        Add an new edge to the graph.
        """
        labels = [label1, label2]
        vers = []
        for label in labels:
            if not self.hasVertex(label):
                self.addVertex(label)
            vers.append(self.getVertexNode(label))
        vers[0].value.list.insertLast(vers[1].value)
        edge = DSAGraph._DSAGraphEdge(label1, label2, value)
        self.edges.insertLast(edge)
        if not self.isDirect:
            vers[1].value.list.insertLast(vers[0].value)
            edge = DSAGraph._DSAGraphEdge(label2, label1, value)
            self.edges.insertLast(edge)

    def deleteEdge(self, label1, label2):
        """
        Delete an existing edge from the graph.
        """
        ver1 = self.getVertex(label1)
        ver2 = self.getVertex(label2)
        if ver1 and ver2:
            retNode = ver1.list.remove(ver2)
            if not retNode:
                raise ValueError("Input edge error")
            edgeNode = self.edges.head
            while edgeNode is not None:
                edge = edgeNode.value
                if edge.label1 == label1 and edge.label2 == label2:
                    self.edges.remove(edge)
                edgeNode = edgeNode.next
            self.edges.remove(edge)
            if not self.isDirect:
                ver2.list.remove(ver1)
                edgeNode = self.edges.head
                while edgeNode is not None:
                    edge = edgeNode.value
                    if edge.label1 == label2 and edge.label2 == label1:
                        self.edges.remove(edge)
                    edgeNode = edgeNode.next
        else:
            raise ValueError(f"Vertex {label1} or {label2} wrong")

    def hasVertex(self, label):
        """
        Check if a vertex exists in the graph.
        """
        vertexNode = self.vertices.head
        while vertexNode is not None:
            if vertexNode.value.label == label:
                return True
            vertexNode = vertexNode.next
        return False

    def getVertexCount(self):
        """
        Get the count of vertices in the graph.
        """
        count = 0
        vertexNode = self.vertices.head
        while vertexNode is not None:
            count += 1
            vertexNode = vertexNode.next
        return count

    def getEdgeCount(self):
        """
        Get the count of edges in the graph.
        """
        count = 0
        vertexNode = self.vertices.head
        while vertexNode is not None:
            edgeNode = vertexNode.value.list.head
            while edgeNode is not None:
                count += 1
                edgeNode = edgeNode.next
            vertexNode = vertexNode.next
        if not self.isDirect:
            count = count // 2
        return count

    def getVertex(self, label):
        """
        Get a vertex from the graph using the vertex label.
        """
        node = self.getVertexNode(label)
        if node:
            return node.value
        return None

    def getVertexNode(self, label):
        """
        Get a linked list node of a vertex from the graph
        using the vertex label.
        """
        vertexNode = self.vertices.head
        while vertexNode is not None:
            if vertexNode.value.label == label:
                return vertexNode
            vertexNode = vertexNode.next
        return None

    def getAdjacent(self, label):
        """
        Get a linked list of adjacent vertices of a vertex
        using the vertex label.
        """
        if self.hasVertex(label):
            vertex = self.getVertex(label)
            return vertex.list
        return None

    def isAdjacent(self, label1, label2):
        """
        Use to check if two vertices are adjacent.
        """
        if self.hasVertex(label1) and self.hasVertex(label2):
            adjacents = self.getAdjacent(label1)
            if adjacents:
                itemNode = adjacents.head
                while itemNode is not None:
                    if itemNode.value.label == label2:
                        return True
                    itemNode = itemNode.next
        return False

    def getEdge(self, label1, label2):
        """
        Get an edge from the graph using the vertex labels.
        """
        edgeNode = self.edges.head
        while edgeNode is not None:
            edge = edgeNode.value
            if edge.label1 == label1 and edge.label2 == label2:
                return edge
            edgeNode = edgeNode.next
        return None

    def getDistance(self, label1, label2):
        """
        Get the distance between two vertices.
        """
        retQ = self.getPath(label1, label2)
        if retQ:
            dist = 0
            while not retQ.isEmpty():
                t1 = retQ.dequeue()
                t2 = retQ.dequeue()
                edge = self.getEdge(t1.value.label, t2.value.label)
                print(f"({t1.value.label},{t2.value.label})", end=" ")
                if edge:
                    dist += edge.value
                else:
                    print("Edge not found")
            return dist
        return -1

    def getPath(self, label1, label2):
        """
        Get the path between two vertices.
        """
        if label1 != label2 and self.hasVertex(label1) and self.hasVertex(label2):
            vertexNode1 = self.getVertexNode(label1)
            Ts = DSAStack()
            Q = DSAQueue()
            self.clearVisited()
            vertexNode = vertexNode1
            if vertexNode:
                vertexNode.value.setVisited()
                Q.enqueue(vertexNode)
                print(f"Get Path: from {label1} to {label2} ", end="")
                while not Q.isEmpty():
                    v = Q.dequeue()
                    w = v.value.list.head
                    while w is not None:
                        if not w.value.visited:
                            Ts.push(v)
                            Ts.push(w)
                            w.value.setVisited()
                            if w.value.label == label2:
                                filterS = DSAStack()
                                target = w
                                while not Ts.isEmpty():
                                    t = Ts.pop()
                                    s = Ts.pop()
                                    if target.value.label == t.value.label:
                                        filterS.push(t)
                                        filterS.push(s)
                                        target = s
                                newQ = DSAQueue()
                                while not filterS.isEmpty():
                                    newQ.enqueue(filterS.pop())
                                self.dumpSearch(newQ)
                                return newQ
                            Q.enqueue(w)
                        w = w.next
        return None

    def isPath(self, label1, label2):
        """
        Check if there is a path between two vertices
        using the vertex label.
        """
        path = self.getPath(label1, label2)
        return path is not None

    def getDirectStr(self):
        """
        Get the string for the direction of the graph.
        """
        return "DIRECT" if self.isDirect else "UNDIRECT"

    def displayAsList(self):
        """
        Display the graph as a list.
        """
        vertexNode = self.vertices.head
        print(f"\r\nDisplay as list, {self.getDirectStr()},"
              f" vertex count={self.getVertexCount()},"
              f" edge count={self.getEdgeCount()}")
        while vertexNode is not None:
            print(f"  V: {vertexNode.value.label} [", end=" ")
            edgeNode = vertexNode.value.list.head
            while edgeNode is not None:
                print(edgeNode.value.label, end=" ")
                edgeNode = edgeNode.next
            print("]")
            vertexNode = vertexNode.next

    def displayEdges(self):
        """
        Display all the edges of the graph.
        """
        print(f"\r\nDisplay edges, edge count={self.getEdgeCount()}")
        edgeNode = self.edges.head
        while edgeNode is not None:
            print(f"  E: {edgeNode.value.label1} -> {edgeNode.value.label2}," +
                  f" {edgeNode.value.value}")
            edgeNode = edgeNode.next

    def _getIndexOfLabel(self, label, labelLookup):
        """
        Get the index of a label in the lookup label list.
        """
        length = labelLookup.size
        for i in range(length):
            if labelLookup[i] == label:
                return i
        raise KeyError(f"Can't find label: {label}")

    def displayAsMatrix(self):
        """
        Display the graph as a matrix.
        """
        count = self.getVertexCount()
        labelLookup = np.empty(count, dtype='U')
        adjacencyMatrix = np.zeros((count, count), dtype=int)
        vertexNode = self.vertices.head
        labelIndex = 0
        while vertexNode is not None:
            labelLookup[labelIndex] = vertexNode.value.label
            labelIndex += 1
            vertexNode = vertexNode.next
        vertexNode = self.vertices.head
        while vertexNode is not None:
            i = self._getIndexOfLabel(vertexNode.value.label, labelLookup)
            adjacencyMatrix[i][i] = vertexNode.value.value
            edgeNode = vertexNode.value.list.head
            while edgeNode is not None:
                j = self._getIndexOfLabel(edgeNode.value.label, labelLookup)
                adjacencyMatrix[i][j] += 1
                edgeNode = edgeNode.next
            vertexNode = vertexNode.next
        print(f"\r\nDisplay as matrix, {self.getDirectStr()},"
              f" vertex count={self.getVertexCount()}"
              f" edge count={self.getEdgeCount()}")
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
        """
        Clear the visited flags for all the vertices.
        """
        vertexNode = self.vertices.head
        while (vertexNode is not None):
            vertexNode.value.clearVisited()
            vertexNode = vertexNode.next

    def dumpSearch(self, q):
        """
        Display the search result.
        """
        newQ = copy.deepcopy(q)
        print("{ ", end="")
        while not newQ.isEmpty():
            t1 = newQ.dequeue()
            t2 = newQ.dequeue()
            print(f"({t1.value.label},{t2.value.label})", end=" ")
        print("}")

    def breadthFirstSearch(self):
        """
        Perform a breadth first research on the graph.
        """
        self.sort()
        T = DSAQueue()
        Q = DSAQueue()
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
        """
        Get the 1st unvisited vertex from the adjacent list.
        """
        node = adjList.head
        while node is not None:
            if not node.value.visited:
                return node
            node = node.next
        return None

    def depthFirstSearch(self):
        """
        Perform a depth first research on the graph.
        """
        self.sort()
        T = DSAQueue()
        S = DSAStack()
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
                except ValueError:
                    break
        print("DFS: ", end="")
        self.dumpSearch(T)

    def degree(self):
        raise NotImplementedError("degree not implement")

    def hasValue(self, value):
        """
        Check if the vertex in the graph using the vertex label.
        """
        vertexNode = self.vertices.head
        while vertexNode is not None:
            if vertexNode.value.value == value:
                return True
            vertexNode = vertexNode.next
        return False

    def nextVertex(self):
        raise NotImplementedError("degree not implement")

    def orderList(self, linkList):
        """
        Order the linked list.
        """
        node = linkList.head
        values = []
        while node:
            values.append(node.value)
            node = node.next
        values.sort(key=getLabel)
        orderedList = DSALinkedList()
        for value in values:
            orderedList.insertLast(value)
        return orderedList

    def sort(self):
        """
        Sort the vertices list and edges list.
        """
        self.vertices = self.orderList(self.vertices)
        vertexNode = self.vertices.head
        while vertexNode is not None:
            edgeList = vertexNode.value.list
            vertexNode.value.list = self.orderList(edgeList)
            vertexNode = vertexNode.next


def getLabel(vertexNode):
    """
    Get the label of a vertex node for sorting.
    """
    return vertexNode.label
