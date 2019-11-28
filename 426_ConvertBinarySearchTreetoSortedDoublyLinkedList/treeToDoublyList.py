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
