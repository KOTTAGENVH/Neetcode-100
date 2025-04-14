#YTB: https://youtu.be/YPTqKIgVk-k?si=Qef4JRnn_rzp-hmj
from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
    def topElement(self,numbers: List[int],k: int) ->  List[int]:
        count = Counter(numbers)
        print("Count", count) #Answer: Counter({1: 3, 2: 2, 3: 1})
        
        # Get the k most common elements
        top_k = [num for num, freq in count.most_common(k)]
        
        return top_k
     
sol = Solution()
print("answer:", sol.topElement([1,1,1,2,2,3],k=2)) #Answer: [1, 2]