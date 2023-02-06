class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,1))
        char = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                pos, speed = queue.popleft()
                if pos == target:
                    return char
                queue.append((pos+speed, speed*2))
                if (pos+speed < target and speed < 0) or (pos+speed > target and speed > 0):
                    if speed > 0:
                        queue.append((pos, -1))
                    else:
                        queue.append((pos, 1))
            char += 1