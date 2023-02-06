class DetectSquares:

    def __init__(self):
        self.xaxis = defaultdict(set)
        self.points = set()
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.add((point[0], point[1]))
        self.xaxis[point[0]].add((point[0], point[1]))
        self.freq[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        for x, y in self.xaxis[point[0]]:
            d = y-point[1]
            if d != 0:
                third, fourth = (x+d, point[1]), (x+d, y)
                if third in self.points and fourth in self.points:
                    count += self.freq[(x, y)] * self.freq[third] * self.freq[fourth]
                fifth, sixth = (x-d, point[1]), (x-d, y)
                if fifth in self.points and sixth in self.points:
                    count += self.freq[(x, y)] * self.freq[fifth] * self.freq[sixth]
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)