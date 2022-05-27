func twoSum(nums []int, target int) []int {
    hashTable := map[int]int{}
    for idx, num := range nums {
        if p, ok := hashTable[target - num]; ok {
            return []int{p, idx}
        }
        
        hashTable[num] = idx
    }

    return nil
}
