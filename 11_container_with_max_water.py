
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l,r = 0, len(heights) -1
        while l<r:
            myarea=(r-l)*min(heights[r], heights[l])
            result = max(result,myarea)
            if heights[l]>=heights[r]:
                r -=1 
            else:
                l+=1
        return result
        