#! /usr/bin/env python3

def pattern_matches(pattern, source):
	found_matches = 0
	pattern_len = len(pattern)
	source_len = len(source)

	for index in range(source_len):
		if index + pattern_len > source_len:
			break

		found_matches += current_matches(pattern, source, index)

	return found_matches

def current_matches(pattern, source, index):
	for increment, requires_vowel_char in enumerate(pattern):
		requires_vowl = True if requires_vowel_char == '0' else False
		is_vowel = source[index + increment] in ('a', 'e', 'i', 'o', 'u', 'y')
		if requires_vowl != is_vowel:
			return 0

	return 1

print(pattern_matches('010', 'amazing'))
