//go:build reverseint

package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

https://leetcode.com/problems/reverse-integer/description/

*/

func main() {
	fmt.Println(reverse(1534236469))
}

func reverse(x int) int {
	if x > 2147483647 || x < -2147483647 {
		return 0
	}
	isNegative := false
	if x < 0 {
		isNegative = true
		x *= -1
	}
	lenX := len(strconv.Itoa(x))
	output := 0
	for i := lenX - 1; i >= 0; i-- {
		placeValue := "1" + strings.Repeat("0", i)
		val, err := strconv.Atoi(placeValue)
		if err != nil {
			return 0
		}
		output = output + (x%10)*val
		x /= 10
	}
	if isNegative {
		output *= -1
	}
	if output > 2147483647 || output < -2147483647 {
		return 0
	}
	return output
}
