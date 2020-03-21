# 解法一：O(log(m + n))
# 参考： https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/leetcode-4-median-of-two-sorted-arrays-xun-zhao-li/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        k, k_pre = (n + 2) // 2, (n + 1) // 2
        if n & 1 == 1:
            return self.getKth(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k)
        return (self.getKth(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k) + self.getKth(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k_pre)) / 2 

    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        l1 = end1 - start1 + 1
        l2 = end2 - start2 + 1
        if l1 > l2: return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if l1 == 0: return nums2[start2 + k - 1]
        if k == 1: return min(nums1[start1], nums2[start2])
        i = start1 + min(k // 2, l1) - 1
        j = start2 + min(k // 2, l2) - 1
        if nums1[i] < nums2[j]:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
        return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))

# 解法二： O(log(min(m, n)
# 参考：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/shuang-zhi-zhen-by-powcai/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right :
            m1 = left +(right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / 2
