# Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing.

# Examples:

# isSubsequence('hello', 'hello world'); // true
# isSubsequence('sing', 'sting'); // true
# isSubsequence('abc', 'abracadabra'); // true
# isSubsequence('abc', 'acb'); // false (order matters)
# Your solution MUST have AT LEAST the following complexities:

# Time Complexity - O(N + M)

# Space Complexity - O(1)



word1 = "hello"
word2 = "hello world"

# def isSubsequence(word1,word2):
#     l = 0
#     r = 0 
#     while r < len(word2) and l < len(word1):
#         if word1[l] == word2[r]:
#             l += 1
#             r += 1
#         else:
#             r += 1

#     print(l,r)
#     if l == len(word1):
#         return True
#     else:
#         return False


# def isSubsequence(word1,word2):
#     i,j = 0,0
#     if not word1:
#         return True
    
#     while j < len(word2):
#         if word1[i] == word2[j]:
#             i += 1
#         if i == len(word1):
#             return True
#         j += 1
    
#     return False


# a = isSubsequence(word1,word2)
# print(a)


def isSubsequenceRec(word1,word2):
    if not word1:
        return True
    if not word2:
        return False
    if word1[0] == word2[0]:
        return isSubsequenceRec(word1[1:],word2[1:])
    return isSubsequenceRec(word1,word2[1:])


a = isSubsequenceRec(word1,word2)
print(a)