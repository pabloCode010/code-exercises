// REMOVE DUPLICATES FROM SORTED ARRAY
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

// Dada una matriz de enteros numsordenada en orden no decreciente , elimine los duplicados en el lugar de modo que cada elemento único aparezca solo una vez . El orden relativo de los elementos debe mantenerse igual . Luego devuelve el número de elementos únicos ennums .

// Considere la cantidad de elementos únicos de numsto be k. Para ser aceptado, debe hacer lo siguiente:

// Cambie la matriz numsde modo que los primeros kelementos numscontengan los elementos únicos en el orden en que estaban presentes numsinicialmente. Los elementos restantes de numsno son importantes al igual que el tamaño de nums.
// Devolver k.

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const n = nums.length;
    let prevIdx = null;
    
    for (var i = 0; i < nums.length - 1; i++) {
        if (nums[i] === nums[i + 1]) {
            prevIdx = prevIdx || i + 1;
            while (i < nums.length - 1 && nums[i] === nums[i + 1]) {
                i++;
            }

            if (i == n-1) {
                return prevIdx
            }

            nums[prevIdx] = nums[i + 1];
            prevIdx++;
        } else if (prevIdx !== null) {
            nums[prevIdx] = nums[i + 1];
            prevIdx++;
        }
    }
    return prevIdx ? prevIdx : nums.length

};

const nums = [1,1,2];
const diff = removeDuplicates(nums);
console.log(nums.slice(0, diff));