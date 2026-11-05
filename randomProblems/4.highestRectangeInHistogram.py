import subprocess
subprocess.run('cls', shell=True)

def largestRectangleArea(heights):
    stack = []
    maxArea = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width
            maxArea = max(maxArea, area)

        stack.append(i)

    return maxArea

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))