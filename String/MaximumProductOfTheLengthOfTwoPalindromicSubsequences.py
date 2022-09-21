class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindrome = {}
        for mask in range(1,1<<n): #all possible subsequences
            subseq = ""
            for i in range(n):
                if mask & 1<<i:
                    subseq += s[n-i-1]
            if subseq == subseq[::-1]:
                palindrome[mask] = subseq
        maxProduct = 0
        for mask1 in palindrome.keys():
            for mask2 in palindrome.keys():
                if not mask1 & mask2:
                    maxProduct = max(maxProduct,len(palindrome[mask1])*len(palindrome[mask2]))
        return maxProduct