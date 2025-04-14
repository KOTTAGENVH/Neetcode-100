#Actual Time complexity: O(m*n)
#Time complexity: O(m*n*26)
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #Default dictionary
      res = defaultdict(list) #Defaultdics automatically configures the key.

      #iterate the words
      for s in strs:
        count = [0] * 26 # Having 26 zeros A-Z
        #iterate over the letters in the word
        for c in s:
         count[ord(c.lower()) - ord("a")] += 1

        res[tuple(count)].append(s)
    
      return res.values()

sol = Solution()
print (sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
