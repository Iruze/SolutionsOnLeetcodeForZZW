"""
python3 单调栈解法 官方说是滑动窗口，但是我觉得不是传统意义上的sliding window，更应该是单调栈主题解法。 
官网说的两个性质，个人理解就是贪心思想，最短子数组下标区间是[x1, x2]， 双栈deque存储的是左端x1。
举个例子，如果当前deque存储的对应值为[1, 3, 4], 等待入栈的值为2， 则栈内的3, 4一定要弹出，
因为如果不弹出得栈[1, 3, 4, 2]，如果后面等待入栈的值和3, 4的差>=K, 那么和2的差更应该>=k， 
但是3， 4显然不是最短的子数组，所以3， 4必须要弹出，deque必须要维护为一个严格单调递增的栈：
"""

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        n = len(A)
        presum = [0 for _ in range(n + 1)]
        for i in range(n):
            presum[i + 1] = presum[i] + A[i]
        
        deque = collections.deque()
        
        ans = n + 1
        for i, v in enumerate(presum):
            
            # 维护单调递增栈
            while deque and presum[deque[-1]] >= v:
                deque.pop()
            # 从最小值作为减数开始
            while deque and presum[deque[0]] + K <= v:
                # 注意此处是前缀和，求长度无需加1： i - deque.popleft() + 1
                ans = min(ans, i - deque.popleft())
            
            deque.append(i)
        
        return ans if ans < n + 1 else -1
