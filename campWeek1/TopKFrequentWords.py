class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap= []
        res = []
        counter = Counter(words)
        for kv in counter.items():
            heapq.heappush(heap, (-1*kv[1],kv[0]))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res