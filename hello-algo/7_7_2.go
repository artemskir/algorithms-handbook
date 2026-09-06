//go:build exercise_7_7_2

package main

import (
	"container/list"
	"fmt"
)

/*

Given the root of a binary tree, return the level order
traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	root := &TreeNode{
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

	fmt.Println("Test 1:", levelOrder(root))
	// expected: [[3] [9 20] [15 7]]

	//  1
	root2 := &TreeNode{Val: 1}

	fmt.Println("Test 2:", levelOrder(root2))
	// expected: [[1]]

	// nil
	var root3 *TreeNode

	fmt.Println("Test 3:", levelOrder(root3))
	// expected: []
}

// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	queue := list.New()
	queue.PushBack(root)
	nums := make([][]int, 0)

	for queue.Len() > 0 {
		levelSize := queue.Len()
		level := make([]int, 0, levelSize)

		for i := 0; i < levelSize; i++ {
			node := queue.Remove(queue.Front()).(*TreeNode)
			level = append(level, node.Val)

			if node.Left != nil {
				queue.PushBack(node.Left)
			}
			if node.Right != nil {
				queue.PushBack(node.Right)
			}
		}
		nums = append(nums, level)
	}
	return nums
}
