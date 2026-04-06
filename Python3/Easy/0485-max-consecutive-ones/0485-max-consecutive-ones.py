class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        count = 0
        for num in nums:
            count +=1
            if num == 0:
                count =0
            maxx = max(count,maxx)
        return maxx
         