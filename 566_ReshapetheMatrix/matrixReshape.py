class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, columns = len(nums), len(nums[0])
        if rows * columns != r * c:
            return nums
        r1, c1 = 0, 0
        output = [[0] * c for _ in range(r)]
        for i in range(rows):
            for j in range(columns):
                if c1 == c:
                    r1, c1 = r1 + 1, 0
                output[r1][c1] = nums[i][j]
                c1 += 1
        return output
