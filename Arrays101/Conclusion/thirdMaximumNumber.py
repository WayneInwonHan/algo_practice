def thirdMax(self, nums: List[int]) -> int:
    a = sorted(nums)
    set(a)
    
    if len(a)<=2:
        return a[1]
    else:
        return a[len(a)-3]