/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let len=nums
    nums.push(...len)
    
    return nums
    
};