import subprocess
subprocess.run('cls', shell=True)

def numRescueBoats(people, limit):
    people.sort()

    left = 0
    right = len(people)-1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats

people = [3,5,3,4]
limit = 5

print(numRescueBoats(people, limit))
