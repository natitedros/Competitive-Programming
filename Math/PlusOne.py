class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (temp + carry) // 10
        if not carry:
            return digits
        return [carry] + digits