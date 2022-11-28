/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    var len=nums.length
    for (var i=0; i<len;i+=1){
        nums.push(nums[i]);
    }
    return nums
    
};