class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i]+1 not in s:
                l = 1
                while nums[i]-l in s: 
                    l+=1
                count = max(count,l)
        return count