#! /usr/bin/env python3

def convolution(arr):
	arr_len = len(arr)
	give = [0] * arr_len
	for i in range(arr_len):
		give[i] = (
			(arr[i - 1] if i > 0 else 0)
			+ arr[i]
			+ (arr[i + 1] if i + 1 < arr_len else 0)
		)

	return give

assert convolution([4, 0, 1, -2, 3]) == [4, 5, -1, 2, 1]
assert convolution([]) == []

