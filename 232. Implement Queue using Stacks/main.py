class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue = [x].extend(self.queue)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        result = self.queue[-1]
        self.queue = self.queue[:-1]
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue:
            return False
        else:
            return True