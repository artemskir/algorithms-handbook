//go:build exercise_6_5

package main

import "fmt"

/*

Input: s = "anagram", t = "nagaram"

Output: true

https://leetcode.com/problems/valid-anagram/description/

*/

func main() {
	fmt.Println(isAnagram("atc", "cat"))
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	cnt := make(map[rune]int)
	for _, c := range s {
		cnt[c]++
	}
	for _, c := range t {
		cnt[c]--
		if cnt[c] < 0 {
			return false
		}
	}
	return true
}
