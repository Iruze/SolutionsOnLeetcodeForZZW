# 方法一： 递归版本

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        f = self.preorderTraversal
        return [root.val] + f(root.left) + f(root.right) if root else []
        
# 方法二： 迭代版本

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                ans.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return ans
