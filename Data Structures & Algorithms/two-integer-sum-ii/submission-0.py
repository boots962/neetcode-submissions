class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comp = {}
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in comp:
                return [comp[diff], i+1]
            else:
                comp[n] = i+1
        return []