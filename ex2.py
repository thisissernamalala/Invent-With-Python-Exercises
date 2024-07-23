def convertToFarenheit(degreesCelsius):
    farenheit = degreesCelsius*(9/5)+32
    return farenheit


def convertToCelsius(degreesFarenheit):
    celsius = (degreesFarenheit-32)*(5/9)
    return celsius

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFarenheit(0) == 32
assert convertToFarenheit(100) == 212
assert convertToCelsius(convertToFarenheit(15)) == 15