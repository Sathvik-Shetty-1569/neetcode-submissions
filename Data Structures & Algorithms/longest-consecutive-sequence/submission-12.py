class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        snums = list(set(nums))
        snums.sort()
        maxf = 1
        for i in range(1, len(snums)):
            if snums[i-1]+1 != snums[i]:
                count = 1
                maxf = max(count , maxf)
            else :
                count+=1
                maxf = max(maxf,count)
        return maxf