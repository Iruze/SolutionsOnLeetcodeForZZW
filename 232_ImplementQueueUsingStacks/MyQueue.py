class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pu = []
        self.po = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pu.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.po:
            while self.pu:
                self.po.append(self.pu.pop())
        return self.po.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.po:
            while self.pu:
                self.po.append(self.pu.pop())
        return self.po[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.po == [] and self.pu == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
