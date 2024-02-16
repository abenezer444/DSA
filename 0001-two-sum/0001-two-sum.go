func twoSum(nums []int, target int) []int {
    
    seen := make(map[int]int)
    
    for index, num := range nums{
        compliment := target - num
        
        compliment_index, ok := seen[compliment]
        
        if ok {
            return []int{index,compliment_index}
        }
        seen[num] = index
    }
    return nil
}