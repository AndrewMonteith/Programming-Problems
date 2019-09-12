'''
    Problem: Missing Words

    Given 2 sequences s and t, t is a subsequence of s if the words of t
    occur in s not necessarily in a contiguos sequence but in the same order.

    "hi there" is a subsequence of "hi there friend"
    "hi there" is a subsequence of "hi over there friend"
    "hi there" is a subsequence of "hi a hi b there c there"
    "hi there" is not a subsequence of "there mate, i said hi" 


    Write a function remove_subsequence(s, t) that removes the first occurence
    of the subsequence t from s and returns the result as a words vector.

    Examples:
        remove_subsequence("hi there friend", "hi there") == ["friend"]
        remove_subsequence("hi over there friend", "hi there") == ["over friend"]
        remove_subsequence("hi a hi b there c there", "hi there") == ["a", "hi", "b", "c", "there"]

    Assumptions:
        s & t are non empty strings
        1 <= |t| <= |s| <= 10^5

        t is a subsequence of s
'''

def remove_subsequence(s, t):
    words_s, words_t = s.split(" "), t.split(" ")

    t_i = 0 # index of word in words_t we're looking to remove
    to_remove = set([])

    for i in range(0, len(words_s)):
        if words_s[i] == words_t[t_i]:
            to_remove.add(i)
            t_i += 1

            if t_i == len(words_t):
                break 
    
    return [words_s[i] for i in range(0, len(words_s)) if i not in to_remove]

assert(remove_subsequence("hi there friend", "hi there") == ["friend"])
assert(remove_subsequence("hi over there friend", "hi there") == ["over", "friend"])
assert(remove_subsequence("a hi b hi c there d there", "hi there") == ["a", "b", "hi", "c", "d", "there"])

print("Success")