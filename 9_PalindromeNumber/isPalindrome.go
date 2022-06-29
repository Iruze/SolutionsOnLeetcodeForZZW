func isPalindrome(x int) bool {
    if x < 0 || (x % 10 == 0 && x != 0) {
        return false
    }

    revertedNum := 0
    for x > revertedNum {
        revertedNum = revertedNum * 10 + x % 10
        x /= 10
    }

    // 当x为奇数对称，比如12321的时候，x=12， revertedNum=123
    return x == revertedNum || x == revertedNum / 10
}
