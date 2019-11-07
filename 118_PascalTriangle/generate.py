from collections import deque


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output, pre = [], []
        for i in range(numRows):
            if not output:
                output.append([1])
                continue
            pre1, pre2 = output[-1] + [0], [0] + output[-1]
            pre = list(map(lambda x, y: x + y, pre1, pre2))
            output.append(pre)
        return output
