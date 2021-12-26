a = [2,5,8]
s = ["abcde"]
b = a
s=list(s)
arr = s*2
arr = list(arr)
b[2] = 9

print(a)
print(b)

c = [i for i in a]
a[0] = 10
print(c)
print(a)
print(len(s))