'''
    Given a list of numbers [1 .. n] where one number is missing. Find that number.
    Provided: List of numbers, what the numbers should go upto
'''

# O(n) Time and O(1) Memory
def missing_numbers_1(A, n):
    return n*(n+1)/2 - sum(A)

print(missing_numbers_1([1,2,4,5], 5))