def solve(s):
    result = 0
    prev = 2
    for i in range(len(s)):
        temp = ord(s[i]) - 97
        if prev == temp:
            result += 2
        elif prev == (temp+1)%3:
            result += 1
        prev = temp
    return result
print(solve("bcaaa"))
