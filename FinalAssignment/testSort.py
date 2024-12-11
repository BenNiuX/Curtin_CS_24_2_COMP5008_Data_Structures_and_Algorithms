import unittest
import numpy as np

from DSAsorts import heapSort, quickSort
from DSAVehicle import Vehicle


class TestSort(unittest.TestCase):
    """
    Test the sort functions.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHeapSort(self):
        """
        Test the heap sort function.
        """
        vehIds = ["A", "B", "C", "D", "E"]
        distances = [3, 1, 5, 4, 2]
        vehicles = np.arange(len(vehIds), dtype=Vehicle)
        for i, vehId in enumerate(vehIds):
            veh = Vehicle(vehId)
            veh.setDistanceToDest(distances[i])
            vehicles[i] = veh
        print("Unsorted vehicles:")
        for vehicle in vehicles:
            print(vehicle)
        heapSort(vehicles)
        print("Heap sorted vehicles:")
        prevDist = 0
        for i in range(vehicles.size):
            veh = vehicles[i]
            self.assertTrue(veh.getDistanceToDest() >= prevDist)
            prevDist = veh.getDistanceToDest()
            print(veh)

    def testQuickSort(self):
        """
        Test the quick sort function.
        """
        vehIds = ["A", "B", "C", "D", "E"]
        batteryLevels = [3, 1, 5, 4, 2]
        vehicles = np.arange(len(vehIds), dtype=Vehicle)
        for i, vehId in enumerate(vehIds):
            veh = Vehicle(vehId)
            veh.setBatteryLevel(batteryLevels[i])
            vehicles[i] = veh
        print("Unsorted vehicles:")
        for vehicle in vehicles:
            print(vehicle)
        quickSort(vehicles)
        print("Quick sorted vehicles:")
        prevDist = 0
        for i in range(vehicles.size):
            veh = vehicles[i]
            self.assertTrue(veh.getDistanceToDest() <= prevDist)
            prevDist = veh.getBatteryLevel()
            print(veh)


if __name__ == '__main__':
    unittest.main()
