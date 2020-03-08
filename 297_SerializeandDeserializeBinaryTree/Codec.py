# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '#,'
        res = str(root.val) + ','
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _deserialize(l):
            if not l: return None
            cur = l.pop(0)
            if cur == '#': return None
            root = TreeNode(int(cur))
            root.left = _deserialize(l)
            root.right = _deserialize(l)
            return root
        l = data.strip(',').split(',')
        return _deserialize(l)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
