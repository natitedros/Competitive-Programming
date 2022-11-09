class Solution:
    def backtrack(self, s, letters, index, result):
        if index == len(s):
            result.append(''.join(letters))
            return
        if not s[index].isnumeric():
            letters.append(s[index].upper())
            self.backtrack(s, letters, index+1, result)
            letters.pop()
            letters.append(s[index].lower())
            self.backtrack(s, letters, index+1, result)
            letters.pop()
        else:
            letters.append(s[index])
            self.backtrack(s, letters, index+1, result)
            letters.pop()
            return

    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, [], 0, result)
        return result