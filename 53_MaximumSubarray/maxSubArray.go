import "math"

func maxSubArray(nums []int) int {
    curSum, maxSum := math.MinInt, math.MinInt
    for _, num := range nums {
        if curSum < 0 {
            curSum = num
        } else {
            curSum += num
        }

        // go语言中没有:?三元表达式
        // go中Max, Min函数是针对float64类型数据的
        if maxSum < curSum {
            maxSum = curSum
        }
    }

    return maxSum
}
