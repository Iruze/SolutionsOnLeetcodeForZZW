class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.order = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.order or x < self.order[-1]:
            self.order.append(x)
        else:
            self.order.append(self.order[-1])

    def pop(self) -> None:
        if self.data:
            self.order.pop()
            return self.data.pop()
        else:
            return -float('Inf')

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return -float('Inf')
            

    def getMin(self) -> int:
        if self.order:
            return self.order[-1]
        else:
            return -float('Inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
