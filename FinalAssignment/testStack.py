import unittest

from DSAStack import DSAStack


class TestStack(unittest.TestCase):
    """
    Test the stack class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """
        Function to test the stack class.
        """
        testStack = DSAStack()
        self.assertTrue(testStack.isEmpty())
        self.assertEqual(testStack.getCount(), 0)
        self.assertRaises(ValueError, lambda: testStack.pop())
        self.assertRaises(ValueError, lambda: testStack.top())

        testStack = DSAStack()
        self.assertEqual(testStack.getCount(), 0)
        testStack.push(1)
        print(testStack)
        testStack.push("2")
        print(testStack)
        self.assertEqual(testStack.top(), "2")
        self.assertEqual(testStack.getCount(), 2)
        testStack.push(3)
        print(testStack)
        self.assertEqual(testStack.top(), 3)
        self.assertEqual(testStack.getCount(), 3)
        self.assertEqual(testStack.pop(), 3)
        print(testStack)
        self.assertEqual(testStack.top(), "2")
        print(testStack)
        self.assertEqual(testStack.getCount(), 2)
        self.assertEqual(testStack.pop(), "2")
        print(testStack)
        self.assertEqual(testStack.pop(), 1)
        print(testStack)
        self.assertEqual(testStack.getCount(), 0)
        self.assertTrue(testStack.isEmpty())


if __name__ == '__main__':
    unittest.main()
