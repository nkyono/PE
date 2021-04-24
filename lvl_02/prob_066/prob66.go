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

func contFracIrrArith(x float64) []uint64 {
	arr := []uint64{}
	rem := math.Floor(math.Sqrt(x))
	arr = append(arr, uint64(rem))
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
		arr = append(arr, uint64(a))
		if q == 1 {
			break
		}
	}
	return arr
}

type pair struct {
	p uint64
	q uint64
}

/* calc convergents using continued fraction
 * issue with over on odd periods because odd periods turn into 2r
 * could try to swith to bigInt which may solve problem
 * instead I ignored all even periods (because only odd ones overflowed)
 * just used r instead of 2r. due to the way convergents are calculated,
 * if a convergent_i[r] > convergent_j[r] than convergent_i[2r] > convergent_j[2r]
 * I have no written proof for this theory, but it worked ...
 */

func pellRecurrence(d uint64) pair {
	ansPair := pair{}
	a := contFracIrrArith(float64(d))
	converg := []pair{}
	converg = append(converg, pair{a[0], 1}, pair{a[0]*a[1] + 1, a[1]})
	period := len(a)
	// fmt.Println("----------")
	if period%2 == 0 {
		// a = append(a, a[1:]...)
		// period = period * 2
		// fmt.Printf("%d, %v\n", period, a)
		for i := 2; i < period; i++ {
			converg = append(converg, pair{a[i]*converg[i-1].p + converg[i-2].p, a[i]*converg[i-1].q + converg[i-2].q})
		}
		// fmt.Printf("%v\n", converg)
		ansPair.p = converg[len(converg)-1].p
		ansPair.q = converg[len(converg)-1].q
		return ansPair
	} else {
		return ansPair
	}
}

func pellDriver(lim uint64) {
	maxX := uint64(0)
	maxD := uint64(0)
	maxY := uint64(0)
	for d := uint64(2); d <= lim; d++ {
		check := math.Sqrt(float64(d))
		if float64(int(check)) != check {
			ans := pellRecurrence(d)
			fmt.Printf("%d: %v\n", d, ans)
			if ans.p > maxX {
				maxX = ans.p
				maxD = d
				maxY = ans.q
				// fmt.Printf("d: %d, x: %d, y: %d\n", maxD, maxX, maxY)
			}
		}
	}
	fmt.Printf("d: %d, x: %d, y: %d\n", maxD, maxX, maxY)
}

func driver() {
	lim := uint64(1000)
	// bruteForce(lim)
	pellDriver(lim)
}

func main() {
	start := time.Now()
	driver()
	fmt.Println("time:", time.Since(start))
}
