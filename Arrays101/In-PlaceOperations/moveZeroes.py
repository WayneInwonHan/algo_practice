def moveZeroes(self, nums):
    insert_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_index]=nums[i]
            insert_index+=1
    for i in range(insert_index,len(nums)):
        nums[i]=0