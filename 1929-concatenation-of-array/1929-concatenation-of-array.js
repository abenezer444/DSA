/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    var len=nums
    nums.push(...len)
    
    return nums
    
};