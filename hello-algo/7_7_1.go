//go:build exercise_7_7_1

package main

import "fmt"

/*

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	// Test 1: Empty tree
	var root1 *TreeNode = nil

	fmt.Println("Test 1:", maxDepth(root1))
	// expected: 0

	// Test 2: One node
	//
	//  1
	//
	root2 := &TreeNode{
		Val: 1,
	}

	fmt.Println("Test 2:", maxDepth(root2))
	// expected: 1

	// Test 3:
	//
	//        3
	//       / \
	//      9   20
	//         /  \
	//        15   7
	//
	root3 := &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val: 9,
		},
		Right: &TreeNode{
			Val: 20,
			Left: &TreeNode{
				Val: 15,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
	}

	fmt.Println("Test 3:", maxDepth(root3))
	// expected: 3

	// Test 4: Left-skewed tree
	//
	//      1
	//     /
	//    2
	//   /
	//  3
	// /
	//4
	//
	root4 := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 4,
				},
			},
		},
	}

	fmt.Println("Test 4:", maxDepth(root4))
	// expected: 4

	// Test 5: Right-skewed tree
	//
	// 1
	//  \
	//   2
	//    \
	//     3
	//
	root5 := &TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
			Right: &TreeNode{
				Val: 3,
			},
		},
	}

	fmt.Println("Test 5:", maxDepth(root5))
	// expected: 3
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)

	return 1 + max(leftDepth, rightDepth)
}
