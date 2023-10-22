# TWO SUM
# https://leetcode.com/problems/two-sum/description/

# Dada una matriz de números enteros nums y un número entero target, devuelva índices de los dos números de manera que sumen target .

# Puede suponer que cada entrada tendría exactamente una solución y no puede utilizar el mismo elemento dos veces.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

solution = Solution()

print(
    solution.twoSum([2,7,11,15], 9)
)