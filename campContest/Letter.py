import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def main():
    s = list(input().strip())
    lower = 0
    upper = 0
    result = 0
    for char in s:
        if char.islower():
            lower += 1
        else:
            if lower > 0:
                result += 1
                lower -= 1
    print(result)
main()