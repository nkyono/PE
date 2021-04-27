package main

import (
	"fmt"
	"math"
)

func calcRectangles(m, n int) int {
	return m * (m + 1) * n * (n + 1) / 4
}

func main() {
	type ans struct {
		diff int
		m    int
		n    int
	}
	answer := ans{diff: 1000, m: -1, n: -1}
	m := 1
	n := 1
	rects := calcRectangles(m, n)
	for rects < 2001000 {
		for n < m && rects < 2001000 {
			rects := calcRectangles(m, n)
			// fmt.Printf("%dx%d: %d\n", m, n, rects)
			diff := int(math.Abs(float64(2000000 - rects)))
			if diff < answer.diff {
				answer.diff = diff
				answer.m = m
				answer.n = n
				fmt.Printf("%v\n", answer)
			}
			n++
		}
		m++
		n = 1
	}
}
