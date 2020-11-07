二叉树大部分使用**递归**解法

## 二叉树的高度

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

<details>
    <summary>解法</summary>
    
```python3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0     # base case 是 root = None
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

</details>

## 判断是否为平衡二叉树

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
<details>
    <summary>解法</summary>
    
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

</details>

## 二叉树的直径

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

<details>
    <summary>解法</summary>
    
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

</details>

## 二叉树的坡度

- [563. 二叉树的坡度](https://leetcode-cn.com/problems/binary-tree-tilt/)

> 给定一个二叉树，计算**整个树**的坡度。         
一个树的**节点的坡度**定义即为，该节点左子树的结点之和和右子树结点之和的**差的绝对值**。空结点的的坡度是0。          
**整个树**的坡度就是其所有节点的坡度之和。     

示例:

```
输入: 
         1
       /   \
      2     3
输出: 1
解释: 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
```

本题跟上一题 **二叉树的直径** 思路一样，本题中 `titl`函数返回本节点的总和，实际捎带计算了当前节点的坡度

<details>
    <summary>解法</summary>
    
```python3
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        def tilt(root):
            if not root: return 0
            l, r = tilt(root.left), tilt(root.right)
            
            # 去掉这一句，tilt函数本质是返回节点总和
            # 然而，坡度正好=abs(l - r), 故而捎带计算坡度
            self.tilt += abs(l - r)
            
            return l + r + root.val
        tilt(root)
        return self.tilt
```
</details>

## 二叉树中不相邻节点的最大总和

**实质就是：　打家劫舍III，跟上面的内置函数tilt()一样，在求root当前节点的同时还做了其他的事情**
  - [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)
  > 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。       
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。         

示例 1:
```
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
```

<details>
    <summary>解法</summary>
    
```python3
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            """
            找到打劫root节点和不打劫root的总和: [不打劫, 打劫]
            """
            if not root: return [0, 0]
            #　分别求左右节点打劫&不打劫的结果: [左不打劫, 左打劫], [右不打劫, 右打劫]
            l, r = helper(root.left), helper(root.right)
            #　root不打劫 = 左打劫 + 右打劫
            #  root打劫 = root.val + 左不打劫 + 右不打劫
            #  故, 返回 [root不打劫, root打劫]
            return [max(l) + max(r), root.val + l[0] + r[0]]
        # 最终结果取 [root不打劫, root打劫] 的最大值
        return max(helper(root))
```

</details>

## 二叉树的序列化
- [652. 寻找重复的子树](https://leetcode-cn.com/problems/find-duplicate-subtrees/)
> 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。          
两棵树重复是指它们具有相同的结构以及相同的结点值。

<details>
    <summary>解法</summary>
    
```python3
class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def collect(node):
            # 前序遍历
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            
            # 这边三句是在前序遍历中，捎带统计序列化
            # 去掉这三句则是前序遍历
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            
            # 返回捎带计算的结果
            return serial

        collect(root)
        return ans

# 序列化二叉树的步骤
"""
def collect(node):
    if not node: return "#"
    serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
    return serial
    
其中
    count[serial] += 1
    if count[serial] == 2:
        ans.append(node)
才是顺带求取
"""
```

</details>
