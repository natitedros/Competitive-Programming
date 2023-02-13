class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = a[::-1]
        b = b[::-1]
        res = []
        for i in range(max(len(a), len(b))):
            temp, count = 0, 0
            temp ^= carry
            count += carry
            if i < len(a):
                temp ^= int(a[i])
                count += int(a[i])
            if i < len(b):
                temp ^= int(b[i])
                count += int(b[i])
            res.append(str(temp))
            carry = 0
            if count > 1:
                carry = 1
        if carry:
            res.append(str(carry))
        res = res[::-1]
        return "".join(res)
        