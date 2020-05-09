"""
python3, 逐个取nums1和nums2中的序列，合并，比较，保留最大的序列：

1). 从nums1中取s个数字，显然 s 在[max(0, k - l2), min(l1, k)]区间内；
2). 则nums2中取 k - s个数字；
3). 合并上面取到的序列, 比较保留最大的序列
"""

class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 求nums中长度为k的最大的序列
        def maxKSeq(nums, k):
            giveup = len(nums) - k
            stack = []
            for i, v in enumerate(nums):
                while stack and stack[-1] < v and giveup:
                    stack.pop()
                    giveup -= 1
                stack.append(v)
            return stack[:k]
        # 合并nums1和nums2序列
        def merge(nums1, nums2):
            nums = []
            while nums1 and nums2:
                nums.append(max(nums1, nums2).pop(0))
            return nums + (nums1 or nums2)

        l1, l2 = len(nums1), len(nums2)
        ans = [0 for _ in range(k)]
        for s in range(max(0, k - l2), min(l1, k) + 1):
            cur = merge(maxKSeq(nums1, s), maxKSeq(nums2, k - s))
            # max可以从多个list中取字典序最大的那一个
            ans = max(ans, cur)
        return ans
