class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        思路: 以 5014 为例, 计算 "十位" 上的1的个数, 分为两部分:
        hight = 501, low = 4
        第一部分-高位:
            [0-49]1[0-9]   一共 50 = hight // 10 *digit
            考虑到如果是 5024的话, 实际高位是 
            [0-50]1[0-9]    所以需要比较"十位"上的数和目标数target的关系, 如果 "十位" > target, 则[]高位总数+1], 否则[高位总数-1]
            所以只需要加上修正因子 offset = 9 - target,
            最终高位总数 = (hight + offset) // 10 * digit
        
        第二部分-低位:
            计算完了高位[0-49]1[0-9], 低位就是 [50]1[0]-[50]1[4]了, 和明显是 4 + 1个, 但是如果 "十位" < target,
            也就是如果是计算"2"的个数的话, 那么[50]1[0]-[50]1[4]就是0个了
            所以, 
            最终低位总数 = low + 1 if hight % 10 == target else 0 
        """

        if n == 0:
            return 0
        if n <= 9:
            return 1
        digit = 1
        cnt = 0
        target = 1
        offset = 9 - target
        while digit <= n:
            hight, low = n // digit, n % digit
            cnt += (hight + offset) // 10 * digit + (low + 1 if hight % 10 == target else 0)
            digit *= 10
        return cnt
