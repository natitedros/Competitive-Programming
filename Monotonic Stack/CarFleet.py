class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        positionTime = {}
        for i in range(len(position)):
            positionTime[position[i]] = (target-position[i])/(speed[i])
        for i in sorted(positionTime):
            if stack == []:
                stack.append(positionTime[i])
            else:
                while stack != [] and positionTime[i] >= stack[-1]:
                    stack.pop()
                stack.append(positionTime[i])
        return len(stack)