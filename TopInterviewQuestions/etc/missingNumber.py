class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        high = len(nums)
        low = 0
        while low<high:
            mid = low + (high-low)//2
            if nums[mid]>mid:
                high = mid
            else:
                low = mid+1
        return low