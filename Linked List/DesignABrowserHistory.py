class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.ptr = node

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.ptr
        self.ptr.next = node
        self.ptr = self.ptr.next

    def back(self, steps: int) -> str:
        while steps and self.ptr.prev:
            self.ptr = self.ptr.prev
            steps -= 1
        return self.ptr.val

    def forward(self, steps: int) -> str:
        while steps and self.ptr.next:
            self.ptr = self.ptr.next
            steps -= 1
        return self.ptr.val