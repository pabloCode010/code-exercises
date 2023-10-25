# VALID PARENTHESES
# https://leetcode.com/problems/valid-parentheses/description/

# Dada una cadena que scontiene solo los caracteres '(', ')', '{', y , determine si la cadena de entrada es válida.'}''['']'

# Una cadena de entrada es válida si:

# Los corchetes abiertos deben cerrarse con el mismo tipo de corchetes.
# Los corchetes abiertos deben cerrarse en el orden correcto.
# Cada corchete cerrado tiene un corchete abierto correspondiente del mismo tipo.

#Primera Implementación

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for i in s:
            if i in "([{":
                parentheses.append(i)
            elif i in ")]}":
                if not parentheses:
                     return False
                last_parentheses = parentheses.pop()
                if last_parentheses == "[" and i != "]": 
                     return False
                elif last_parentheses == "(" and i != ")":
                    return False
                elif last_parentheses == "{" and i != "}":
                     return False
        return not parentheses

solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))

  ###       ###
  ###       ###
  ###       ###
  ###       ###
#######   #######
 #####     #####
  ###       ###
   #         #

# Segunda Implementación

# class Solution:
#     def isValid(self, s: str) -> bool:
#         parentheses = []
#         map_values = {"[": "]", "(": ")", "{": "}"}

#         for i in s:
#             if i in "([{":
#                 parentheses.append(i)
#             elif i in ")]}" and len(parentheses) > 0:
#                 last_parentheses = parentheses[-1]
#                 if map_values[last_parentheses] != i:
#                     return False
#                 del parentheses[-1]
#             else:
#                 return False
        
#         return len(parentheses) == 0

# solution = Solution()

# print(solution.isValid("()"))
# print(solution.isValid("()[]{}"))
# print(solution.isValid("(]"))