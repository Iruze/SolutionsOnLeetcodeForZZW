"""
乘积　＝　以某个节点node为根的总和　×　（所有节点总和　－　以node为根的节点的总和）：
"""
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def postorder(root):
            if not root: return 0
            s = postorder(root.left) + postorder(root.right) + root.val
            SUM.append(s)
            return s
        ans = 0
        SUM = []
        postorder(root)
        for i in range(len(SUM) - 1):
            ans = max(ans, SUM[i] * (SUM[-1] - SUM[i]))
        return ans % (10 ** 9 + 7)
