package main

import (
	"fmt"
	"math"
	"time"
)

// (x^2 - 1)/D = y^2 , find MIN x
// root(x^2 - 1/D) = y, so if we find y, where y is an int, we have found min x
/*
 x^2 - D * y^2 == 1
 x^2 - 1 = D * y^2
 (x + 1)(x - 1) = D * y^2

*/

// brute force does work, but it will take forever
// better way, google pell equation
func bruteForce() {
	maxX := -1
	maxD := -1
	maxY := -1
	for d := float64(2); d <= 1000; d++ {
		root := math.Sqrt(d)
		if float64(int(root)) != root {
			x := float64(2)
			for {
				check := math.Sqrt((math.Pow(x, 2) - 1) / d)
				if float64(int(check)) == check {
					if int(x) > maxX {
						maxX = int(x)
						maxY = int(check)
						maxD = int(d)
					}
					fmt.Printf("x: %d, y: %d, d: %d\n", int(x), int(check), int(d))
					break
				}
				x++
			}
		}
	}
	fmt.Printf("maxes x: %d, y: %d, d: %d\n", maxX, maxY, maxD)
}

func driver() {
	bruteForce()
}

func main() {
	start := time.Now()
	driver()
	fmt.Println("time:", time.Since(start))
}
