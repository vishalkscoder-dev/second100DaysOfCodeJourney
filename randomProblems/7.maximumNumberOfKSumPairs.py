import subprocess
subprocess.run('cls', shell=True)

def maxOperations(nums, k):
    freq = {}
    count = 0

    for num in nums:
        complement = k - num

        if freq.get(complement, 0) > 0:
            count += 1
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1

    return count

nums = [1,2,3,4]
k = 5

print(maxOperations(nums,k))