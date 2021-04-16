package test

import (
	"fmt"
	"testing"
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

func TestPhi(t *testing.T) {
	var test = []struct {
		in   int
		want int
	}{
		{1, 1},
		{9, 6},
		{7, 6},
		{23, 22},
		{100, 40},
	}

	for _, tt := range test {
		testname := fmt.Sprintf("%d", tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := phi(tt.in)
			if ans != tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}
