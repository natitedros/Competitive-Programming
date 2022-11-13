class TrieNode():
    def __init__(self):
        self.value = 0
        self.children = dict()

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.value = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        sums = 0
        def findPrefix(curr):
            nonlocal sums
            sums += curr.value
            for child in curr.children.values():
                findPrefix(child)
        findPrefix(curr)
        return sums
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)