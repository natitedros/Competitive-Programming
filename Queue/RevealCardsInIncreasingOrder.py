class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque()
        for i in range(len(deck)-1,-1,-1):
            if not q:
                q.appendleft(deck[i])
            else:
                q.appendleft(q.pop())
                q.appendleft(deck[i])
        return q