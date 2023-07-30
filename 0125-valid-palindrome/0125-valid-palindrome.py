class Solution:
    def isPalindrome(self, s: str) -> bool:

         pattern = r'[^a-zA-Z0-9]'
         s = re.sub(pattern, '', s.lower())
        #  print(s)
        #  print(s[::-1])
         return s == s[::-1]