#Check this  O(n)
from typing import List
from functools import reduce

class Solution:
    def array_except_self(self, number: List[int]) -> List[int]:
        outStore: List[int] = []

        for i in range(len(number)):
            tempStore = number.copy()   # make a copy so original list isn't affected
            del tempStore[i]            # remove the element at index i
            product = reduce(lambda x, y: x * y, tempStore)
            outStore.append(product)

        return outStore

sol = Solution()
print("OutStore:", sol.array_except_self([1, 2, 3, 4, 5]))
