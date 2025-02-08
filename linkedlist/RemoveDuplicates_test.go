package removeduplicates

import "testing"

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
