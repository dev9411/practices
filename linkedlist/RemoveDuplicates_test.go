package removeduplicates

import (
	"reflect"
	"testing"
)

func TestCountLinkedList(test *testing.T) {
	// Table-driven test cases
	testCases := []struct {
		name     string
		input    []int
		expected int
	}{
		{"Empty List", []int{}, 0},
		{"Single Element", []int{1}, 1},
		{"Unique Elements", []int{1, 2, 3, 4, 5}, 5},
		{"Duplicates Present", []int{1, 2, 3, 3, 4, 5, 5}, 7},
		{"All Duplicates", []int{1, 1, 1, 1}, 4},
	}

	for _, tc := range testCases {
		test.Run(tc.name, func(test *testing.T) {
			head := createLinkedList(tc.input)
			result := countLinkedList(head)

			if result != tc.expected {
				test.Errorf("Failed %s: expected %d, got %d", tc.name, tc.expected, result)
			}
		})
	}
}

func TestRemoveDuplicates(test *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		expected []int
	}{
		{"Empty List", []int{}, []int{}},
		{"Single Element", []int{1}, []int{1}},
		{"No Duplicates", []int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{"Duplicates Present", []int{1, 2, 2, 3, 4, 4, 5}, []int{1, 2, 3, 4, 5}},
		{"All Duplicates", []int{7, 7, 7, 7}, []int{7}},
		{"Negative Numbers", []int{-1, -2, -2, -3}, []int{-1, -2, -3}},
		{"Mixed Positive and Negative Numbers", []int{-1, 2, 2, -3, 4, -3, 5}, []int{-1, 2, -3, 4, 5}},
		{"Large Numbers", []int{1000000, 1000000, 2000000}, []int{1000000, 2000000}},
		{"Unsorted List with Duplicates", []int{3, 1, 2, 3, 4, 2, 5}, []int{3, 1, 2, 4, 5}},
		{"Single Duplicate at the End", []int{1, 2, 3, 3}, []int{1, 2, 3}},
		{"Single Duplicate at the Beginning", []int{1, 1, 2, 3}, []int{1, 2, 3}},
		{"Alternating Duplicates", []int{1, 2, 1, 2, 3, 3, 4}, []int{1, 2, 3, 4}},
	}

	for _, tc := range testCases {
		test.Run(tc.name, func(t *testing.T) {
			head := createLinkedList(tc.input)
			head = RemoveDuplicates(head)
			result := linkedListToSlice(head)

			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("Test %s failed: expected %v, got %v", tc.name, tc.expected, result)
			}
		})
	}
}

func linkedListToSlice(head *Node) []int {
	if head == nil {
		return []int{}
	}
	return append([]int{head.data}, linkedListToSlice(head.next)...)
}
