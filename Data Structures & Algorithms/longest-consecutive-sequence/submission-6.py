class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_set = set(nums)
        maxf = 0
        for i in s_set:
            le = 0
            if(i-1 not in s_set):
                le +=1
                while(i+le in s_set):
                    le+=1
                maxf = max(maxf,le)
        return maxf