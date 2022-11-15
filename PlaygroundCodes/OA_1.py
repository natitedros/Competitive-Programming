def solve(s):
    result = 0
    for i in range(1, len(s)):
        temp = ord(s[i]) - 97
        prev = ord(s[i-1]) - 97
        if prev == temp:
            result += 2
        elif prev == (temp+1)%3:
            result += 1
    return result
