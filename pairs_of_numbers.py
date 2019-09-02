'''
    Given a list of distinct unsorted integers A and a target t
    find all pairs (x, y) such x + y = t
'''


# Time Complexity O(nlogn) 
# > O(nlogn) for sorting
# > O(n) for finding the pairs
def pairs_of_numbers(A, t):
    nums = sorted(A)
    l, r = 0, len(nums) - 1
    pairs = []

    while l < r:
        a, b = A[l], A[r]

        x = a + b
        
        if x == t:
            pairs.append((a, b))
            l += 1
            r -= 1
        elif x > t:
            r -= 1        
        elif x < t:
            l += 1
    
    return pairs


numbers = list(range(500))
target = 157

print(pairs_of_numbers(numbers, target))