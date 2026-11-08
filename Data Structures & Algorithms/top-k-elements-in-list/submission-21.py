class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0)+1
        
        sortmap = sorted(hmap.items(), key = lambda x:x[1], reverse = True)
        ls=[]
        i=0
        for i in range(k):
            ls.append(sortmap[i][0])
        return ls