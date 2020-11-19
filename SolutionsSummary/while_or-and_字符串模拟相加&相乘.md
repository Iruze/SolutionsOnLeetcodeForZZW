### 模拟相加
> 要点：
```python3
1) or循环
    while n1 >= 0 or n2 >= 0
2) 当前位累加
    tmp = n1 + n2 + carry
    carry = tmp // 10
    res = str(tmp % 10) + res
3) 是否有进位：
    return res if not carry else '1' + res
```
- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
> 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
>
>注意：

>num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

解法一： `while n1 > 0 and n2 > 0` 的解法：
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        flag = 0
        n1, n2 = len(num1),len(num2)
        res = ''
        while n1 > 0 and n2 > 0:
            s = int(num1[n1 - 1]) + int(num2[n2 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n1, n2 = n1 - 1, n2 - 1
        while n1 > 0:
            s = int(num1[n1 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n1 -= 1
        while n2 > 0:
            s = int(num2[n2 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n2 -= 1
        if flag:
            res = '1' + res
        return res
```
这种解法，用了3个while:
```python
while n1 and n2
while n1
while n2
```


解法二： `while n1 > 0 or n2 > 0` 的解法：
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
```
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
> 给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
示例 1:
```
输入: a = "11", b = "1"
输出: "100"
```
解法：
```python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i, j = i - 1, j - 1
        return res if not carry else '1' + res
```
### 模拟相乘
> 要点：
```python3
1) O(M*N)双循环
    for i in range(len(nums1) - 1, -1, -1)
        ...
        for j in range(len(nums2) - 1, -1, -1):
2) num1上的第i位数 * num2上的第j位数
   结果是两位数，分别在第 i+j, 第 i+j+1 位上
    total = res[i + j + 1] + n1 * n2
    res[i + j + 1] = total % 10
    res[i + j] += total // 10
3) 去掉前缀'0'
    res.lstrip('0')
```
- [43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)
> 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
>示例 1:
```shell
输入: num1 = "2", num2 = "3"
输出: "6"
```
>示例 2:
```shell
输入: num1 = "123", num2 = "456"
输出: "56088"
```
解答：
```python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        # num1上的第i位数 * num2上的第j位数
        # 结果是两位数，分别在第 i+j, 第 i+j+1 位上
        for i in range(len(num1) - 1, -1, -1):
            n1 = int(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                n2 = int(num2[j])
                total = res[i + j + 1] + n1 * n2
                # 当前位 i+j+1 上的十进制值
                res[i + j + 1] = total % 10
                # 计算 i+j 的进位
                res[i + j] += total // 10
        # 整数列表转换为字符串
        res = ''.join(map(str,res))
        # 返回前，去掉前缀'0'
        return res.lstrip('0')
```
**当然也有，`while l1 and l2`的`and`型的：**         
-[21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
> 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。            

示例：
```shell
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```
迭代解法：
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pNode = dummy
        while l1 and l2:
            if l1.val < l2.val:
                pNode.next = l1
                l1 = l1.next
            else:
                pNode.next = l2
                l2 = l2.next
            pNode = pNode.next
        pNode.next = l1 if l1 else l2
        return dummy.next
```

### 归并排序

<details>
    <summary>while-or解法</summary>
    
```python
class Solution:

    def merge_sort(self, nums):
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
    

    def merge(self, left, right):
        i, j = 0, 0
        tmp = []
        while i < len(left) or j < len(right):
            if j == len(right) or i < len(left) and left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        return tmp
```
</details>

<details>
    <summary>while-and解法</summary>
    
```java
import java.lang.Math;


public class MergeSort {
    public void sort(int[] arr) {

        if(arr == null) return;

        int[] temp = new int[arr.length];
        int left_min, left_max, right_min, right_max;

        //步长 
        for(int i = 1; i < arr.length; i = i * 2) {
            for(left_min = 0; left_min < arr.length - i; left_min = right_max) {

                left_max = right_min = left_min + i;
                right_max = Math.min(arr.length, right_min + i);

                int t = 0;
                while(left_min < left_max && right_min < right_max) {
                    temp[t++] = arr[left_min] < arr[right_min]? arr[left_min++]: arr[right_min++];
                }

                //如果Lmin 没有走到LMAX的位置 说明L还有元素 
                while(left_min < left_max) {
                    arr[--right_min] = arr[--left_max];
                }

                while(t > 0) {
                    //把整个数组还原到 刚刚剩下那个最大元素的后面 
                    arr[--right_min] = temp[--t];
                }
            }
        }
    }
}
```
</details>
