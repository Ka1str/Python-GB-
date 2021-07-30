class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        other = other.__complex

        r_complex = self.__complex + other
        return MyComplex(r_complex.real, int(r_complex.imag))

    def __mul__(self, other):
        other = other.__complex

        r_complex = self.__complex * other
        return MyComplex(r_complex.real, int(r_complex.imag))

    def __str__(self):
        return self.__complex.__str__()


c1 = MyComplex(2, -3)
c2 = MyComplex(5)

print(c1 + c2)
print(c1 * c2)
