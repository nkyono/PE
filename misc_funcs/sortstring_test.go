package test

import (
	"fmt"
	"sort"
	"testing"
)

type characters []rune

func (s characters) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s characters) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s characters) Len() int {
	return len(s)
}

func SortString(s string) string {
	chars := []rune(s)
	sort.Sort(characters(chars))
	return string(chars)
}

func TestSortString(t *testing.T) {
	var test = []struct {
		in   string
		want string
	}{
		{"cba", "abc"},
		{"fwinwi", "fiinww"},
		{"oqbnruw", "bnoqruw"},
		{"ab", "ab"},
		{"bbaa", "aabb"},
	}
	for _, tt := range test {
		testname := fmt.Sprint(tt.in)
		t.Run(testname, func(t *testing.T) {
			ans := SortString(tt.in)
			if ans != tt.want {
				t.Errorf("got '%s', want '%s'", ans, tt.want)
			}
		})
	}
}
