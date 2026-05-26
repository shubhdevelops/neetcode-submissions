class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        need=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            window=s2[i:i+len(s1)]
            if Counter(window)==need:
                return True
        return False