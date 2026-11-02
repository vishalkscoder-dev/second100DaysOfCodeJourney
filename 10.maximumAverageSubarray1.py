import subprocess
subprocess.run('cls', shell=True)

def findMaxAverage(nums, k):
    total = 0

    for i in range(k):
        total += nums[i]

    maxSum = total

    for i in range(k, len(nums)):
        total += nums[i]
        total -= nums[i - k]

        maxSum = max(maxSum, total)

    return float(maxSum) / k

nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))
