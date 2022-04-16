def toys(w):
    # Write your code here
    n = len(w)
    if n == 1:
        return 1
    w.sort()
    container = 0
    ptr = 0
    for i in range(len(w)):
        if w[ptr]+4<w[i]:
            ptr = i
            container += 1
    return container+1