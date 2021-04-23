package main

/* Solved by calculating the whole sequence and keeping track of indexes
 * then just found difference between index of 1/2 and 1/3 minus 1
 */

import (
	"fmt"
	"time"
)

// phi and calcFareyLength were made unnecesary for current way of solving
/*
func phi(n int) int {
	res := float64(n)
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			for n%i == 0 {
				n = n / i
			}
			res = res * (1.0 - 1.0/float64(i))
		}
	}
	if n > 1 {
		res = res * (1.0 - 1.0/float64(n))
	}
	return int(res)
}

func calcFareyLength(n int) int {
	numFracs := []int{0, 2}
	for i := 2; i <= n; i++ {
		numFracs = append(numFracs, phi(i)+numFracs[i-1])
	}
	return numFracs[n]
}
*/

type frac struct {
	num int
	dem int
}

func calcIndexes(n int) map[frac]int {
	indexes := make(map[frac]int)
	numA := 0
	demA := 1
	numB := 1
	demB := n // 1/n will always be the '1st' index (0/1 then 1/n)
	indexes[frac{numA, demA}] = 0
	indexes[frac{numB, demB}] = 1
	index := 2

	for numB <= n {
		k := (n + demA) / demB
		temp := numA
		numA = numB
		numB = k*numB - temp
		temp = demA
		demA = demB
		demB = k*demB - temp
		// fmt.Printf("%d/%d\n", numB, demB)
		indexes[frac{numB, demB}] = index
		index++
	}
	return indexes
}

func driver() {
	n := 12000
	// fareyLength := calcFareyLength(n)
	indexes := calcIndexes(n)
	/*
		for k, v := range indexes {
			fmt.Printf("%d/%d : %d\n", k.num, k.dem, v)
		}
	*/
	fmt.Printf("1/3 index: %d\n1/2 index: %d\ndiff: %d\n", indexes[frac{1, 3}], indexes[frac{1, 2}], indexes[frac{1, 2}]-indexes[frac{1, 3}]-1)
}

func main() {
	start := time.Now()
	driver()
	fmt.Println("time:", time.Since(start))
}
