def celsius(degreeC):
    degreeF = degreeC * 1.8 + 32
    return degreeF


text = celsius(100)
print(text)


def fahrenheit(degreeA):
    degreeB = (degreeA - 32) / 1.8
    return degreeB


abc = fahrenheit(212)
print(abc)
