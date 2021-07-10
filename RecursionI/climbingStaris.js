var climbStairs = function(n) {
    let map = new Map();
    if(n === 1) return 1;
    if(n === 2) return 2;
    if(map.has(n)){
    	return map.get(n);
    }else{
        let value = climbStairs(n - 1) +climbStairs(n - 2);
        map.set(n,value);
        return value;
    }
};