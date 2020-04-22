# 模拟（暴力）解法

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def spiral(x, y, offset=0):
            while True:
                if len(ans) == R * C:
                    break
                offset += 1
                # lo - > hi
                for i in range(1, offset + 1):
                    if isInternal(x, y + i) and len(ans) < R * C:
                        ans.append([x, y + i])
                y += offset

                # up - > down
                for i in range(1, offset + 1):
                    if isInternal(x + i, y) and len(ans) < R * C:
                        ans.append([x + i, y])
                x += offset

                offset += 1

                # hi - > lo
                for i in range(1, offset + 1):
                    if isInternal(x, y - i) and len(ans) < R * C:
                        ans.append([x, y - i])
                y -= offset

                # down - > up
                for i in range(1, offset + 1):
                    if isInternal(x - i, y) and len(ans) < R * C:
                        ans.append([x - i, y])
                x -= offset
        
        def isInternal(x, y):
            return 0 <= x < R and 0 <= y < C 
        
        ans = [[r0, c0]]
        spiral(r0, c0)

        return ans
