import subprocess
subprocess.run('cls', shell=True)

def maxArea(height):
    left = 0
    right = len(height) - 1

    maxArea = 0

    while left < right:
        width = right - left

        h = min(height[left], height[right])

        area = width * h

        maxArea = max(area, maxArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))