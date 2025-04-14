from typing import List
from functools import reduce
from collections import defaultdict
#lambda arguments: expression
# O(n²)
class Solution:
    def array_except_self(self, number: List[int]) -> List[int]:
        outStore: List[int] = []

        for i in range(len(number)):
            tempStore = number.copy()
            del tempStore[i]
            product =  reduce(lambda x, y: x * y, tempStore)
            outStore.append(product)
        return outStore

sol = Solution()

print("OutStore: ",sol.array_except_self([-1,1,0,-3,3]))