"""
维护一个大小为s1长度的窗口，窗口在s2上滑动， 每次更新窗口首尾的字符，比对窗口和s1映射。
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        permutation, cur = [0] * 26, [0] * 26
        for c in s1:
            permutation[ord(c) - ord('a')] += 1
        lo, hi = 0, 0
        # cur, permutation分别存储s2, s1的字符映射
        while hi < l2:
            cur[ord(s2[hi]) - ord('a')] += 1
            # 维护一个大小为l1的窗口
            while hi - lo + 1 > l1:
                cur[ord(s2[lo]) - ord('a')] -= 1
                lo += 1
            if permutation == cur:
                return True
            hi += 1
        return False
