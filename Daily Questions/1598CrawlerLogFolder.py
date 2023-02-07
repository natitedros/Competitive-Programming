class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if log == "../":
                steps = max(0, steps-1)
            elif log[0] != ".":
                steps += 1
        return steps
