func mySqrt(x int) int {
    if x <= 0 {
        return x
    }

    lo, hi := 1, x
    var mid int
    for lo < hi {
        mid = lo + (hi - lo) >> 1
        if mid * mid == x || hi - lo == 1 {
            return mid
        } else if mid * mid < x {
            lo = mid
        } else {
            hi = mid
        }
    }

    return lo
}
