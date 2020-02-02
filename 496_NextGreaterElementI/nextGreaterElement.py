# 解法一：先reg，后从reg中检索nums1中的元素
# 时间复杂度： O(M + N), 空间负责度：O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        reg = {}
        # reg记录nums2中每个数下一个更大元素
        # stack维护一个单调递减序列
        for i, v in enumerate(nums2):
            while stack and nums2[stack[-1]] < v:
                reg[nums2[stack.pop()]] = v
            stack.append(i)
        # 从reg中检索nums1中的每个元素
        res = []
        for num in nums1:
            if num in reg:
                res.append(reg[num])
            else:
                res.append(-1)
        return res
        


# 解法二： 直接在while，弹出栈的过程中判断 if num in nums1：
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                num = nums2[stack[-1]]
                if num in nums1:
                    res[nums1.index(num)] = nums2[i]
                stack.pop()
            stack.append(i)
        return res
