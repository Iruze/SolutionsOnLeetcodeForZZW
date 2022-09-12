import "strconv"

// 模拟加法的对位相加 + 进位 的运算过程
func addBinary(a string, b string) string {
    i, j := len(a) - 1, len(b) - 1
    ans := ""

    var a1, b1, sum, carry int
    for i >= 0 || j >= 0 {
        // a1提前结束，则当前位置0
        if i < 0 {
            a1 = 0
        } else {
            a1, _ = strconv.Atoi(string(a[i]))
        }
        // b1提前结束，则当前位置0
        if j < 0 {
            b1 = 0
        } else {
            b1, _ = strconv.Atoi(string(b[j]))
        }

        sum = a1 + b1 + carry
        // 结算下一轮对位相加的进位
        carry = sum / 2
        // 当前位结果 = 总和sum模2
        ans = strconv.Itoa(sum % 2) + ans

        // 下标左移，准备下一轮扫描
        i, j = i - 1, j - 1
    }

    // 上面的结果ans第一位是字符"0"，有进位，则要加入进位"1"
    if carry > 0 {
        ans = "1" + ans
    }

    return ans
}
