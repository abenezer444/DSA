func twoSum(nums []int, target int) []int {
    
    var ans []int;
    
    for i, num := range nums{
        for j,num_ := range nums{
            if i != j && num + num_ == target{
                ans = append(ans,i)
            }
        }
    }
    return ans
    
}