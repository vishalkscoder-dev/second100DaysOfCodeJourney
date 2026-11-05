import subprocess
subprocess.run("cls", shell=True)

def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    answer = n * [0]

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()

            answer[prev] = i - prev

        stack.append(i)

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))