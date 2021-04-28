package main

import "fmt"

type nodeDouble struct {
	val  int
	next *nodeDouble
	prev *nodeDouble
}

func doubleLinkedList(values []int) {
	first := nodeDouble{values[0], nil, nil}
	curr := &first
	prev := curr
	for _, v := range values[1:] {
		newNode := nodeDouble{v, nil, curr}
		curr.next = &newNode
		prev = curr
		curr = curr.next
		curr.prev = prev
	}
	curr.next = &first
	prev = curr
	curr = curr.next
	curr.prev = prev
	for i := 0; i < len(values); i++ {
		fmt.Printf("%v\n", curr)
		curr = curr.next
	}

}

type nodeSingle struct {
	val  int
	next *nodeSingle
}

func singleLinkedList(values []int) {
	first := nodeSingle{-1, nil}
	head := &first
	curr := head
	for _, v := range values {
		newNode := nodeSingle{v, nil}
		curr.next = &newNode
		curr = curr.next
	}
	head = head.next
	for head.next != nil {
		fmt.Printf("%v\n", head)
		head = head.next
	}
}

func main() {
	values := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	singleLinkedList(values)
	doubleLinkedList(values)
}
