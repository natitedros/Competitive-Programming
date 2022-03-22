class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        pushPtr = 0
        popPtr = 0
        length = len(pushed)
        while pushPtr < length:
            stk.append(pushed[pushPtr])
            while stk != [] and popped[popPtr] == stk[-1]:
                stk.pop()
                popPtr += 1
            pushPtr += 1
        if stk == []:
            return True
        else:
            return False