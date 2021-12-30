class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 !=0:
            return []
        else:
            freq = Counter(changed)
            changed.sort()
            original = []
            for i in range(len(changed)):
                if freq[changed[i]] != 0:
                    if changed[i]*2 in freq and freq[changed[i]*2] ==0:
                        return []
                    elif changed[i]*2 in freq:
                        freq[changed[i]] -= 1
                        freq[changed[i]*2] -= 1
                        original.append(changed[i])
                    else:
                        return[]
            return original