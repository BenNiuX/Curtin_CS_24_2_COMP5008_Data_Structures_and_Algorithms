#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

import random

def bubbleSort(A):
    # print('Begin:', A)
    for i in range(A.size - 1):
        swapped = False
        for ii in range(A.size - 1 - i):
            if A[ii] > A[ii + 1]:
                temp = A[ii]
                A[ii] = A[ii + 1]
                A[ii + 1] = temp
                # print(i, ii, A)
                swapped = True
        if not swapped:
            # print('After:', A)
            return
    # print('After:', A)

def insertionSort(A):
    # print('Begin:', A)
    i = 1
    for i in range(1, A.size):
        ii = i
        while ii > 0 and A[ii - 1] > A[ii]:
            temp = A[ii]
            A[ii] = A[ii - 1]
            A[ii - 1] = temp
            # print(i, ii, A)
            ii -= 1
    # print('After:', A)

def selectionSort(A):
    # print('Begin:', A)
    for i in range(A.size):
        minIdx = i
        for jj in range(i + 1, A.size):
            if A[jj] < A[minIdx]:
                minIdx = jj
        if minIdx != i:
            temp = A[minIdx]
            A[minIdx] = A[i]
            A[i] = temp
            # print(i, minIdx, A)
    # print('After:', A)

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurseMedian3(A, 0, A.size - 1)

def quickSortRecurseLeft(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = leftIdx  # left-most element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseLeft(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseLeft(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return

def quickSortRecurseRan(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)  # random element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseRan(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseRan(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return

def quickSortRecurseMid(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = (leftIdx + rightIdx) // 2  # middle element
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurseMid(A, leftIdx, newPivotIdx - 1)
        quickSortRecurseMid(A, newPivotIdx + 1, rightIdx)
    else:
        # Base case
        return

def quickSortRecurseMedian3(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        # Median 3 element
        midIdx = (leftIdx + rightIdx) // 2
        if (A[leftIdx] - A[midIdx]) * (A[rightIdx] - A[leftIdx]) >= 0:
            pivotIdx = leftIdx
        elif (A[midIdx] - A[leftIdx]) * (A[rightIdx] - A[midIdx]) >= 0:
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
    print('Begin:', A, leftIdx, rightIdx, pivotIdx)
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx
    print('Mid:', A)
    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[currIdx]
            A[currIdx] = A[ii]
            A[ii] = temp
            currIdx += 1
    newPivIdx = currIdx
    A[rightIdx] = A[newPivIdx]
    A[newPivIdx] = pivotVal
    print('After:', A)
    return newPivIdx

def trickleDown(A, curIdx, numItems):
    lIdx = curIdx * 2 + 1
    rIdx = lIdx + 1
    if lIdx < numItems:
        largeIdx = lIdx
        if rIdx < numItems:
            if A[lIdx] < A[rIdx]:
                largeIdx = rIdx
        if A[largeIdx] > A[curIdx]:
            tmp = A[largeIdx]
            A[largeIdx] = A[curIdx]
            A[curIdx] = tmp
            trickleDown(A, largeIdx, numItems)

def heapify(A, numItems):
    for i in range(int(numItems/2)-1, -1, -1):
        trickleDown(A, i, numItems)

def heapSort(A):
    print('Begin:', A)
    heapify(A, A.size)
    for i in range(A.size - 1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        trickleDown(A, 0, i)
    print('After:', A)