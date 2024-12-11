
class TreeNode():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode: key={self.key} value={self.value}" \
                f" left={self.left.key if self.left else None}" \
                f" right={self.right.key if self.right else None}"


def test():
    testTreeNode = TreeNode(1, 1)
    print(testTreeNode)
    assert testTreeNode is not None
    assert testTreeNode.left is None
    assert testTreeNode.right is None
    assert testTreeNode.key == 1
    assert testTreeNode.value == 1
    testTreeNode2 = TreeNode("2", "2")
    print(testTreeNode2)
    assert testTreeNode2.key == "2"
    assert testTreeNode2.value == "2"
    testTreeNode.left = testTreeNode2
    print(testTreeNode)

if __name__ == "__main__":
    test()