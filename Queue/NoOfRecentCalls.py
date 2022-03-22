class RecentCounter:

    def __init__(self):
        self.requests = []
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0]<t-3000:
            self.requests.pop(0)
        return len(self.requests)
            