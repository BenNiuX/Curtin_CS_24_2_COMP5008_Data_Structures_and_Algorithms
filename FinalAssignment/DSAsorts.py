import random


def quickSort(A):
    """
    Sort the array using quick sort algorithm
    """
    size = len(A)
    quickSortRecurseMedian3(A, 0, size - 1)


def quickSortRecurseLeft(A, leftIdx, rightIdx):
    """
    Implement quick sort algorithm using left-most element as pivot.
    """
    if rightIdx > leftIdx:
        pivotIdx = leftIdx  # left-most element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseLeft(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseLeft(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return


def quickSortRecurseRan(A, leftIdx, rightIdx):
    """
    Implement quick sort algorithm using random element as pivot.
    """
    if rightIdx > leftIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)  # random element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseRan(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseRan(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return


def quickSortRecurseMid(A, leftIdx, rightIdx):
    """
    Implement quick sort algorithm using middle element as pivot.
    """
    if rightIdx > leftIdx:
        pivotIdx = (leftIdx + rightIdx) // 2  # middle element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseMid(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseMid(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return


def quickSortRecurseMedian3(A, leftIdx, rightIdx):
    """
    Implement quick sort algorithm using median 3 element as pivot.
    """
    if rightIdx > leftIdx:
        # Median 3 element
        midIdx = (leftIdx + rightIdx) // 2
        if (A[leftIdx].getBatteryLevel() - A[midIdx].getBatteryLevel()) * (
            A[rightIdx].getBatteryLevel() - A[leftIdx].getBatteryLevel()
        ) >= 0:
            pivotIdx = leftIdx
        elif (A[midIdx].getBatteryLevel() - A[leftIdx].getBatteryLevel()) * (
            A[rightIdx].getBatteryLevel() - A[midIdx].getBatteryLevel()
        ) >= 0:
            pivotIdx = midIdx
        else:
            pivotIdx = rightIdx
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseMedian3(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseMedian3(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    """
    Find all values that are smaller than the pivot
    and transfer them to the left-hand-side of the array.
    """
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):
        if A[ii].getBatteryLevel() > pivotVal.getBatteryLevel():
            temp = A[currIdx]
            A[currIdx] = A[ii]
            A[ii] = temp
            currIdx += 1
    newPivIdx = currIdx
    A[rightIdx] = A[newPivIdx]
    A[newPivIdx] = pivotVal
    return newPivIdx


def trickleDown(A, curIdx, numItems):
    """
    Trickle down the item to the correct position in the heap sort.
    """
    lIdx = curIdx * 2 + 1
    rIdx = lIdx + 1
    if lIdx < numItems:
        largeIdx = lIdx
        if rIdx < numItems:
            if A[lIdx].getDistanceToDest() < A[rIdx].getDistanceToDest():
                largeIdx = rIdx
        if A[largeIdx].getDistanceToDest() > A[curIdx].getDistanceToDest():
            tmp = A[largeIdx]
            A[largeIdx] = A[curIdx]
            A[curIdx] = tmp
            trickleDown(A, largeIdx, numItems)


def heapify(A, numItems):
    """
    Heapify the array.
    """
    for i in range(int(numItems/2)-1, -1, -1):
        trickleDown(A, i, numItems)


def heapSort(A):
    """
    Sort the array using heap sort algorithm.
    """
    heapify(A, A.size)
    for i in range(A.size - 1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        trickleDown(A, 0, i)


def findNearestVehicle(vehicles):
    """
    Find the nearest vehicle from the list of vehicles.
    """
    if vehicles is not None and vehicles.size == 0:
        return None
    heapSort(vehicles)
    return vehicles[0]


def findVehicleWithHighestBattery(vehicles):
    """
    Find the vehicle with the highest battery from the list of vehicles.
    """
    if vehicles is not None and vehicles.size == 0:
        return None
    quickSort(vehicles)
    return vehicles[0]
