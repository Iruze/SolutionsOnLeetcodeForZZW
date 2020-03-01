"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    global pLastNodeInList
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        global pLastNodeInList
        pLastNodeInList = None
        self.__convertNode(root)
        pHeadNodeInList = pLastNodeInList
        while pHeadNodeInList and pHeadNodeInList.left:
            pHeadNodeInList = pHeadNodeInList.left
        pHeadNodeInList.left, pLastNodeInList.right = pLastNodeInList, pHeadNodeInList
        return pHeadNodeInList
    
    def __convertNode(self, root):
        if not root: return
        global pLastNodeInList
        pCurrNode = root
        if pCurrNode.left:
            self.__convertNode(pCurrNode.left)
        pCurrNode.left = pLastNodeInList
        if pLastNodeInList:
            pLastNodeInList.right = pCurrNode
        pLastNodeInList = pCurrNode
        if pLastNodeInList.right:
            self.__convertNode(pLastNodeInList.right)

# 写法二：
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def _convert(root):
            if not root:
                return
            _convert(root.left)
            root.left = self.last
            if self.last:
                self.last.right = root
            self.last = root
            _convert(root.right)
        # 调用_convert()函数
        if not root:
            return
        self.last = None
        _convert(root)
        head = self.last
        while head and head.left:
            head = head.left
        head.left, self.last.right = self.last, head
        return head
