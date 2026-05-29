class Solution:
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                oldDay = stack.pop()

                ans[oldDay] = i - oldDay

            stack.append(i)

        return ans