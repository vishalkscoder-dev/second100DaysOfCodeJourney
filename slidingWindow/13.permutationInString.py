import subprocess
subprocess.run('cls', shell=True)

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    if s1Count == s2Count:
        return True

    left = 0

    for right in range(len(s1), len(s2)):
        s2Count[ord(s2[right]) - ord('a')] += 1
        s2Count[ord(s2[left]) - ord('a')] -= 1

        left += 1

        if s2Count ==  s1Count:
            return True

    return False

s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1,s2))





        