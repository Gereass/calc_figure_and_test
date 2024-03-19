NAME = "figuree"
import math


class calc:
    def calc_S_circkl(self, r):
        return round((r * r * math.pi), 5)

    def calc_S_tringle(self, a,b,c):
        p = 0
        p = (a+b+c)/2
        return round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 5)