class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.denom = d
        
    def __str__(self):
        return "{}/{}".format(self.num, self.denom)

fraction = Fraction(5,6)
# print(fraction)