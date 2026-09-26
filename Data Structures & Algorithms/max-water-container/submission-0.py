class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = subtraction of indices 
        # height = min(val, val)
        # store = width * height 
        width, height = 0, 0
        l, r = 0, len(heights) - 1
        initial_cap = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            cap = width * height
            if cap > initial_cap:
                initial_cap = cap 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return initial_cap