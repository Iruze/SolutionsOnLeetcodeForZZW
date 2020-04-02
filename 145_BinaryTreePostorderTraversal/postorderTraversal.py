# 方法一： 递归版本

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        f = self.postorderTraversal
        return f(root.left) + f(root.right) + [root.val] if root else []
        
# 方法二：迭代版本

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        cur = root
        # 按照从头插入的顺序：根-右-左
        while cur or stack:
            while cur:
                ans.insert(0, cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop().left
        return ans
