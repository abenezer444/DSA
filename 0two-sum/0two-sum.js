/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let dict={}
    for (let i=0; i<nums.length; i+=1){
        let diff=target-nums[i]
        if (diff in dict){
            return [i,dict[diff]]
        }else{
            dict[nums[i]]=i
        }
    }
};