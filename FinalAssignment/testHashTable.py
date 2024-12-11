import unittest

from DSAHashTable import DSAHashTable
from DSAVehicle import Vehicle


class TestHashTable(unittest.TestCase):
    """
    Test the hash table class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """
        Function to test the hash table class.
        """
        vehIds = ["A", "B", "C", "D", "E", "F", "G"]
        vehicles = []
        for i in range(len(vehIds)):
            veh = Vehicle(vehIds[i])
            vehicles.append(veh)
        testHash = DSAHashTable(5)
        print(testHash)
        testHash.insert(vehicles[0])
        self.assertEqual(testHash.count, 1)
        testHash.insert(vehicles[1])
        self.assertEqual(testHash.count, 2)
        print(testHash)
        self.assertEqual(testHash.search(vehicles[0].vid), vehicles[0])
        self.assertEqual(testHash.search(vehicles[1].vid), vehicles[1])
        testHash.insert(vehicles[2])
        print(testHash)
        testHash.insert(vehicles[3])
        print(testHash)
        testHash.insert(vehicles[4])
        print(testHash)
        testHash.insert(vehicles[5])
        print(testHash)
        testHash.insert(vehicles[6])
        print(testHash)
        self.assertEqual(testHash.count, 7)
        testHash.delete(vehicles[0].vid)
        print(testHash)
        self.assertEqual(testHash.count, 6)
        testHash.delete(vehicles[1].vid)
        print(testHash)
        self.assertEqual(testHash.count, 5)
        testHash.delete(vehicles[2].vid)
        print(testHash)
        self.assertEqual(testHash.count, 4)
        testHash.delete(vehicles[3].vid)
        print(testHash)
        self.assertEqual(testHash.count, 3)
        testHash.delete(vehicles[4].vid)
        print(testHash)
        self.assertEqual(testHash.count, 2)
        testHash.delete(vehicles[5].vid)
        print(testHash)
        self.assertEqual(testHash.count, 1)
        testHash.delete(vehicles[6].vid)
        print(testHash)
        self.assertEqual(testHash.count, 0)
        self.assertFalse(testHash.delete("9"))
        self.assertIsNone(testHash.search("9"))


if __name__ == '__main__':
    unittest.main()
