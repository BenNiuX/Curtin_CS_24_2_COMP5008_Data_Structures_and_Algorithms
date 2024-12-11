import unittest

from DSALinkedList import DSALinkedList


class TestLinkedList(unittest.TestCase):
    """
    Test the linked list class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """
        Function to test the linked list class.
        """
        testLinkedList = DSALinkedList()
        self.assertTrue(testLinkedList.isEmpty())
        print(testLinkedList)
        self.assertRaises(ValueError, lambda: testLinkedList.removeFirst())
        self.assertRaises(ValueError, lambda: testLinkedList.removeLast())
        self.assertRaises(ValueError, lambda: testLinkedList.peekFirst())
        self.assertRaises(ValueError, lambda: testLinkedList.peekLast())
        testLinkedList.insertFirst(1)
        print(testLinkedList)
        self.assertFalse(testLinkedList.isEmpty())
        self.assertEqual(testLinkedList.peekFirst(), 1)
        self.assertEqual(testLinkedList.peekLast(), 1)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNone(testLinkedList.head.next)
        self.assertIsNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        testLinkedList.insertLast(2)
        print(testLinkedList)
        self.assertEqual(testLinkedList.peekFirst(), 1)
        self.assertEqual(testLinkedList.peekLast(), 2)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNotNone(testLinkedList.head.next)
        self.assertIsNotNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        self.assertEqual(testLinkedList.removeLast(), 2)
        print(testLinkedList)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNone(testLinkedList.head.next)
        self.assertIsNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        self.assertEqual(testLinkedList.peekLast(), 1)
        testLinkedList.insertLast(3)
        print(testLinkedList)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNotNone(testLinkedList.head.next)
        self.assertIsNotNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        self.assertEqual(testLinkedList.peekFirst(), 1)
        self.assertEqual(testLinkedList.peekLast(), 3)
        self.assertEqual(testLinkedList.peekFirst(), 1)
        testLinkedList.insertLast(4)
        print(testLinkedList)
        self.assertEqual(testLinkedList.removeFirst(), 1)
        print(testLinkedList)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNotNone(testLinkedList.head.next)
        self.assertIsNotNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        self.assertFalse(testLinkedList.isEmpty())
        self.assertEqual(testLinkedList.removeFirst(), 3)
        print(testLinkedList)
        self.assertIsNone(testLinkedList.head.prev)
        self.assertIsNone(testLinkedList.head.next)
        self.assertIsNone(testLinkedList.tail.prev)
        self.assertIsNone(testLinkedList.tail.next)
        self.assertFalse(testLinkedList.isEmpty())
        self.assertEqual(testLinkedList.removeFirst(), 4)
        print(testLinkedList)
        self.assertTrue(testLinkedList.isEmpty())
        testLinkedList.insertFirst(1)
        print(testLinkedList)
        testLinkedList.insertFirst(2)
        print(testLinkedList)
        testLinkedList.insertFirst(3)
        print(testLinkedList)


if __name__ == '__main__':
    unittest.main()
