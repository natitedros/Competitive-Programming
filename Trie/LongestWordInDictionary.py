class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Solution:
    def insertWord(self, word, root):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            self.insertWord(word, root)

        result = ""
        for k in range(26):
            char = chr(k+97)
            if char in root.children:
                def returnLongest(currWord, current, character):
                    nonlocal result
                    if current.isWord == False:
                        return
                    currWord.append(character)
                    if len(result) < len(currWord):
                        result = "".join(currWord)
                    for i in range(26):
                        key = chr(i+97)
                        if key in current.children:
                            returnLongest(currWord, current.children[key], key)
                    currWord.pop()
                    return
                returnLongest([], root.children[char], char)
        return result
