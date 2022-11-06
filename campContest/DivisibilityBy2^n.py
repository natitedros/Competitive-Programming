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
    
def countZeros(num):
    length = num.bit_length()
    result = 0
    for i in range(length):
        if num & (1<<i):
            break
        result += 1
    return result

def main():
    for _ in range(inp()):
        n = inp()
        nums = inlt()
        indexZeros = []
        currentZeros = 0
        for i, num in enumerate(nums):
            indexZeros.append(countZeros(i+1))
            currentZeros += countZeros(num)
        if currentZeros >= n:
            print(0)
        else:
            indexZeros.sort(reverse=True)
            count = 0
            found = False
            for i in range(len(indexZeros)):
                currentZeros += indexZeros[i]
                if currentZeros >= n:
                    print(i+1)
                    found = True
                    break
            if not found:
                print(-1)
                    
main()