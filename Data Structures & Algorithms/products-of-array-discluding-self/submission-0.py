class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= suffix
            suffix *= nums[i]

        return arr
