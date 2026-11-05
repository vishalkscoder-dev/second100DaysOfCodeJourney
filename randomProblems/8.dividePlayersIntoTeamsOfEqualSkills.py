import subprocess
subprocess.run('cls', shell=True)

def dividePlayers(skill):
    skill.sort()

    n = len(skill)
    total = 0

    target = skill[0] + skill[n-1]

    left = 0
    right = n - 1

    while left < right:
        if skill[left] + skill[right] != target:
            return -1
        else:
            total += skill[left] * skill[right]

            left += 1
            right -= 1

    return total


skill = [3,2,5,1,3,4]
print(dividePlayers(skill))



        