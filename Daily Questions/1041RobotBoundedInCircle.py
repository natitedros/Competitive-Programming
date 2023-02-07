class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        go = [0,1]
        pos = [0,0]
        # left rotate => swap and if x was 0, mul with -1
        # right rotate=> swap and if y was 0, mul with -1
        for i in instructions:
            if i == "L":
                mul = -1 if go[0] == 0 else 1
                go[0], go[1] = go[1], go[0]
                go[0] *= mul
                go[1] *= mul
            elif i == "R":
                mul = -1 if go[1] == 0 else 1
                go[0], go[1] = go[1], go[0]
                go[0] *= mul
                go[1] *= mul
            else:
                print("hi")
                pos[0] += go[0]
                pos[1] += go[1]
        return not (pos != [0,0] and go == [0, 1])
