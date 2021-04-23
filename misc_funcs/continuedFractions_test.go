package test

import (
	"fmt"
	"math"
	"testing"
)

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

func TestContinuedFracs(t *testing.T) {
	var test = []struct {
		in   int
		want []int
	}{
		{4, []int{2}},
		{9, []int{3}},
		{5, []int{2, 4}},
		{46, []int{6, 1, 3, 1, 1, 2, 6, 2, 1, 1, 3, 1, 12}},
		{19, []int{4, 2, 1, 3, 1, 2, 8}},
		{2, []int{1, 2}},
		{3, []int{1, 1, 2}},
		{139, []int{11, 1, 3, 1, 3, 7, 1, 1, 2, 11, 2, 1, 1, 7, 3, 1, 3, 1, 22}},
	}

	for _, tt := range test {
		testname := fmt.Sprintf("%d", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := contFracIrrArith(float64(tt.in))
			if !compSliceInt(ans, tt.want) {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
