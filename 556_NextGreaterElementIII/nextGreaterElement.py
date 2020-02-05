class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        if len(nums) <= 1:
            return -1
        front = len(nums) - 2
        while front >= 0 and nums[front] >= nums[front + 1]:
            front -= 1
        if front >= 0:
            end = len(nums) - 1
            while front < end and nums[end] <= nums[front]:
                end -= 1
            nums[front], nums[end] = nums[end], nums[front]
        nums[front+1:] = nums[front+1:][::-1]
        n_new = int(''.join(nums))
        return n_new if n_new > n and n_new < pow(2, 31) else -1
