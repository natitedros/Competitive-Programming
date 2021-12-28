class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            stack.append(i)
            if stack[-1] == "+":
                stack.pop()
                temp = 0
                temp = int(stack.pop(-2)) + int(stack.pop(-1))
                stack.append(temp)
            elif stack[-1] == "-":
                stack.pop()
                temp = 0
                temp = int(stack.pop(-2)) - int(stack.pop(-1))
                stack.append(temp)
            elif stack[-1] == "*":
                stack.pop()
                temp = 0
                temp = int(stack.pop(-2)) * int(stack.pop(-1))
                stack.append(temp)
            elif stack[-1] == "/":
                stack.pop()
                temp = 0
                temp = int(stack.pop(-2)) / int(stack.pop(-1))
                stack.append(temp)
        return int(stack.pop())