# 方法一： 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, cnt = nums[0], 1
        for num in nums[1:]:
            if num == ans:
                cnt += 1
            elif cnt == 1:
                ans = num 
            else:
                cnt -= 1
        return ans
        
# 方法二：借助set
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        for i in set1:
            if(nums.count(i) > len(nums) // 2):
                return i
