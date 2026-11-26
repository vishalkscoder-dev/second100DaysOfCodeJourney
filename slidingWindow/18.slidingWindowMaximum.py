from collections import deque

import subprocess
subprocess.run('cls', shell=True)

def maxSlidingWindow(nums, k):
    left = 0
    check = deque()
    result = []

    for right in range(len(nums)):
        while check and nums[check[-1]] < nums[right]:
            check.pop()

        check.append(right)

        if check[0] < left:
            check.popleft()

        if right - left + 1 == k:
            result.append(nums[check[0]])

            left += 1

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums,k))