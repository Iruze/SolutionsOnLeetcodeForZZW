class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        SUM = sum(A)
        # 如果总和不能三等分
        if SUM % 3 != 0:
            return False
        SUM //= 3
        total, idx = A[0], 1
        # 计算第一段1/3
        while total != SUM and idx < len(A):
            total, idx = total + A[idx], idx + 1
        # 如果idx到头了，则只能一等分
        if idx == len(A):
            return False
        # 计算第二段1/3
        total, idx = A[idx], idx + 1
        while total != SUM and idx < len(A):
            total, idx = total + A[idx], idx + 1
        # 如果idx到头了，只能二等分
        return idx < len(A)
