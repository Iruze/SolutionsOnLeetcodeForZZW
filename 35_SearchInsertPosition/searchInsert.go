func searchInsert(nums []int, target int) int {
    // 标准的二分法，注意right取值len(nums)
    // 包含了target>nums[-1]的测试用例
    left, right := 0, len(nums)
    for left < right {  // while在go中不是关键字
        mid := left + (right - left) >> 1
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }

    return left
}
