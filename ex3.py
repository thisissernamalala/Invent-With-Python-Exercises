def isOdd(number):
    if number%2 != 0 and type(number)==int:
        return True
    elif number == 0:
        return False
    else:
        return False
    
def isEven(number):
    if number%2==0 and type(number)==int:
        return True
    elif number == 0:
        return True
    else:
        return False

assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False