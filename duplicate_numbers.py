'''
    Given a list of integers A, remove duplicates from the list
    Obviously there are many ways of doing it with various space and time complexities
'''


# O(n) Time Complexity, O(n) Space Complexity
def remove_duplicates(A):
    already_found, numbers = set(), []

    for n in A:
        if n not in already_found:
            already_found.add(n)
            numbers.append(n)

    return numbers

print(remove_duplicates([1,2,2,3,4,4,4,5]))

# O(1) memory, O(n^2) time complexity
def remove_duplicates(A):
    duplicate_index = len(A) # all elements after duplicate_index are deemed as duplicates

    def swap(i, j):
        A[i], A[j] = A[j], A[i]
    
    i = 0
    while i < duplicate_index:
        n = A[i]

        j = i + 1
        while j < duplicate_index:
            n2 = A[j]

            if n == n2:
                duplicate_index -= 1
                swap(j, duplicate_index)
                continue
            
            j += 1

        i += 1
    
    return A[:duplicate_index]

print(remove_duplicates([1,2,2,3,4,4,4,5]))