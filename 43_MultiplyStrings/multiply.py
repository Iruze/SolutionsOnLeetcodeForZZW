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
