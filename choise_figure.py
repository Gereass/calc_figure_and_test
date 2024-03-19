from figuree import *

calc = calc()
type_figure = ''
a,b,c = 0,0,0

def check_tringle(a,b,c):
    return 'rectangular' if c*c == b*b + a*a else 'not rectangular' 

print("choose figure(C, T): ")
type_figure = str(input())


if type_figure == 'C' or type_figure == 'c':
    print('insert R: ')
    a = int(input())
    print('S circle:', calc.calc_S_circkl(a))
elif type_figure == 'T' or type_figure == 't':
    print('insert a,b,c: ')
    a,b,c = int(input())
    print('S tringle:', calc.calc_S_tringle(a,b,c))
    print(check_tringle(a,b,c))
    

