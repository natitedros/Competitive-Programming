class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def rec(ind):
            temp  = ""
            digit = ""
            while ind < n and s[ind] != "]":
                if s[ind].isdigit():
                    digit += s[ind]
                elif s[ind] == "[":
                    chars,ind = rec(ind+1)
                    temp += int(digit)*chars
                    digit = ""
                else:
                    temp += s[ind]
                ind += 1
            return (temp,ind)
        decoded,index = rec(0)             
        return decoded