/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    
    // sort the array
    nums.sort(function(a,b) {  
        return a-b;         
    });    
    
    // find Index
    let index = nums.findIndex(x => x >= target); 
    
    // if target is Max than elements
    if (index === (-1)) {
        index = nums.length;
    }

    return index;
};
