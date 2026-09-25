class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        large = 0
        
        for n in numss:
            if n-1 not in numss:
                curr = n
                t = 1
                while curr+1 in numss:
                    curr+=1
                    t +=1
                large = max(large, t)
        return large