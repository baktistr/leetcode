class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        answer = 0
        # i = 0
        for i in range(len(s)):
            if i < len(s)-1  and mapping[s[i]] < mapping[s[i+1]]:
                answer -= mapping[s[i]]
            else:
                answer += mapping[s[i]]
                    
        return answer