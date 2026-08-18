class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        setNums = sorted(list(set(nums)))
        if setNums == nums:
            return False
        else:
            return True 