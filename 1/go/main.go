package main

// twoSum returns the indices of the two numbers that add up to target.
// One pass with a hash map of value -> index: O(n) time, O(n) space.
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))
	for i, n := range nums {
		if j, ok := seen[target-n]; ok {
			return []int{j, i}
		}
		seen[n] = i
	}
	return nil
}
