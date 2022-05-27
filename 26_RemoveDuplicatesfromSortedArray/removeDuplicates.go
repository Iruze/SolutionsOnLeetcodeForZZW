func removeDuplicates(nums []int) int {
    // 快慢指针解法, pre指向当前不重复的元素的索引
    pre := 0
    for idx, _ := range nums {
        if pre < idx && nums[pre] != nums[idx] {
            pre += 1
            nums[pre] = nums[idx]
        }
    }

    return pre + 1
}
