class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            print(sorted_word)
            if sorted_word not in anagram:
                anagram[sorted_word] = []
            anagram[sorted_word].append(word)

        print(anagram)
        print(anagram.values())

        return(list(anagram.values()))