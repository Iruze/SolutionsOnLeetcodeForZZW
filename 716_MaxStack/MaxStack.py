class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deque = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.deque.appendleft(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.deque.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.deque[0]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.deque)

    def popMax(self):
        """
        :rtype: int
        """
        maxval = self.peekMax()
        self.deque.remove(maxval)
        return maxval


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
