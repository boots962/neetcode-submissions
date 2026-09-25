class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1

        lmax = 0
        rmax = 0
        trapped = 0
        while start<=end:
            lmax = max(lmax, height[start])
            rmax = max(rmax, height[end])

            if lmax<rmax:
                trapped += lmax-height[start]
                start+=1
            else:
                trapped += rmax-height[end]
                end-=1
            
            
        return trapped
