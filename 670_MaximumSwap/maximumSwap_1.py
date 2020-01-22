# solution1:
# 思路： 先将num转化为字符数组num_str，排降序num_strmax，比对排序前后不相同的字符，交换这个两个字符
#       num_strmax的idx处的大数放在num_str的idx处，同时找到大数在num_str中最后一次出现的地方idx1
#       在idx1处放上小数num_str[idx]

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        num_strmax = sorted(num_str, reverse=True)
        for idx in range(len(num_str)):
            if num_str[idx] != num_strmax[idx]:
                idx1 = - num_str[::-1].index(num_strmax[idx]) - 1
                num_str[idx1] = num_str[idx]
                num_str[idx] = num_strmax[idx]
                break
        return int(''.join(num_str))
