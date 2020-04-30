""" 洗牌算法

def shuffle(nums):
  n = len(nums)
  for i in range(n):
    rand = random.randint(i, n - 1)     # [i, n - 1]
    swap(nums, i, rand)
# 一共有 n! 的可能，所以是均匀随机打乱的
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.cur = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.cur)
        for i in range(n):
            rand = random.randint(i, n - 1)
            self.cur[i], self.cur[rand] = self.cur[rand], self.cur[i]
        return self.cur
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
