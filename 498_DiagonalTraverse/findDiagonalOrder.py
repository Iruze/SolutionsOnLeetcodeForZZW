# 沿着上边界和右边界向左下方扫描矩阵，注意前后两次需要反转单次扫描的结果
class Solution:

    flag = False

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # online总是从当前位置向左下方矩阵搜索元素
        # 注意前后两次要反转
        def online(rows, cols, r, c):
            ans = []
            while 0 <= r < rows and 0 <= c < cols:
                ans.append(matrix[r][c])
                r += 1
                c -= 1
            return ans if self.flag else ans[::-1]
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        output = []
        # 沿着上边界向左下方扫描
        for c in range(cols):
            output += online(rows, cols, 0, c)
            self.flag = not self.flag
        # 沿着右边界向左下方扫描
        for r in range(1, rows):
            output += online(rows, cols, r, cols - 1)
            self.flag = not self.flag
        return output
