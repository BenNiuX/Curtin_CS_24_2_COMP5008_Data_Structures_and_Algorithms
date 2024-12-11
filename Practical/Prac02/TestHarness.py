import sys
import timeit
import prac02

def usage():
    print(" Usage: python TestHarness n xy")
    print("        where")
    print("        n is number of integers to calculate")
    print("        x is one of")
    print("           F - Factorial")
    print("           f - Fibonacci")
    print("           g - Greatest Common Denominator")
    print("           n - Number conversion")
    print("        y is one of")
    print("           I - Iterative")
    print("           R - Recursive")

def do(n, sceType, actType):
    try:
        if sceType == 'F':
            if actType == "I":
                print(prac02.calcNFactorialIterative(n))
            elif actType == "R":
                print(prac02.calcNFactorialRecursive(n))
            else:
                print("Unsupported")
        elif sceType =='f':
            if actType == "I":
                print(prac02.fibIterative(n))
            elif actType == "R":
                print(prac02.fibRecursive(n))
            else:
                print("Unsupported")
        elif sceType == 'g':
            if actType == "I":
                print(prac02.gcdIterative(n, 8))
            elif actType == "R":
                print(prac02.gcdRecursion(n, 8))
            else:
                print("Unsupported")
            pass
        elif sceType == 'n':
            if actType == "I":
                print(prac02.numConvInterative(n, 2))
            elif actType == "R":
                print(prac02.numConvRecursion(n, 2))
            else:
                print("Unsupported")
            pass
        else:
            print("Unsupported scenario")
    except ValueError as e:
        print("Value Error", e)
    except RecursionError as e:
        print("Recursion Error", e)

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        usage()
    else:
        for aa in range(2, len(sys.argv)):
        
            n = int(sys.argv[1])
            sceType = sys.argv[aa][0]
            actType = sys.argv[aa][1]

            runningTotal = 0

            startTime = timeit.default_timer()
            do(n, sceType, actType)
            endTime = timeit.default_timer()

            runningTotal += (endTime - startTime)
        
            print(sceType + actType + " " + str(n) + " " + str(runningTotal))