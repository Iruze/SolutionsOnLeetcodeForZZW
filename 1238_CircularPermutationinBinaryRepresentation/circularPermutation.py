class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        # 89. 格雷编码： https://leetcode-cn.com/problems/gray-code/
        def grayCode(n):
            return [i ^ i >> 1 for i in range(2 ** n)]
        
        # 189. 旋转数组： https://leetcode-cn.com/problems/rotate-array/
        gray = grayCode(n)
        idx = gray.index(start)
        gray[:idx], gray[idx:] = gray[:idx][::-1], gray[idx:][::-1]
        gray = gray[::-1]
        
        return gray
