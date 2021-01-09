class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.app = list()
        # decrease维护一个单调非递增栈
        self.decrease = list()


    def push(self, x: int) -> None:
        self.app.append(x)
        # 元素可能相同，　故而相等的也要加入到decrease中去
        if not self.decrease or x <= self.decrease[-1]:
            self.decrease.append(x)


    def pop(self) -> None:
        ans = self.app.pop()
        # 如果pop出来的是最小值，　则decrease中的队列也要减去它
        if ans == self.decrease[-1]:
            self.decrease.pop()
        return ans


    def top(self) -> int:
        return self.app[-1]


    def getMin(self) -> int:
        return self.decrease[-1]
