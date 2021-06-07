def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    return list(set([x for x in range(1, len(nums)+1)]) - set(nums))