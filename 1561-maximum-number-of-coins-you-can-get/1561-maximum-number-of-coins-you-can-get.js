/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort(function(a, b){return a - b})
    let r=piles.length - 2
    const times=(piles.length)/3
    let ans=0
    
    for (let i=0; i<times; i+=1){
        ans+=piles[r]
        r-=2
    }
    return ans
    
};