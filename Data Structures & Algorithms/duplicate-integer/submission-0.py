class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh = []
        for i in nums:
            if i in hsh:
                return True
            hsh.append(i)
        return False
