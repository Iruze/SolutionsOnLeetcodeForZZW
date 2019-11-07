class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        for i in range(rowIndex):
            cur1, cur2 = cur + [0], [0] + cur
            cur = list(map(lambda x, y: x + y, cur1, cur2))
        return cur
