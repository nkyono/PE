package test

import (
	"fmt"
	"testing"
)

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

func TestSliceComp(t *testing.T) {
	var test = []struct {
		in   [2][]int
		want bool
	}{
		{[2][]int{[]int{}, []int{}}, true},
		{[2][]int{[]int{1, 2, 3}, []int{1, 2, 3}}, true},
		{[2][]int{[]int{}, []int{1, 2, 3}}, false},
		{[2][]int{[]int{1, 2}, []int{2, 1}}, false},
		{[2][]int{[]int{1, 2}, []int{}}, false},
	}

	for _, tt := range test {
		testname := fmt.Sprintf("%v", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := compSliceInt(tt.in[0], tt.in[1])
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
