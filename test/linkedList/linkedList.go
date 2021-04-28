package main

import "fmt"

type node struct {
	val  int
	next *node
}

func main() {
	values := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	first := node{-1, nil}
	head := &first
	curr := head
	for _, v := range values {
		newNode := node{v, nil}
		curr.next = &newNode
		curr = curr.next
	}
	head = head.next
	for head.next != nil {
		fmt.Printf("%v\n", head)
		head = head.next
	}
}
