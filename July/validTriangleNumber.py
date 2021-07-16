class Solution:
    def triangleNumber(self, nums):
        n=len(nums)
        if n<3:
            return 0
        nums=sorted(nums)
        nums=nums[::-1]
        count=0
        for i in range(0,n-2):
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    count+=(right-left)
                    left+=1
                else:
                    right-=1
        return count

