package main

import "fmt"

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

func main() {
	// NOTE: farey sequence for n=1 is 2 because of 0/1 and 1/1 but we are not including that
	// answer should be numFracs[1000000] - 2
	numFracs := []int{0, 2}
	for i := 2; i <= 1000000; i++ {
		numFracs = append(numFracs, phi(i)+numFracs[i-1])
	}
	fmt.Printf("%d\n", numFracs[1000000]-2)
}
