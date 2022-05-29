func removeElement(nums []int, val int) int {
    var res = -1
    for idx, num := range nums {
        if num != val {
            res++
            if res != idx {
                nums[idx], nums[res] = nums[res], nums[idx]
            }
        }
    }

    return res + 1
}
