二叉树大部分使用递归解法

### 二叉树的高度

- [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最大深度。    
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明**: 叶子节点是指没有子节点的节点。

示例：

```
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 
```

直接看code

```python3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0     # base case 是 root = None
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### 判断是否为平衡二叉树

- [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是高度平衡的二叉树。     
本题中，一棵高度平衡二叉树定义为：       
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

```
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
```

code

```python3
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root: return 0
            return 1 + max(depth(root.left), depth(root.right))
        if not root: return True
        # 判断条件：left平衡 && right平衡 && abs(left - right) < 2
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(depth(root.left) - depth(root.right)) < 2
```

### 二叉树的直径

- [543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/)

> 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :

```
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
```

**注意**：两结点之间的路径长度是以它们之间边的数目表示。

```python3
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        # depth 函数返回的是高度，但是同时实现了直径 Diameter 的计算
        def depth(root):
            if not root: return 0
            l, r = depth(root.left), depth(root.right)
            
            # 去掉这一句，就是求高度 depth 函数的本质
            # 然而，直径正好 = l + r
            self.diameter = max(self.diameter, (l + r))
            
            return 1 + max(l, r)
        depth(root)
        return self.diameter
```
