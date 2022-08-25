class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for char in magazine:
            mag[char] += 1
        for char in ransomNote:
            mag[char] -= 1
            if mag[char] < 0:
                return False
        return True