def stk(s, p):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        valueFound = False
        if len(stack)>=len(p):
            for j in range(len(p)):
                if stack[len(stack)-1-j] == p[len(p)-1-j]:
                    valueFound = True
                else:
                    valueFound = False
                    break
        if valueFound == True:
            for k in range(len(p)):
                stack.pop()
    ' '.join(stack)
    return stack

s = ["d","a","a","b","c","b","a","a","b","c","b","c"]
p = ["a","b","c"]
print(stk(s, p))
                
