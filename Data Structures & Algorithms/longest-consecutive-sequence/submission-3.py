class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return
        cap = set(nums)

        pen = 0
        for num in cap:
            if num - 1 not in cap:
                counter = 0
                current = num

                while current in cap:
                    counter += 1
                    current += 1
                pen = max(pen, counter)   
        
        return pen