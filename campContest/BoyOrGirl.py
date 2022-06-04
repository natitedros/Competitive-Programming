import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

name = insr()
letters = set()
count = 0
for char in name:
    if char not in letters:
        letters.add(char)
        count += 1
print(letters)
if count%2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")