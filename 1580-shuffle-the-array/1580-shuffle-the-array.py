class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer=[]
        x=[]
        y=[]
        for i in range(n):
            x.append(nums[i])
        
        for i in range(n, len(nums)):
            y.append(nums[i])
        
        for i in range(n):
            answer.append(x[i])
            answer.append(y[i])
        
        return answer

        return 0
