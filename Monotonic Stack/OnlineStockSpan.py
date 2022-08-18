class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0]<=price:
            span += self.stk.pop()[1]
        self.stk.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)