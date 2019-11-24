class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> None:
        self.queue = self.queue[:-1]

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        if not self.queue:
            return None
        return min(self.queue)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()