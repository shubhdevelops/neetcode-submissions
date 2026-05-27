class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        need = Counter(t)
        window = Counter()

        left = 0
        ans = ""

        for right in range(len(s)):

            window[s[right]] += 1

            while window >= need:

                temp = s[left:right+1]

                if ans == "" or len(temp) < len(ans):
                    ans = temp

                window[s[left]] -= 1
                left += 1

        return ans