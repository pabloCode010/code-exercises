// REMOVE ELEMENT
// https://leetcode.com/problems/remove-element/description/

// Dada una matriz de números enteros numsy un número entero val, elimine todas las apariciones de valin- nums in-place . El orden de los elementos puede cambiarse. Luego devuelve el número de elementos en numslos que no son igualesval .

// Considere la cantidad de elementos en numslos que no son iguales val, kpara ser aceptado, debe hacer lo siguiente:

// Cambie la matriz numsde manera que los primeros kelementos numscontengan los elementos que no sean iguales a val. Los elementos restantes de numsno son importantes al igual que el tamaño de nums.
// Devolver k.

package main

import "fmt"

func main(){
	nums := []int{}
	fmt.Println(nums)

	k := removeElement(nums, 0)

	fmt.Println(nums)
	fmt.Println(nums[:k])
}

func removeElement(nums []int, val int) int {
    var(
		moves int
		n int = len(nums)
	)

	//reorder
	for i := 0; i < n-moves; {
		if nums[i] == val { 
			nums[i], nums[n-moves-1] = nums[n-moves-1], nums[i]
			moves++
		}else{
			i++
		}
	}

	return n - moves
}