class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                
                max_area = max(h, max_area)
            
            elif h >= stack[-1][1]:
                stack.append((i, h))
                # h < stack[-1][1]
            else:
                start, start_height = stack.pop()
                width = i - start
                popped_area = width * start_height
                max_area = max(max_area, popped_area)
                while stack and h < stack[-1][1]:
                    start, start_height = stack.pop()
                    width = i - start
                    area = width * start_height
                    max_area = max(max_area, area)
                stack.append((start, heights[i]))
        
        total_w = len(heights)
        for i, h in stack:
            w = total_w - i
            a = h * w
            max_area = max(max_area, a)
    
        return max_area
