class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = [0] * 2 * (len(nums))
        for i, num in enumerate(nums):
            answer[i] = num
            answer[i+(len(nums))] = num
        return answer
