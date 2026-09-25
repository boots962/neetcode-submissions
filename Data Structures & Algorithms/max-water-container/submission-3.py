class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        b = 0
        e = len(heights)-1
        while b <=e:
            area = max(min(heights[e], heights[b])*(e-b), area)

            if heights[b]<=heights[e]:
                b+=1
            else:
                e-=1
        return area