def hammingDistance(self, x, y):
    ans = 0
    for i in range(31,-1,-1):
        b1 = x>>i&1
        b2 = y>>i&1
        ans += not(b1==b2)
    return ans