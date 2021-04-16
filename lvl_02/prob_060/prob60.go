package main

/* The primes 3, 7, 109, and 673, are quite remarkable.
 * By taking any two primes and concatenating them in any order the result will always be prime.
 * For example, taking 7 and 109, both 7109 and 1097 are prime.
 * The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
 * Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
 */

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
	for i := 2; i < int(math.Sqrt(float64(target)))+1; i++ {
		if target%i == 0 {
			return false
		}
	}
	return true
}

// testPrime checks whether a number can be split into two primes and returns the ways it can be
// returns an array of tuples, each tuple is the primes it can be split into
func testPrime(prime int, primes map[int][][]int) [][]int {
	primeString := strconv.Itoa(prime)
	var res [][]int
	if len(primeString) < 2 {
		return res
	}
	for i := 1; i < len(primeString); i++ {
		a, e1 := strconv.Atoi(primeString[:i])
		b, e2 := strconv.Atoi(primeString[i:])
		if e1 != nil || e2 != nil {
			fmt.Println("conversion of int to string failed")
			fmt.Printf("%v\n%v\n", e1, e2)
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
	for i, v := range list {
		if v == e {
			list[len(list)-1], list[i] = list[i], list[len(list)-1]
			return list[:len(list)-1]
		}
	}
	return list
}

/* checkRelations is a function that returns an array of primes that form a complete graph of size n
 * curr represents the current key/prime that we are checking
 * arr a pointer to a list of primes that are all connected to each other via other primes (ie. 7109 connects 7 & 109)
 * primes is a map that reprents a graph like structure. Shows which primes are connected
 */
func checkRelations(curr int, arr *[]int, primes map[int]map[int]bool) bool {
	// n is the size of graph that we want/number of primes we want that all connect
	n := 5
	if len(*arr) == n {
		return true
	}
	for k := range primes[curr] {
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

func iterPrimes() int {
	primes := make(map[int][][]int)
	for i := 2; i < 50000000; i++ {
		if _, checkOne := primes[i]; calcDivsBool(i) && !checkOne {
			res := testPrime(i, primes)
			if len(res) != 0 {
				for _, v := range res {
					rev, e := strconv.Atoi(strconv.Itoa(v[1]) + strconv.Itoa(v[0]))
					if e != nil {
						fmt.Println("Error converting string to int")
						fmt.Printf("%v\n", e)
					}
					if calcDivsBool(rev) {
						p := []int{v[0], v[1]}
						primes[i] = append(primes[i], p)
						primes[rev] = append(primes[rev], p)
					}
				}
			} else {
				primes[i] = [][]int{}
			}
		}
	}
	// fmt.Printf("%v\n", primes)
	primeCounts := make(map[int]map[int]bool)
	for _, v := range primes {
		for _, val := range v {
			if _, check := primeCounts[val[0]]; !check {
				primeCounts[val[0]] = make(map[int]bool)
			}
			primeCounts[val[0]][val[1]] = true
			if _, check := primeCounts[val[1]]; !check {
				primeCounts[val[1]] = make(map[int]bool)
			}
			primeCounts[val[1]][val[0]] = true
		}
	}
	/*
		for k, v := range primeCounts {
			fmt.Printf("%d, %v\n", k, v)
		}
	*/
	minSum := -1
	var minArr []int
	for k, v := range primeCounts {
		if len(v) >= 4 {
			arr := []int{k}
			if checkRelations(k, &arr, primeCounts) {
				sum := 0
				for _, v := range arr {
					sum = sum + v
				}
				fmt.Printf("%d %v\n", sum, arr)
				if minSum > sum || minSum == -1 {
					minSum = sum
					minArr = make([]int, len(arr))
					copy(minArr, arr)
				}
			}
		}
	}

	fmt.Printf("%v\n", minArr)
	return minSum
}

func main() {
	p := fmt.Println
	start := time.Now()
	fmt.Println(iterPrimes())
	p("time:", time.Since(start))
}
