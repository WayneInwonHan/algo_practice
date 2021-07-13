var kthGrammar = function(N, K) {
    if (N === 1 && K === 1) return 0;
    
    let aboveK = Math.round(K/2);
    const value = kthGrammar(N-1, aboveK);
    
    if (value === 0) {
        if (K % 2 === 0) {
            return 1;
        } else {
            return 0;
        }
    } else {
        if (K % 2 === 0) {
            return 0;
        } else {
            return 1;
        }
    }
};