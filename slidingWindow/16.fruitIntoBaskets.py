import subprocess
subprocess.run('cls', shell=True)

def totalFruit(fruits):
    left = 0
    basket = {}
    maxFruits = 0

    for right in range(len(fruits)):

        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        while len(basket) > 2:

            basket[fruits[left]] -= 1

            if basket[fruits[left]] == 0:
                del basket[fruits[left]]

            left += 1

        maxFruits = max(maxFruits, right - left + 1)

    return maxFruits


fruits = [1,2,3,2,2]

print(totalFruit(fruits))
