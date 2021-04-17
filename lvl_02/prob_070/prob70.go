package main

import (
	"fmt"
	"math"
	"problem70/SortString"
	"strconv"
)

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
	minRatio := 1000.0
	minPhi := -1
	minIndex := -1
	phiMap := make(map[int]int)
	phiMap[1] = 1
	for i := 0; i < int(math.Pow(10, 7)+1); i++ {
		phiRes := phi(i)
		phiMap[i] = phiRes
		phiSorted := SortString.SortString(strconv.Itoa(phiRes))
		iSorted := SortString.SortString(strconv.Itoa(i))
		if phiRes != i && phiSorted == iSorted {
			currRatio := float64(i) / float64(phiRes)
			if minRatio > currRatio {
				minRatio = currRatio
				minPhi = phiRes
				minIndex = i
				fmt.Printf("%d, %d, %f\n", i, phiRes, float64(i)/float64(phiRes))
			}
		}
	}

	fmt.Printf("%d, %d, %f\n", minIndex, minPhi, minRatio)
}
