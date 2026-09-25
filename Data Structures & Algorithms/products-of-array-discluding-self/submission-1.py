class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zcount = 0
        for i in nums:
            if i !=0:
                prod*=i
            if i == 0:
                zcount+=1

        if zcount >= 2:
            return [0] * len(nums)
        num = []
        
        for i in nums:
            if zcount == 1:
                if i == 0:
                    num.append(prod)
                else:
                    num.append(0)
            else:
                num.append(prod//i)
        return num