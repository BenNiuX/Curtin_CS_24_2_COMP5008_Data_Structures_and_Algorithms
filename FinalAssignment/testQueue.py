import unittest

from DSAQueue import DSAQueue


class TestQueue(unittest.TestCase):
    """
    Test the queue class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """
        Function to test the queue class.
        """
        testQueue = DSAQueue()
        self.assertTrue(testQueue.isEmpty())
        self.assertEqual(testQueue.getCount(), 0)
        self.assertRaises(ValueError, lambda: testQueue.dequeue())
        print(testQueue)
        testQueue.enqueue(1)
        print(testQueue)
        testQueue.enqueue("2")
        print(testQueue)
        self.assertEqual(testQueue.peek(), 1)
        self.assertEqual(testQueue.getCount(), 2)
        testQueue.enqueue(3)
        print(testQueue)
        self.assertEqual(testQueue.peek(), 1)
        self.assertEqual(testQueue.getCount(), 3)
        testQueue.enqueue(4)
        self.assertEqual(testQueue.dequeue(), 1)
        print(testQueue)
        self.assertEqual(testQueue.peek(), "2")
        self.assertEqual(testQueue.getCount(), 3)
        testQueue.enqueue(5)

        print(testQueue)
        self.assertEqual(testQueue.getCount(), 4)
        self.assertEqual(testQueue.dequeue(), "2")

        print(testQueue)
        self.assertEqual(testQueue.peek(), 3)
        self.assertEqual(testQueue.dequeue(), 3)

        print(testQueue)
        self.assertEqual(testQueue.getCount(), 2)
        self.assertEqual(testQueue.dequeue(), 4)

        print(testQueue)
        self.assertEqual(testQueue.getCount(), 1)
        self.assertEqual(testQueue.dequeue(), 5)
        self.assertTrue(testQueue.isEmpty())


if __name__ == '__main__':
    unittest.main()
