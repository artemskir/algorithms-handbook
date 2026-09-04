//go:build exercise_5_5

package main

import "fmt"

/*

Input: s = "([])"

Output: true

s consists of parentheses only '()[]{}'.

https://leetcode.com/problems/valid-parentheses/description/

*/

func main() {
	fmt.Println(isValid("()[]{}"))
}

// s = "()[]{}"
// s = "([])"
func isValid(s string) bool {
	var stack []rune
	pairs := map[rune]rune{')': '(', ']': '[', '}': '{'}
	for _, v := range s {
		switch v {
		case '(', '[', '{':
			stack = append(stack, v)
		default:
			if len(stack) == 0 || stack[len(stack)-1] != pairs[v] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
