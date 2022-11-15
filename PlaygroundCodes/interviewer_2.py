def solve(phonenumber1, phonenumber2):
    stk1 = []
    for num in phonenumber1:
        if num == "#":
            stk1.pop()
        else:
            stk1.append(num)
    stk2 = []
    for num in phonenumber2:
        if num == "#":
            stk2.pop()
        else:
            stk2.append(num)
    return stk1 == stk2