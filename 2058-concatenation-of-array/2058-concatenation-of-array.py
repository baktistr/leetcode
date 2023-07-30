class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        print(nums)
        answer = []
        for i in range(len(nums)):
            answer.append(nums[i])
        for i in range(len(nums)):
            answer.append(nums[i])
        return answer