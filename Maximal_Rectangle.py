class Solution:

    def largestRectangleArea(self, heights):
        stack = []
        maxi = 0
        index = 0
        
        while index < len(heights):
            # Push to stack if current height is greater than the height of the bar at stack top
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top
                top_of_stack = stack.pop()
                # Calculate the area with heights[top_of_stack] as the smallest height bar 'h'
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                # Update max area, if needed
                maxi = max(maxi, area)
        
        # Now, pop the remaining bars from stack and calculate area with every popped bar
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            maxi = max(maxi, area)
        
        return maxi

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        
        # Create a 2D array to store the heights of columns
        presum = [[0] * m for _ in range(n)]
        
        # Compute the heights for each column
        for j in range(m):
            colsum = 0
            for i in range(n):
                if matrix[i][j] == '1':
                    colsum += 1
                else:
                    colsum = 0
                presum[i][j] = colsum
        
        # Compute the maximum area for each row's histogram
        for i in range(n):
            max_area = max(max_area, self.largestRectangleArea(presum[i]))
        
        return max_area

# Test case
matrix = [    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]


obj = Solution()
ans = obj.maximalRectangle(matrix)

print(ans)  
