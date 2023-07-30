class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        answer=[]
        for i in range(len(nums)):
            # answer[i] = nums[nums[i]]
            answer.append(nums[nums[i]])
        return answer