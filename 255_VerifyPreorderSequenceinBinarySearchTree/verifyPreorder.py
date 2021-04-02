# 参考: 
# https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/solution/python3-tu-jie-by-ml-zimingmeng/


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        new_min = float('-inf')
        for idx, p in enumerate(preorder):
            if p < new_min: return False
            while stack and preorder[stack[-1]] < p:
                new_min = preorder[stack.pop()]
            stack.append(idx)
        return True
