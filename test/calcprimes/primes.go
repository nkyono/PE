package main

import (
	"fmt"
	"math"
	"time"
)

// compared to python3, which takes ~90 seconds to compute 10000000 primes, Go takes ~5 seconds
func calcDivsBool(target int) bool {
	if target < 2 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(target))); i++ {
		if target%i == 0 {
			return false
		}
	}

	return true
}

func calcPrimes() []int {
	var prime []int
	numPrimes := 0

	for x := 0; x < 10000000; x++ {
		if calcDivsBool(x) {
			prime = append(prime, x)
			numPrimes++
		}
	}
	fmt.Printf("number primes: %d\n", numPrimes)
	return prime
}

func main() {
	p := fmt.Println
	start := time.Now()
	calcPrimes()
	p("time:", time.Since(start))
}
