/*
 *The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
 * As the sum of these divisors is equal to 28, we call it a perfect number.
 * Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
 * forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
 * Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
 * 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
 * Since this chain returns to its starting point, it is called an amicable chain.
 * Find the smallest member of the longest amicable chain with no element exceeding one million.
 */

/* weird because the chain spans multiple numbers so I thought I was getting different chains but they were all of the same chain
 * pretty sure you could also make a graph and use some graph theory to find a longest path (idk though, was just a passing thought)
 */
package main

import (
	"fmt"
	"math"
	"time"
)

func calcDivs(n int) []int {
	divs := []int{}
	if n < 2 {
		return divs
	}
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if i*i == n {
			divs = append(divs, i)
		} else if n%i == 0 {
			divs = append(divs, i)
			divs = append(divs, n/i)
		}
	}
	divs = append(divs, 1)
	return divs
}

func sumDivs(divs []int) int {
	sum := 0
	for i := 0; i < len(divs); i++ {
		sum += divs[i]
	}
	return sum
}

func makeChain(i int, debug bool) map[int]bool {
	divs := calcDivs(i)
	sum := sumDivs(divs)
	chain := make(map[int]bool)
	chain[i] = true
	// aliquots[i] = sum
	if sum != i {
		for {
			chain[sum] = true
			divs = calcDivs(sum)
			sum = sumDivs(divs)
			if debug {
				fmt.Printf("%d, %v\n", sum, divs)
			}
			if _, prs := chain[sum]; (prs || sum > 1000000 || len(divs) == 0) && sum != i {
				chain = make(map[int]bool)
				chain[-1] = true
				return chain
			} else if sum == i {
				return chain
			}
		}
	}
	return chain
}

func driver() {
	// aliquots := make(map[int]int)
	chains := make(map[int]map[int]bool)
	for i := 1; i < 1000000; i++ {
		chains[i] = makeChain(i, false)
	}

	longest := -1
	longestKey := -1
	for k, v := range chains {
		if len(v) > longest {
			longest = len(v)
			longestKey = k
		}
	}
	fmt.Printf("%d, length: %d\n%v\n", longestKey, longest, chains[longestKey])
}

func main() {
	start := time.Now()
	driver()
	fmt.Println("time:", time.Since(start))
}
