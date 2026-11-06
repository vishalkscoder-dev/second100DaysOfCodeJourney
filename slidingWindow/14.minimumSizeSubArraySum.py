import subprocess
subprocess.run('cls', shell=True)

def minSubArrayLen(target, nums):
    left = 0
    minLength = float('inf')
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            minLength = min(minLength, right-left+1)

            total -= nums[left]

            left += 1

    if minLength == float('inf'):
        return 0

    return minLength

target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))


        
        