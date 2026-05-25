class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for n in nums:
            map[n]=map.get(n,0)+1
            res=sorted(map,key=map.get,reverse=True)
        return res[:k]