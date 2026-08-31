package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

/*

Do not use recursion. https://leetcode.com/problems/fibonacci-number/description/

*/

func fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	a, b := 0, 1 // F(0), F(1)
	for i := 2; i <= n; i++ {
		b, a = a+b, b
	}
	return b
}

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("usage: %s <n>", os.Args[0])
	}
	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(fib(n))
}
