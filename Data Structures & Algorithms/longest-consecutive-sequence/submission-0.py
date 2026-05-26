class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for n in s:

        
            if n - 1 not in s:

                count = 1

                while n + 1 in s:
                    n += 1
                    count += 1

                ans = max(ans, count)

        return ans