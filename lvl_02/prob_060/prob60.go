package main

import (
	"fmt"
	"math"
	"strconv"
	"time"
)

// checks whether a number has divisors other than 1, itself (ie. is it prime)
func calcDivsBool(target int) bool {
	if target < 2 {
		return false
	}
	for i := 2; i < int(math.Sqrt(float64(target))); i++ {
		if target%i == 0 {
			return false
		}
	}
	return true
}

// testPrime checks whether a number can be split into two primes
func testPrime(prime int, primes map[int]bool) [][]int {
	primeString := strconv.Itoa(prime)
	var res [][]int
	if len(primeString) < 2 {
		return res
	}
	for i := 0; i < len(primeString); i++ {
		a, e1 := strconv.Atoi(primeString[:i])
		b, e2 := strconv.Atoi(primeString[i:])
		if e1 != nil || e2 != nil {
			fmt.Println("conversion of int to string failed")
		}
		if primeString[i] != '0' {
			_, checkA := primes[a]
			_, checkB := primes[b]
			if checkA && checkB {
				pair := []int{a, b}
				res = append(res, pair)
			}
		}
	}

	return res
}

// helper function that checks whether element in array
func checkArray(e int, list []int) bool {
	for _, v := range list {
		if v == e {
			return true
		}
	}
	return false
}

// helper function that removes element from array
func removeElem(e int, list []int) []int {
	list[len(list)-1], list[e] = list[e], list[len(list)-1]
	return list[:len(list)-1]
}

/* checkRelations is a function that returns an array of primes that form a complete graph of size n
 * curr represents the current key/prime that we are checking
 * arr a pointer to a list of primes that are all connected to each other via other primes (ie. 7109 connects 7 & 109)
 * primes is a map that reprents a graph like structure. Shows which primes are connected
 */
func checkRelations(curr int, arr *[]int, primes map[int]map[int]bool) bool {
	// n is the size of graph that we want/number of primes we want that all connect
	n := 4
	if len(*arr) == n {
		return true
	}
	for k := range primes {
		if !checkArray(k, *arr) {
			*arr = append(*arr, k)
			for _, y := range *arr {
				_, check := primes[y][k]
				if !check && k != y {
					*arr = removeElem(k, *arr)
					break
				}
			}
			if checkArray(k, *arr) {
				if checkRelations(k, arr, primes) {
					return true
				} else {
					*arr = removeElem(k, *arr)
				}
			}
		}
	}
	return false
}

func iterPrimes() {
	var prime []int
	for i := 0; i < 10000000; i++ {
		if calcDivsBool(i) {
			prime = append(prime, i)
		}
	}
	fmt.Printf("%v\n", prime)
}

func main() {
	p := fmt.Println
	start := time.Now()
	iterPrimes()
	p("time:", time.Since(start))
}
