# ROMAN TO INTEGER
# https://leetcode.com/problems/roman-to-integer/description/

# Dado un número romano, conviértalo a un número entero.
# Los números romanos están representados por siete símbolos diferentes:  I, V, X, L, y .CDM

# Símbolo        Valor 
# I                1 
# V                5 
# X                10 
# L                50 
# C                100 
# D                500 
# M                1000

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        int_roman = 0
        prev_value = values[s[0]]

        for i in range(1, len(s)):
            value = values[s[i]]
            int_roman += prev_value if prev_value >= value else -prev_value
            prev_value = value
        int_roman += prev_value

        return int_roman

solution = Solution()
roman = "XIX"
roman_to_int = solution.romanToInt(roman)
print(f"{roman} = {roman_to_int}")