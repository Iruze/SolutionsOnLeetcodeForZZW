class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            self.nums = []
        else:
            # 只能nums不为空，才能进行后续赋值
            self.nums = [0] * len(nums)
            # 前缀和
            self.nums[0] = nums[0]
            for i in range(1, len(nums)):
                self.nums[i] = self.nums[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums or i > j or i < 0 or j >= len(self.nums):
            return 0
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
