import random

class Solution(object):
    def __init__(self, nums):
        self.original = [x for x in nums]
        self.temp = nums
        self.indices = [x for x in range(len(nums))]
    def reset(self):
        return self.original
    def shuffle(self):
        if not len(self.temp):
            return []
        i = random.choice(self.indices)
        j = random.choice(self.indices)
        self.temp[i], self.temp[j] = self.temp[j], self.temp[i]
        return self.temp