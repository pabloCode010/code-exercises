# PALINDROME NUMBER
# https://leetcode.com/problems/palindrome-number/description/

# Dado un número entero x, devuelve true si x es un palíndromo y false de otra manera.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_number = str(x)
        return str_number == str_number[::-1]

solution = Solution()

print(
    solution.isPalindrome(121)
)