class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2 or m < 0 or n < 0 or m + n > len(nums1):
            return
        idx1, idx2, idx = m - 1, n - 1, len(nums1) - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] < nums2[idx2]:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            idx -= 1
        while idx1 >= 0:
            nums1[idx] = nums1[idx1]
            idx -= 1
            idx1 -= 1
        while idx2 >= 0:
            nums1[idx] = nums2[idx2]
            idx -= 1
            idx2 -= 1
        for i in range(idx + 1):
            nums1[i] = 0
