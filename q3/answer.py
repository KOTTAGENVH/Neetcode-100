#YTB Link: https://youtu.be/KLlXCFG5TnA?si=IIgus7oN3W0CICZ9
from typing import List


class Solution:
    def twoSum( nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index
        for i, n in enumerate(nums): #enumerate gives us both index and value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
    
print("two Sum: ", Solution.twoSum([2,7,11,15], 9))
# Time Complexity: O(n)
# Space Complexity: O(n)
# The time complexity of the twoSum function is O(n) because it iterates through the list of numbers once,
# and the space complexity is O(n) because it uses a dictionary to store the indices of the numbers.

