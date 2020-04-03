# 方法一： 二分法：
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 计算matrix中小于等于num的元素的个数
        def rank(num):
            r, c = 0, cols - 1
            cnt = 0
            while r < rows and 0 <= c:
                if matrix[r][c] <= num:
                    cnt += c + 1
                    r += 1
                else:
                    c -= 1
            return cnt
        rows, cols = len(matrix), len(matrix[0])
        low, hight = matrix[0][0], matrix[-1][-1]
        # 二分法计算出第k个元素
        while low < hight:
            mid = low + ((hight - low) >> 1)
            rk = rank(mid)
            if rk < k:
                low = mid + 1
            else:
                hight = mid
        return low
        
# 方法二：堆
# 每一列从左向右推进，堆的元素维护在n个
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        hp = []
        # 建堆，k小于n时，只需前k行行首元素入堆
        for r in range(min(k, n)):
            heapq.heappush(hp, (matrix[r][0], r, 0))
        cnt = 0
        x, i, j = 0, 0, 0
        while cnt < k:
            cnt += 1
            x, i, j = heappop(hp)
            # 当最小元素出堆后，该元素的后一个元素入堆
            if j + 1 < n:
                heappush(hp, (matrix[i][j + 1], i, j + 1))
        return x
