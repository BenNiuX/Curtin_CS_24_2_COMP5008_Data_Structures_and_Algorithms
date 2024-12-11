
def calcNFactorialIterative(n):
    try:
        num = int(n)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import must not be negative")
    nFactorial = 1
    for ii in range(num, 1, -1):
        nFactorial = nFactorial * ii 
    return nFactorial

def calcNFactorialRecursive(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import must not be negative")
    factorial = 1
    if n == 0:
        factorial = 1
    else:
        factorial = n * calcNFactorialRecursive(n - 1)
    return factorial

def fibIterative(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import must not be negative")
    fibVal = 0
    currVal = 1
    lastVal = 0
    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        for ii in range(2, n + 1):
            fibVal = currVal + lastVal 
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibRecursive(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import must not be negative")
    fibVal = 0
    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        fibVal = fibRecursive(n - 1) + fibRecursive(n - 2)
    return fibVal

# Implement greatest common divisor using recursion
# Ref to https://dyclassroom.com/recursion-algorithm/greatest-common-divisor-gcd
def gcdRecursion(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if x < 0 or y < 0:
        raise ValueError("Import must not be negative")
    retVal = 0
    if y == 0:
        retVal = x
    else:
        retVal = gcdRecursion(y, x % y)
    return retVal

# Implement greatest common divisor using iterative
# Ref to https://stackoverflow.com/questions/41130709/finding-greatest-common-divisor-through-iterative-solution-python-3
def gcdIterative(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if x < 0 or y < 0:
        raise ValueError("Import must not be negative")
    elif x == 0 or y == 0:
        return 0
    z = x + y
    while z > 0:
        if x % z == 0 and y % z == 0:
            return z
        z -= 1
    return 1

def convDig(n, base):
    chars = ['A', 'B', 'C', 'D', 'E', 'F']
    if base >= 10:
        if n >= 10:
            return chars[n - 10]
    return str(n)



# Implement number conversions from Base 10 to any Base (2-16) using recursion
# Ref to https://www2.cs.arizona.edu/~mercer/Presentations/17B-RecursiveNumberConversion.pdf
def numConvRecursion(n, base):
    try:
        n = int(n)
        base = int(base)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import number must not be negative")
    if base < 2 or base > 16:
        raise ValueError("Import base must between 2 and 16")
    retVal = ""
    if n == 0:
        retVal = ""
    else:
        retVal = numConvRecursion(n // base, base) + convDig(n % base, base)
    return retVal


# Implement number conversions from Base 10 to any Base (2-16) using interative
# Refer to https://blog.finxter.com/5-best-ways-to-convert-integer-to-base-n-in-python/
def numConvInterative(n, base):
    try:
        n = int(n)
        base = int(base)
    except ValueError:
        raise ValueError("Input must be a integer number")
    if n < 0:
        raise ValueError("Import number must not be negative")
    if base < 2 or base > 16:
        raise ValueError("Import base must between 2 and 16")
    retVal = ""
    while n > 0:
        retVal = convDig(n % base, base) + retVal
        n //= base
    if len(retVal) == 0:
        return "0"
    return retVal

TAB = "    "

def moveDisk(n, src, dst, level):
    print(level * TAB, f"Recursion Level={level}")
    print(level * TAB, f"Moving disk {n} from peg {src} to peg {dst}")
    print(level * TAB, f"n={n}, src={src}, dst={dst}")

def towers(n, src, dst, level=1):
    try:
        n = int(n)
        src = int(src)
        dst = int(dst)
        checkTowerInput(n, src, dst)
    except ValueError as e:
        raise e
    print(level * TAB, f"START towers({n}, {src}, {dst}), Level={level}")
    if n == 1:
        moveDisk(n, src, dst, level)
    else:
        tmp = 6 - src - dst
        towers(n - 1, src, tmp, level + 1)
        moveDisk(n, src, dst, level)
        towers(n - 1, tmp, dst, level + 1)
    print(level * TAB, f"END towers({n}, {src}, {dst}), Level={level}")

def checkTowerInput(n, src, dst):
    try:
        n = int(n)
        src = int(src)
        dst = int(dst)
    except ValueError:
        raise ValueError("Please input integer!")
    else:
        checkRangePass = False
        if n < 1 or n > 10:
            pass
        elif src < 1 or src > 3:
            pass
        elif dst < 1 or dst > 3:
            pass
        elif src == dst:
            pass
        else:
            checkRangePass = True
        if not checkRangePass:
            raise ValueError("Input integer error!")

def testHanoi():
    inputError = True
    n = None
    src = None
    dst = None
    while inputError:
        print("Please input 3 integers: n src dst.")
        print("n shoud between 1 and 10, src and dst should be one of 1,2,3 and different.")
        inputStr = input()
        inputArr = inputStr.split()
        if len(inputArr) != 3:
            print("Input error, again!")
        else:
            try:
                towers(inputArr[0], inputArr[1], inputArr[2])
            except ValueError as e:
                print("Input error, again!", e)
            else:
                inputError = False

def test():
    try:
        print(fibIterative(-6))
        print(fibRecursive(-6))
    except ValueError:
        pass
    '''
    for i in range(2, 2003, 1):
        print(f"Start {i}")
        print(calcNFactorialIterative(i))
        # 1559 ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
        try:
            print(calcNFactorialRecursive(i))
        except RecursionError:
            print(f"Recersion {i}")
            break #998 happen recersion exception
    '''

    try:
        print(calcNFactorialIterative(-1))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    try:
        print(calcNFactorialIterative("abc"))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")

    print(calcNFactorialIterative(0))
    print(calcNFactorialRecursive(0))

    print(calcNFactorialIterative(3))
    print(calcNFactorialRecursive(3))

    print(fibIterative(0))
    print(fibRecursive(0))

    print(fibIterative(3))
    print(fibRecursive(3))
    try:
        print(gcdRecursion(-35,42))
        print(gcdIterative(-35,42))
    except ValueError:
        pass

    print(gcdRecursion(0,0))
    print(gcdIterative(0,0))
    print(gcdRecursion(0,1))
    print(gcdIterative(0,1))
    print(gcdRecursion(1,0))
    print(gcdIterative(1,0))
    print(gcdRecursion(1,1))
    print(gcdIterative(1,1))
    print(gcdRecursion(20, 5))
    print(gcdIterative(20, 5))
    print(gcdRecursion(20, 8))
    print(gcdIterative(20, 8))
    print(gcdRecursion(20, 3))
    print(gcdIterative(20, 3))
    print(numConvRecursion(0, 2))
    print(numConvInterative(0, 2))
    try:
        print(numConvRecursion(99, 1))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    try:
        print(numConvInterative(99, 1))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    print(numConvRecursion(99, 2))
    print(numConvInterative(99, 2))
    print(numConvRecursion(99, 3))
    print(numConvInterative(99, 3))
    print(numConvRecursion(99, 4))
    print(numConvInterative(99, 4))
    print(numConvRecursion(99, 5))
    print(numConvInterative(99, 5))
    print(numConvRecursion(99, 6))
    print(numConvInterative(99, 6))
    print(numConvRecursion(99, 7))
    print(numConvInterative(99, 7))
    print(numConvRecursion(99, 8))
    print(numConvInterative(99, 8))
    print(numConvRecursion(99, 9))
    print(numConvInterative(99, 9))
    print(numConvRecursion(99, 10))
    print(numConvInterative(99, 10))
    print(numConvRecursion(99, 11))
    print(numConvInterative(99, 11))
    print(numConvRecursion(99, 12))
    print(numConvInterative(99, 12))
    print(numConvRecursion(99, 13))
    print(numConvInterative(99, 13))
    print(numConvRecursion(99, 14))
    print(numConvInterative(99, 14))
    print(numConvRecursion(99, 15))
    print(numConvInterative(99, 15))
    print(numConvRecursion(99, 16))
    print(numConvInterative(99, 16))
    try:
        print(numConvRecursion(99, 17))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    try:
        print(numConvInterative(99, 17))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")

if __name__ == "__main__":
    test()
    testHanoi()
    print(numConvRecursion(13, 16))
    print(numConvInterative(13, 16))

    print(numConvRecursion(16, 16))
    print(numConvInterative(16, 16))

    print(numConvRecursion(17, 16))
    print(numConvInterative(17, 16))

    print(numConvRecursion(13, 15))
    print(numConvInterative(13, 15))

    print(numConvRecursion(14, 15))
    print(numConvInterative(14, 15))

    print(numConvRecursion(15, 15))
    print(numConvInterative(15, 15))

    print(numConvRecursion(16, 15))
    print(numConvInterative(16, 15))

    print(numConvRecursion(17, 15))
    print(numConvInterative(17, 15))
'''
    print(numConvRecursion(0, 2))
    print(numConvInterative(0, 2))
    try:
        print(numConvRecursion(99, 1))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    try:
        print(numConvInterative(99, 1))
    except ValueError:
        pass
    else:
        print("INPUT ERROR")
    print(numConvRecursion(99, 2))
    print(numConvInterative(99, 2))
'''
