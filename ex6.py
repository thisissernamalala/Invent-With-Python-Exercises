#

def ordinalSuffix(num):

    num1 = str(num)
    if num1[-1] == "1" and num1!='11':
        return num1+"st"

    elif num1[-1] == "2" and num1!='12':
        return num1+"nd"

    elif num1[-1] == "3" and num1!='13':
        return num1+"rd"

    else:
        return num1+"th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'