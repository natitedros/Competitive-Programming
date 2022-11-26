class Trie:
    def __init__(self):
        self.isWordEnd = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isWordEnd = True

    def search(self, word: str) -> bool:
        
        def rec(curr, index):
            if index == len(word):
                return curr.isWordEnd
            if word[index] == ".":
                for child in curr.children.keys():
                    if rec(curr.children[child], index+1):
                        return True
                return False
            elif word[index] not in curr.children:
                return False
            return rec(curr.children[word[index]], index+1)
        
        return rec(self.root, 0)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)