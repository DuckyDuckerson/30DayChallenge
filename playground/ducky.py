thirdy = __import__('30DayChallenge.support.tools')
from thirdy import pm

a = 2
b = 4
c = 10
d = 14
e = 6
f = 33

list0 = [a, b, c]
list1 = [d, e, f]

list2 = list0 + list1

pm(f'{list2}', 2, 1)

