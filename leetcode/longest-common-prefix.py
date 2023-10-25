# LONGEST COMMON PREFIX
# https://leetcode.com/problems/longest-common-prefix/description/

# Escriba una función para encontrar la cadena de prefijo común más larga entre una matriz de cadenas.

# Si no hay un prefijo común, devuelve una cadena vacía "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""

# Segunda Implementación

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_word = min(strs, key=len)
        prefix = ""

        for i in range(len(min_word)):
            letter = min_word[i]
            for word in strs:
                if letter != word[i]:
                    return prefix
            prefix += letter
        return prefix

solution = Solution()

words = ["flower","flow","flight"]
prefix = solution.longestCommonPrefix(words)

print(prefix)

  ###       ###
  ###       ###
  ###       ###
  ###       ###
#######   #######
 #####     #####
  ###       ###
   #         #


# Primera Implementacion

# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         fisrt_word = strs[0]
#         prefix = ""
#         for i in range(len(fisrt_word)):
#             letter = fisrt_word[i]
#             for j in range(1, len(strs)):
#                 current_word = strs[j]
#                 if i >= len(current_word):
#                     return prefix
#                 elif letter != current_word[i]:
#                     return prefix
#             prefix += letter
#         return prefix

# solution = Solution()

# words = ["flower","flow","flight"]
# prefix = solution.longestCommonPrefix(words)

# print(prefix)


# Tercera Implementación

# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         min_word_length = min(len(word) for word in strs)
#         prefix = ""

#         i = 0
#         j = 0
#         length = len(strs)
#         while j < min_word_length and i < length:
#             letter = strs[i][j]
#             next_letter = strs[(i+1) % length][j]

#             if letter != next_letter:
#                 return prefix
            
#             i += 1

#             if i >= length-1:
#                 prefix += letter
#                 i = 0
#                 j += 1
#         return prefix

# words = ["flower","flow","flight"]
# prefix = solution.longestCommonPrefix(words)

# print(prefix)