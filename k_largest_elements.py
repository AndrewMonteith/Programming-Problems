'''
    Problem: Given an array of integers A, find the largest k elements in the array.
'''

def largest(A, k):
    if k < 0:
        raise ValueError('k cannot be negative')

    if len(A) < k:
        return A

    largest_numbers = []
    
    def add_to_list(x):
        for i, n in enumerate(largest_numbers):
            if n < x:
                largest_numbers[i] = x
                return

    for number in A:
        if len(largest_numbers) < k:
            largest_numbers.append(number)
        else:    
            add_to_list(number)    
    
    return largest_numbers


print(largest([1,2,3,4,5], 3))
print(largest([], 3))
print(largest([-3,-2,-1,0,1,2,3], 1))