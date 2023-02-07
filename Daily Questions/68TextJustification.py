class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        temp = [words[0]]
        count = len(words[0])
        spaces = []
        for i in range(1, len(words)):
            if count + 1 + len(words[i]) <= maxWidth:
                count += 1 + len(words[i])
                temp.append(words[i])
                spaces.append(1)
            else:
                if spaces:
                    left = maxWidth-count
                    added = left//len(spaces)
                    rem = left % len(spaces)
                    for j in range(len(spaces)):
                        spaces[j] += added
                        if rem:
                            spaces[j] += 1
                            rem -= 1
                    spaces.reverse()
                res = []
                char = 0
                for t in temp:
                    res.append(t)
                    char += len(res[-1])
                    if spaces:
                        res.append(" "*spaces.pop())
                        char += len(res[-1])
                res += " "*(maxWidth - char)
                answer.append("".join(res))
                count = len(words[i])
                temp = [words[i]]
                spaces = []
        res = []
        char = 0
        for t in temp:
            res.append(t)
            char += len(res[-1])
            if spaces:
                res.append(" "*spaces.pop())
                char += 1
        res += " "*(maxWidth - char)
        answer.append("".join(res))
        return answer