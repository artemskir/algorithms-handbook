//go:build exercise_4_6

package main

/*

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

https://leetcode.com/problems/plus-one/description/

*/

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("usage: %s <n> <n> ...", os.Args[0])
	}
	var digits []int
	for i := 1; i < len(os.Args); i++ {
		digit, err := strconv.Atoi(os.Args[i])
		if err != nil {
			log.Fatalf("usage: %s <n> <n> ...", os.Args[0])
		}
		digits = append(digits, digit)
	}
	fmt.Println(plusOne(digits))
}

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}
