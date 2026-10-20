class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = dict()
        cap = [0] * 2

        for i in range(len(numbers)):
            if int(target - numbers[i]) in map:
                cap[1] = i + 1
                cap[0] = map.get(target - numbers[i]) + 1
                return cap
            map[numbers[i]] = i
        return cap.sort()