class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # # 解法一：排序+双指针， O(nlogn)
        # nums_sort = sorted(nums)
        # left, right = 0, len(nums) - 1
        # while left < len(nums) and nums[left] == nums_sort[left]:
        #     left += 1
        # while right >= 0 and nums[right] == nums_sort[right]:
        #     right -= 1
        # return right - left + 1 if right > left else 0

        # 解法二：双指针，O(n)
        # 参考： https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
        left_max, right_min = nums[0], nums[-1]
        # begin 记录左边“凸出来”的第一个元素位置
        # end 记录右边“凹下去”的第一个元素位置
        begin, end = 0, -1
        for i, num in enumerate(nums):
            if num < left_max:
                end = i
            else:
                left_max = num
            if nums[len(nums) - i - 1] > right_min:
                begin = len(nums) - i - 1
            else:
                right_min = nums[len(nums) - i - 1]
        return end - begin + 1
