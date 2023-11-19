#! /usr/bin/env python3

def rows_blocked(dropping_position, figure_row, field_row):
	for field_index, figure_index in zip(range(dropping_position, dropping_position + 3), range(3)):
		field_occuped = field_row[field_index] == 1
		figure_occuped = figure_row[figure_index] == 1
		if field_occuped and figure_occuped:
			return True

	return False

def row_filled(dropping_position, figure_row, field_row):
	width = len(field_row)
	for field_index in range(width):
		in_figure = field_index >= dropping_position and field_index < dropping_position + 3
		figure_index = field_index - dropping_position

		occupied = field_row[field_index] == 1 or (in_figure and figure_row[figure_index] == 1)

		if not occupied:
			return False

	return True

def any_rows_filled(dropping_position, from_top, field, figure):
	for figure_row_index in range(3):
		field_row_index = figure_row_index + from_top
		figure_row = figure[figure_row_index]
		field_row = field[field_row_index]
		if row_filled(dropping_position, figure_row, field_row):
			return True

	return False

def level_blocked(dropping_position, from_top, field, figure):
	height = len(field)
	width = len(field[0])

	at_bottom = from_top + 3 >= height
	if at_bottom:
		return True

	for figure_row_index in range(2, -1, -1):
		field_row_index = figure_row_index + from_top + 1
		if rows_blocked(dropping_position, figure[figure_row_index], field[field_row_index]):
			return True

	return False

def find_rows(field, figure):
	height = len(field)
	width = len(field[0])

	for dropping_position in range(width - 2):
		for from_top in range(height - 2):
			if level_blocked(dropping_position, from_top, field, figure):
				if any_rows_filled(dropping_position, from_top, field, figure):
					return dropping_position
				break

	return -1

field =  [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
]
figure = [
	[1, 1, 1],
	[1, 0, 1],
	[1, 0, 1],
]
print(find_rows(field, figure))

# print(any_rows_filled(0, 0, field, figure))

# print(rows_blocked(0, [1, 0, 1], [1, 1, 0, 1, 0]))


# # print(any_rows_filled(0, 2, field, figure))

# # print(row_filled(0, [0, 1, 1], [1, 0, 0]))
# # print(row_filled(0, [0, 0, 1], [1, 0, 0]))
# # print(row_filled(1, [1, 0, 1, 0, 1], [1, 0, 1]))
# # print(row_filled(1, [1, 0, 0, 0, 1], [1, 0, 1]))

field = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[1, 0, 0],
	[1, 1, 0],
]
figure = [
	[0, 0, 1],
	[0, 1, 1],
	[0, 0, 1],
]
print(find_rows(field, figure))
