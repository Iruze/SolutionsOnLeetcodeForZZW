# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        ans = []
        def collect(root):
            if not root: return '#'
            # 因为是前序遍历，得到了每个子树开头的序列化
            serial = '{}, {}, {}'.format(root.val, collect(root.left), collect(root.right))
            count[serial] += 1
            # 不用>=2，避免append重复，=2涵盖了>=2
            if count[serial] == 2:
                ans.append(root)
            return serial
        collect(root)
        return ans
