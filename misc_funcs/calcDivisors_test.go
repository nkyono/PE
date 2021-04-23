package test

import (
	"fmt"
	"math"
	"testing"
)

func calcDivs(n int) []int {
	divs := []int{}
	if n < 2 {
		return divs
	}
	for i := 1; i < int(math.Sqrt(float64(n)))+1; i++ {
		if i*i == n {
			divs = append(divs, i)
		} else if n%i == 0 {
			divs = append(divs, i)
			divs = append(divs, n/i)
		}
	}
	return divs
}

/*
func compSliceInt(a, b []int) bool {
	if (a == nil) != (b == nil) {
		return false
	}
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
*/
func TestCalcDivs(t *testing.T) {
	var test = []struct {
		in   int
		want []int
	}{
		{1, []int{}},
		{23, []int{1, 23}},
		{8, []int{1, 8, 2, 4}},
		{10, []int{1, 10, 2, 5}},
		{9, []int{1, 9, 3}},
	}

	for _, tt := range test {
		testname := fmt.Sprintf("%d", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := calcDivs(tt.in)
			if !compSliceInt(tt.want, ans) {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}
