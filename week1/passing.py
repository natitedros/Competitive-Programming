a = [2,5,8]

b = a

b[2] = 9

print(a)
print(b)

c = [i for i in a]
a[0] = 10
print(c)
print(a)