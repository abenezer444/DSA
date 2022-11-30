/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    var len=nums.slice()
    for (let i of nums){
        len.push(i)
    }
  
    
    
    
    return len
    
};