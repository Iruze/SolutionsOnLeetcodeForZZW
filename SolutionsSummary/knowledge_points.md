# knowledage points
- 中位数计算公式
```shell script
# n无论奇,偶
mid = (nums[n // 2] + nums[(n - 1) // 2]) / 2.0
```

- 主对角线 & 副对角线 规律
```shell
# 主对角线，坐标之和相等
# 副对角线，坐标之差相等
{r + c} | u_diag, {r - c} | d_diag)
```

- 数独在3*3小宫格内遍历
```python
for i in range(9):
    ......
    r1 = (r // 3) * 3 + i // 3
    c1 = (c // 3) * 3 + i % 3
    ......
```

- 快速找到**链表中点**
```python
# 快慢指针
def midLinkList(head):
    if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # mid是slow
        # 1 2 3 4 5 6： mid=3(偏左)
        # 1 2 3 4 5:    mid=3(居中)
        return slow
```

- 计算`list`中点的小小区别
```python
mid = len(nums) // 2   # 偏右， [1, 2, 3, 4]， mid=3

mid = left + (right - left) // 2
# 或
mid = left + ((right - left) >> 1)   # 偏左， [1, 2, 3, 4]， mid=2
