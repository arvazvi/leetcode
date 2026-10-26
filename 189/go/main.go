package main

func reverse(nums []int, L, R int) {
    for L < R {
        nums[L], nums[R] = nums[R], nums[L]
        L++
        R--
    }
}

func rotate(nums []int, k int)  {
    l := len(nums)
    k = k % l
    reverse(nums, 0, l-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, l-1)
}