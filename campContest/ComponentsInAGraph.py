def componentsInGraph(gb):
    # Write your code here
    n = len(gb)
    length = 2*(n+1)
    root = [0]*length
    group = {}
    for i in range(length):
        root[i] = i
        group[i] = [i]
    def find(ind):
        return root[ind]
    def union(one, two):
        parentOne = find(one)
        parentTwo = find(two)
        if parentOne == parentTwo:
            return 0
        if len(group[parentTwo]) > len(group[parentOne]):
            parentOne, parentTwo = parentTwo, parentOne
        for node in group[parentTwo]:
            root[node] = parentOne
            group[parentOne].append(node)
        del group[parentTwo]
    for edge in gb:
        union(edge[0], edge[1])
    counter = Counter(root)
    minVal = length
    maxVal = 0
    for freq in counter.values():
        if freq > maxVal:
            maxVal = freq
        if freq < minVal and freq > 1:
            minVal = freq
    return [minVal, maxVal]