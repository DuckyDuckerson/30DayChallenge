from support.tools import print_message as pm

# ------------------------------------
a = 2
b = 4
c = 10
d = 14
e = 6
f = 33
g = 34
h = 66
# -------------------------------------

list0 = [a, b, c]
list1 = [d, e, f]

list2 = list0 + list1

pm(f'{list2}', 2, 1)

list2.append(h)
pm(f'{list2}', 2, 1)

list2.pop(1)
pm(f'{list2}', 2, 1)
