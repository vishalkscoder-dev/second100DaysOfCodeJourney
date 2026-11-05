import subprocess
subprocess.run('cls', shell=True)


def countFairPairs(nums, lower, upper):
    nums.sort()

    left = 0
    right = len(nums)-1
    count = 0

    while left < right:
        if nums[left] + nums[right] <= upper:
            count += right - left
            left += 1
        else:
            right -= 1

    upperCount = count

    left = 0
    right = len(nums)-1
    count = 0

    while left < right:
        if nums[left] + nums[right] < lower:
            count += right - left
            left += 1
        else:
            right -= 1

    lowerCount = count

    return upperCount - lowerCount        

nums = [0,1,7,4,4,5]
lower = 3
upper = 6

print(countFairPairs(nums, lower, upper))