class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        answer = [0] * len(arr)
        right = -1
        for i in range (len(arr)-1, -1, -1):
            answer[i] = right
            right = max(arr[i], right)
        return answer