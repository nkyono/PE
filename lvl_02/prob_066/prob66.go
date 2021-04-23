package main

import (
	"fmt"
	"math"
	"time"
)

// brute force does work, but it will take forever
// better way, google pell equation
func bruteForce(lim int) {
	maxX := -1
	maxD := -1
	maxY := -1
	for d := float64(2); d <= float64(lim); d++ {
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

/* p_n^2 - D * q_n^2 = (-1)^(n+1)
 * a_0 = floor(sqrt(D))
 * p_0 = a_0
 * p_1 = a_0 * a_1 + 1
 * p_n = a_n * p_(n-1) + p_(n-2)
 * q_0 = 1
 * q_1 = a_1
 * q_n = a_n * q_(n-1) + q_(n-2)
 */

/* p_n^2 - D * q_n^2 = (-1)^(n+1) * Q_(n+1)
 * P_0 = 0
 * P_1 = a_0
 * P_n = a_(n-1) * Q_(n-1) - p_(n-2)
 * Q_0 = 1
 * Q_1 = D - a_0^2
 * Q_n = (D - P_n^2) / Q_(n-1)
 * a_n = floor((a_0 + P_n)/Q_n)
 */

func contFracIrrArith(x float64) []int {
	arr := []int{}
	rem := math.Floor(math.Sqrt(x))
	arr = append(arr, int(rem))
	if math.Pow(rem, 2) == x {
		// x is square
		return arr
	}
	q := float64(1)
	p := float64(0)
	a := rem
	for {
		p = a*q - p
		q = math.Floor((x - math.Pow(float64(p), 2)) / float64(q))
		a = math.Floor((rem + p) / q)
		arr = append(arr, int(a))
		if q == 1 {
			break
		}
	}
	return arr
}

type pair struct {
	p int
	q int
}

func pellRecurrence(d int) pair {
	ansPair := pair{}
	arr := contFracIrrArith(float64(d))
	parr1 := make([]int, len(arr))
	qarr1 := make([]int, len(arr))
	parr2 := make([]int, len(arr))
	qarr2 := make([]int, len(arr))
	// fmt.Printf("%d, %v\n", d, arr)
	parr1[0] = arr[0]
	qarr1[0] = 1
	parr2[0] = 0
	qarr2[0] = 1
	parr2[1] = arr[0]
	qarr2[1] = d - int(math.Pow(float64(arr[0]), 2))
	for i := 2; i < len(arr); i++ {
		parr2[i] = arr[i-1]*qarr2[i-1] - parr2[i-1]
		qarr2[i] = int((float64(d) - math.Pow(float64(parr2[i]), 2)) / float64(qarr2[i-1]))
	}
	/*
		if math.Pow(float64(parr1[0]), 2)-float64(d)*math.Pow(float64(qarr1[0]), 2) == -1*float64(qarr2[1]) {
			ansPair.p = parr1[0]
			ansPair.q = qarr1[0]
			return ansPair
		}
	*/
	parr1[1] = arr[0]*arr[1] + 1
	qarr1[1] = arr[1]
	if math.Pow(float64(parr1[1]), 2)-float64(d)*math.Pow(float64(qarr1[1]), 2) == 1 {
		ansPair.p = parr1[1]
		ansPair.q = qarr1[1]
		return ansPair
	}
	// fmt.Println("---------------")
	i := 2
	for math.Pow(float64(parr1[i-1]), 2)-float64(d)*math.Pow(float64(qarr1[i-1]), 2) != 1 {
		// fmt.Printf("i: %d, ineq: %f\n", i, math.Pow(float64(parr1[i-1]), 2)-float64(d)*math.Pow(float64(qarr1[i-1]), 2))
		parr1 = append(parr1, arr[i]*parr1[i-1]+parr1[i-2])
		qarr1 = append(qarr1, arr[i]*qarr1[i-1]+qarr1[i-2])
		// old: math.Pow(float64(parr1[i]), 2)-float64(d)*math.Pow(float64(qarr1[i]), 2) == math.Pow(-1, float64(i)+1)
		// && math.Pow(float64(parr1[i]), 2)-float64(d)*math.Pow(float64(qarr1[i]), 2) == math.Pow(-1, float64(i+1))*float64(qarr2[i+1])
		/*if parr1[i]*qarr1[i-1]-parr1[i-1]*qarr1[i] == int(math.Pow(-1, float64(i+1))) {
			ansPair.p = parr1[i]
			ansPair.q = qarr1[i]
			// return ansPair
		}*/
		if i == len(arr)-1 {
			arr = append(arr, arr...)
		}
		i++
	}
	ansPair.p = parr1[i-1]
	ansPair.q = qarr1[i-1]
	/*
		fmt.Printf("arr: %v\n", arr)
		fmt.Printf("p1: %v\nq1: %v\n", parr1, qarr1)
		fmt.Printf("p2: %v\nq2: %v\n", parr2, qarr2)
	*/
	/*
		fmt.Printf("p: %v\nq: %v\n", parr1, qarr1)
		minX := -1
		for i := 1; i < len(parr1); i++ {
			if (minX > parr1[i] || minX == -1) && math.Pow(float64(parr1[i]), 2)-float64(d)*math.Pow(float64(qarr1[i]), 2) == 1 {
				ansPair.p = parr1[i]
				ansPair.q = qarr1[i]
				minX = parr1[i]
			}
		}
	*/
	return ansPair
}

func pellDriver(lim int) {
	for d := 2; d <= lim; d++ {
		check := math.Sqrt(float64(d))
		if float64(int(check)) != check {
			ans := pellRecurrence(d)
			fmt.Printf("%d: %v\n", d, ans)
		}
	}
}

func driver() {
	lim := 15
	// bruteForce(lim)
	pellDriver(lim)
}

func main() {
	start := time.Now()
	driver()
	fmt.Println("time:", time.Since(start))
}
