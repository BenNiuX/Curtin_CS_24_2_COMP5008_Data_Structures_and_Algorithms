from DSATreeNode import TreeNode
from DSALinkedList import LinkedList

class BinarySearchTree():

    TRAVERSAL_IN = 0
    TRAVERSAL_PRE = 1
    TRAVERSAL_POST = 2

    def __init__(self):
        self.root = None

    def find(self, key):
        return self._findRec(key, self.root)

    def _findRec(self, key, cur):
        node = None
        if cur == None:
            raise KeyError(f"Key '{key}' not found")
        elif key == cur.key:
            node = cur
        elif key < cur.key:
            node = self._findRec(key, cur.left)
        else:
            node = self._findRec(key, cur.right)
        return node

    def insert(self, key, value):
        node = self._insertRec(key, value, self.root)
        if self.root is None:
            self.root = node
        return node

    def _insertRec(self, key, value, cur):
        updateNode = cur
        if cur == None:
            updateNode = TreeNode(key, value)
        elif key == cur.key:
            raise KeyError(f"Key '{key}' duplicated")
        elif key < cur.key:
            updateNode = self._insertRec(key, value, cur.left)
            if cur.left is None:
                cur.left = updateNode
        else:
            updateNode = self._insertRec(key, value, cur.right)
            if cur.right is None:
                cur.right = updateNode
        return updateNode

    def _promoteSuccessor(self, cur):
        successor = cur
        if cur.left is not None:
            successor = self._promoteSuccessor(cur.left)
            if successor == cur.left:
                cur.left = successor.right
        return successor

    def _deleteNode(self, key, delete):
        updateNode = None
        if delete.left is None and delete.right is None:
            updateNode = None
        elif delete.left is not None and delete.right is None:
            updateNode = delete.left
        elif delete.left is None and delete.right is not None:
            updateNode = delete.right
        else:
            updateNode = self._promoteSuccessor(delete.right)
            if updateNode != delete.right:
                updateNode.right = delete.right
            updateNode.left = delete.left
        return updateNode

    def _deleteRec(self, key, cur):
        updateNode = cur
        if cur is None:
            raise KeyError("Node is none")
        elif key == cur.key:
            updateNode = self._deleteNode(key, cur)
        elif key < cur.key:
            updateNode = self._deleteRec(key, cur.left)
            if cur.left is not None and key == cur.left.key:
                cur.left = updateNode
        else:
            updateNode = self._deleteRec(key, cur.right)
            if cur.right is not None and key == cur.right.key:
                cur.right = updateNode
        return updateNode

    def delete(self, key):
        updateNode = self._deleteRec(key, self.root)
        if self.root.key == key:
            self.root = updateNode

    def _minRec(self, cur):
        key = ""
        if cur is None:
            raise KeyError("Node is none")
        if cur.left is not None:
            key = self._minRec(cur.left)
        else:
            key = cur.key
        return key

    def _minIter(self):
        key = ""
        cur = self.root
        if cur is None:
            raise KeyError("Node is none")
        while cur.left is not None:
            cur = cur.left
        key = cur.key
        return key

    def min(self):
        return self._minIter()

    def _maxRec(self, cur):
        key = ""
        if cur is None:
            raise KeyError("Node is none")
        if cur.right is not None:
            key = self._maxRec(cur.right)
        else:
            key = cur.key
        return key

    def _maxIter(self):
        key = ""
        cur = self.root
        if cur is None:
            raise KeyError("Node is none")
        while cur.right is not None:
            cur = cur.right
        key = cur.key
        return key

    def max(self):
        return self._maxIter()

    def _heightRec(self, cur):
        htSoFar = -1
        if cur is None:
            htSoFar = -1
        else:
            leftHt = self._heightRec(cur.left)
            rightHt = self._heightRec(cur.right)
            if leftHt > rightHt:
                htSoFar = leftHt + 1
            else:
                htSoFar = rightHt + 1
        return htSoFar

    def height(self):
        return self._heightRec(self.root)

    def nodeBlanceScore(self, node, treeHt):
        if node is None or treeHt == 0:
            return 1
        leftHt = self._heightRec(node.left)
        rightHt = self._heightRec(node.right)
        imbalance = abs(leftHt - rightHt)
        sc = 1 - (imbalance / treeHt)
        return sc

    def averageBalance(self, node, treeHt):
        if node is None:
            return 0, 0
        leftSc, leftCn = self.averageBalance(node.left, treeHt)
        rightSc, rightCn = self.averageBalance(node.right, treeHt)
        currSc = self.nodeBlanceScore(node, treeHt)
        totalSc = leftSc + rightSc + currSc
        totalCn = leftCn + rightCn + 1
        return totalSc, totalCn

    def balance(self):
        treeHt = self.height()
        totalSc, totalCn = self.averageBalance(self.root, treeHt)
        if totalCn == 0:
            return 100
        else:
            return (totalSc / totalCn) * 100

    def display(self):
        inorderList = self.inorder()
        preorderList = self.preorder()
        postorderList = self.postorder()
        ret = "inorder{"
        try:
            while True:
                item = inorderList.removeFirst()
                ret += f"\r\n-{item}"
        except ValueError:
            ret += "\r\n}"
        ret += "\r\npreorder{"
        try:
            while True:
                item = preorderList.removeFirst()
                ret += f"\r\n-{item}"
        except ValueError:
            ret += "\r\n}"
        ret += "\r\npost{"
        try:
            while True:
                item = postorderList.removeFirst()
                ret += f"\r\n-{item}"
        except ValueError:
            ret += "\r\n}"
        ret += f"\r\nmin={self.min()} max={self.max()} height={self.height()} bal={self.balance()}"
        print(ret)

    def _traversalRec(self, mode, cur, orderList):
        if cur is not None:
            if mode == self.TRAVERSAL_PRE:
                orderList.insertLast(cur)
            self._traversalRec(mode, cur.left, orderList)
            if mode == self.TRAVERSAL_IN:
                orderList.insertLast(cur)
            self._traversalRec(mode, cur.right, orderList)
            if mode == self.TRAVERSAL_POST:
                orderList.insertLast(cur)

    def inorder(self):
        orderList = LinkedList()
        self._traversalRec(self.TRAVERSAL_IN, self.root, orderList)
        return orderList

    def preorder(self):
        orderList = LinkedList()
        self._traversalRec(self.TRAVERSAL_PRE, self.root, orderList)
        return orderList

    def postorder(self):
        orderList = LinkedList()
        self._traversalRec(self.TRAVERSAL_POST, self.root, orderList)
        return orderList

    def __str__(self):
        inorderList = self.inorder()
        ret = "inorder{"
        try:
            ret += f"\r\nmin: {self.min()}"
            ret += f"\r\nmax: {self.max()}"
            ret += f"\r\nheight: {self.height()}"
            ret += f"\r\nbalance: {self.balance()}"
        except KeyError:
            pass
        try:
            while True:
                item = inorderList.removeFirst()
                ret += f"\r\n--{item}"
        except ValueError:
            ret += "\r\n}"
        return ret


def test():
    testBinarySearchTree = BinarySearchTree()
    print(testBinarySearchTree)
    try:
        print(testBinarySearchTree.min())
        assert False
    except KeyError:
        assert True
    try:
        print(testBinarySearchTree.max())
        assert False
    except KeyError:
        assert True
    assert testBinarySearchTree.height() == -1
    try:
        testBinarySearchTree.find(3)
        assert False
    except KeyError as e:
        print(e)
        assert True
    assert testBinarySearchTree.root is None
    node = testBinarySearchTree.insert(3, 3)
    print(testBinarySearchTree)
    print(testBinarySearchTree.balance())
    assert node is not None
    assert testBinarySearchTree.root is not None
    assert testBinarySearchTree.root.value == 3
    assert testBinarySearchTree.root.key == 3
    try:
        findNode = testBinarySearchTree.find(3)
        assert findNode.value == 3
        assert True
    except KeyError as e:
        print(e)
        assert False
    assert testBinarySearchTree.root is not None
    testBinarySearchTree.insert(1, 1)
    print(testBinarySearchTree)
    testBinarySearchTree.insert(2, 2)
    print(testBinarySearchTree)
    testBinarySearchTree.insert(5, 5)
    print(testBinarySearchTree)
    testBinarySearchTree.insert(4, 4)
    print(testBinarySearchTree)
    try:
        testBinarySearchTree.insert(1, 2)
        assert False
    except KeyError as e:
        print(e)
        assert True

    testBinarySearchTree = BinarySearchTree()
    testBinarySearchTree.insert(4, 4)
    testBinarySearchTree.insert(2, 2)
    testBinarySearchTree.insert(6, 6)
    testBinarySearchTree.insert(1, 1)
    testBinarySearchTree.insert(3, 3)
    testBinarySearchTree.insert(5, 5)
    testBinarySearchTree.insert(7, 7)
    assert testBinarySearchTree.min() == 1
    assert testBinarySearchTree._minIter() == 1
    assert testBinarySearchTree._minRec(testBinarySearchTree.root) == 1
    assert testBinarySearchTree.max() == 7
    assert testBinarySearchTree._maxIter() == 7
    assert testBinarySearchTree._maxRec(testBinarySearchTree.root) == 7
    assert testBinarySearchTree.height() == 2
    print(testBinarySearchTree)

    testBinarySearchTree = BinarySearchTree()
    testBinarySearchTree.insert(50, 50)
    testBinarySearchTree.insert(16, 16)
    testBinarySearchTree.insert(7, 7)
    testBinarySearchTree.insert(89, 89)
    testBinarySearchTree.insert(70, 70)
    testBinarySearchTree.insert(45, 45)
    testBinarySearchTree.insert(10, 10)
    testBinarySearchTree.insert(66, 66)
    testBinarySearchTree.insert(95, 95)
    print(testBinarySearchTree)
    testBinarySearchTree.display()

def testDel():
    testBinarySearchTree = BinarySearchTree()
    testBinarySearchTree.insert(2, 2)
    assert testBinarySearchTree.root.value == 2
    testBinarySearchTree.delete(2)
    assert testBinarySearchTree.root is None
    testBinarySearchTree.insert(2, 2)
    assert testBinarySearchTree.root.value == 2
    testBinarySearchTree.insert(1, 1)
    testBinarySearchTree.insert(3, 3)
    testBinarySearchTree.delete(2)
    assert testBinarySearchTree.root.value == 3
    assert testBinarySearchTree.root.left.value == 1
    assert testBinarySearchTree.root.right is None
    testBinarySearchTree.delete(1)
    assert testBinarySearchTree.root.value == 3
    assert testBinarySearchTree.root.left is None
    assert testBinarySearchTree.root.right is None
    testBinarySearchTree.delete(3)
    assert testBinarySearchTree.root is None

    testBinarySearchTree = BinarySearchTree()
    testBinarySearchTree.insert(10, 10)
    testBinarySearchTree.insert(3, 3)
    testBinarySearchTree.insert(16, 16)
    testBinarySearchTree.insert(1, 1)
    testBinarySearchTree.insert(7, 7)
    testBinarySearchTree.insert(12, 12)
    testBinarySearchTree.insert(20, 20)
    testBinarySearchTree.insert(4, 4)
    testBinarySearchTree.insert(9, 9)
    testBinarySearchTree.insert(14, 14)
    testBinarySearchTree.insert(19, 19)
    testBinarySearchTree.insert(26, 26)
    orderList = testBinarySearchTree.inorder()
    dumpOrderList(orderList)
    testBinarySearchTree.delete(1)
    orderList = testBinarySearchTree.inorder()
    dumpOrderList(orderList)
    testNode = testBinarySearchTree.find(3)
    assert testNode is not None
    assert testNode.left is None
    assert testNode.right is not None and testNode.right.value == 7
    testBinarySearchTree.delete(3)
    orderList = testBinarySearchTree.inorder()
    dumpOrderList(orderList)
    assert testBinarySearchTree.root.value == 10
    assert testBinarySearchTree.root.left is not None and testBinarySearchTree.root.left.value == 7
    assert testBinarySearchTree.find(7)
    testBinarySearchTree.delete(16)
    orderList = testBinarySearchTree.inorder()
    dumpOrderList(orderList)
    assert testBinarySearchTree.root.right.value == 19
    testNode = testBinarySearchTree.find(19)
    assert testNode.left.value == 12
    assert testNode.right.value == 20
    testNode = testBinarySearchTree.find(20)
    assert testNode.left is None
    assert testNode.right.value == 26

def testOrder():
    testBinarySearchTree = BinarySearchTree()
    testBinarySearchTree.insert('D', 'D')
    testBinarySearchTree.insert('B', 'B')
    testBinarySearchTree.insert('F', 'F')
    testBinarySearchTree.insert('A', 'A')
    testBinarySearchTree.insert('C', 'C')
    testBinarySearchTree.insert('E', 'E')
    testBinarySearchTree.insert('G', 'G')
    orderList = testBinarySearchTree.preorder()
    golden = 'DBACFEG'
    for i in golden:
        assert orderList.removeFirst().value == i
    orderList = testBinarySearchTree.inorder()
    golden = 'ABCDEFG'
    for i in golden:
        assert orderList.removeFirst().value == i
    orderList = testBinarySearchTree.postorder()
    golden = 'ACBEGFD'
    for i in golden:
        assert orderList.removeFirst().value == i

OPTIONS = ['a', 'b', 'c', 'd1', 'd2', 'd3', 'd', 'f', 'min', 'max', 'height', 'balance', 'q']
OPTION_DESCS = [
    "Add node",
    "Delete node",
    "Clear the tree",
    "Display the tree: inorder",
    "Display the tree: preorder",
    "Display the tree: postorder",
    "Display the tree",
    "Find in the tree",
    "Return min of the tree",
    "Return max of the tree",
    "Return height of the tree",
    "Return balance of the tree",
    "Quit"
]

def usage():
    print("\r\n==================================")
    print("Interactive Menu for DSABinarySearchTree")
    for i,opt in enumerate(OPTIONS):
        print(f"  ({opt}) {OPTION_DESCS[i]}")
    print("==================================\r\n")

def dumpOrderList(orderList):
    cn = 0
    try:
        while True:
            item = orderList.removeFirst()
            print(f"-{item}")
            cn += 1
    except ValueError:
        print(f"Total count: {cn}")

def interactive():
    usage()
    userInput = ''
    bst = BinarySearchTree()
    while userInput != 'q':
        userInput = input(f"\r\nPlease input options: {', '.join(OPTIONS)}: ")
        if userInput == OPTIONS[0]:
            item = input(f"Please input the key(int) and value: ")
            items = item.split()
            if len(items) == 2:
                try:
                    bst.insert(int(items[0]), items[1])
                except KeyError as e:
                    print(e)
            else:
                print("Input error")
        elif userInput == OPTIONS[1]:
            key = input(f"Please input key(int) to be deleted: ")
            try:
                bst.delete(int(key))
                print(f"Delete key: '{key}' success")
            except KeyError as e:
                print(e)
        elif userInput == OPTIONS[2]:
            bst = BinarySearchTree()
        elif userInput == OPTIONS[3]:
            orderList = bst.inorder()
            dumpOrderList(orderList)
        elif userInput == OPTIONS[4]:
            orderList = bst.preorder()
            dumpOrderList(orderList)
        elif userInput == OPTIONS[5]:
            orderList = bst.postorder()
            dumpOrderList(orderList)
        elif userInput == OPTIONS[6]:
            bst.display()
        elif userInput == OPTIONS[7]:
            key = input(f"Please input the key(int) to find: ")
            try:
                value = bst.find(int(key))
                print(f"Find value: '{value}' with key: '{key}'")
            except KeyError as e:
                print(e)
        elif userInput == OPTIONS[8]:
            print(bst.min())
        elif userInput == OPTIONS[9]:
            print(bst.max())
        elif userInput == OPTIONS[10]:
            print(bst.height())
        elif userInput == OPTIONS[11]:
            print(bst.balance())
        elif userInput == OPTIONS[12]:
            print("!!!BYE BYE!!!")
        else:
            usage()


if __name__ == "__main__":
    test()
    testDel()
    testOrder()
    interactive()