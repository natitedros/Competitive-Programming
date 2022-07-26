class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = defaultdict(int)
        present = set()
        for char in p:
            freq[char] += 1
            present.add(char)
        left = 0
        right = 0
        window = defaultdict(int)
        res = []
        while right < len(s):
            window[s[right]] += 1
            if s[right] in present:
                while window[s[right]] > freq[s[right]]:
                    window[s[left]] -= 1
                    left += 1
                right += 1
            else:
                window = defaultdict(int)
                right += 1
                left = right
            if window == freq:
                res.append(left)
        return res