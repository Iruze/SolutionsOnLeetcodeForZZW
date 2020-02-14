class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.random = 0

    def pick(self, target: int) -> int:
        n = 0
        for i, v in enumerate(self.nums):
            if v == target:
                n += 1
                # randint的范围为 [1, n]
                if random.randint(1, n) == 1:
                    self.random = i 
        return self.random



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
