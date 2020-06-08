class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # 前序遍历得到序列化
        if not root: return '# '
        ans = str(root.val) + ' '
        ans += self.serialize(root.left)
        ans += self.serialize(root.right)
        return ans
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(data):
            if not data: return None
            cur = data.pop(0)
            if cur == '#': return None
            # 前序遍历二叉树序列化字符串，还原二叉树
            root = TreeNode(int(cur))
            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data.split(' '))
