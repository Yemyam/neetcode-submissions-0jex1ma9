class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0
        while p2 > p1:
            # compute area
            height = min(heights[p1], heights[p2])
            width = p2-p1
            area = height * width
            max_area = max(max_area, area)
            if heights[p1] >= heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return max_area