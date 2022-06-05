func plusOne(digits []int) []int {
    n := len(digits)
    carry := 0
    var sum int
    for i := n - 1; i >= 0; i-- {
        // 此处也可以初始化carry为1，把加的1当做低位进位来的1
        // 如此，只有 sum = digits[i] + carray 这一个式子，无需判断i == n - 1
        if i == n - 1 {
            sum = digits[i] + carry + 1
        } else {
            sum = digits[i] + carry
        }
        // 十进制模拟
        digits[i], carry = sum % 10, sum / 10
        // 最后的进位完毕，提前返回
        if carry == 0 {
            return digits
        }
    }
    // 此时digits是100,100,1000...这种数
    digits = make([]int, n + 1)
    digits[0] = 1
    
    return digits
}
