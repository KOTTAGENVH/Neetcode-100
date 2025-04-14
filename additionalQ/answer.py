from typing import List
def find_bigrams(sentence):
    words = sentence.lower().split()
    return [(words[i], words[i+1]) for i in range(len(words)-1)]
print(find_bigrams("te ERER erer"))

def sum_to_N(integers: List[int], n: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, path: List[int], total: int):
        if total == n:
            result.append(path[:])
            return
        if total > n:
            return
        
        for i in range(start, len(integers)):
            path.append(integers[i])
            backtrack(i, path, total + integers[i])  # allow reuse
            path.pop()

    backtrack(0, [], 0)
    return result
