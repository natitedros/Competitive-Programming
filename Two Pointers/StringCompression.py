class Solution:
    def compress(self, chars: List[str]) -> int:
        freq = 0
        left = 0
        for i in range(len(chars)):
            if i == 0 or chars[i-1] == chars[i]:
                freq += 1
            else:
                chars[left] = chars[i-1]
                if freq > 1:
                    freq = str(freq)
                    for j in range(len(freq)):
                        left += 1
                        chars[left] = freq[j]
                left += 1
                freq = 1
        chars[left] = chars[-1]
        if freq > 1:
            freq = str(freq)
            for j in range(len(freq)):
                left += 1
                chars[left] = freq[j]
        return left+1