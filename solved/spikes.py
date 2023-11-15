#! /usr/bin/env python3
def spikes_safe_at_speed(spikes, speed):
	failed_cases = set()
	return _spikes_safe_at_speed(spikes, failed_cases, -1, speed)

def _spikes_safe_at_speed(spikes, failed_cases, current_index, speed):
	print('recursing:', current_index, speed)
	if (current_index, speed) in failed_cases:
		print('failed from memo:', current_index, speed)
		return False

	if current_index >= len(spikes):
		print('success:', current_index, speed)
		return True

	if speed == 0:
		failed_cases.add((current_index, speed))
		print('stalled:', current_index, speed)
		return False

	current_safe = spikes[current_index]
	if not current_safe:
		failed_cases.add((current_index, speed))
		print('not safe:', current_index, speed)
		return False

	if _spikes_safe_at_speed(spikes, failed_cases, current_index + speed + 1, speed + 1):
		return True
	if _spikes_safe_at_speed(spikes, failed_cases, current_index + speed, speed):
		return True
	if _spikes_safe_at_speed(spikes, failed_cases, current_index + speed - 1, speed - 1):
		return True

	failed_cases.add((current_index, speed))
	return False

my_spikes = [True, False, True, True, True, False, True, True, False, True, True]

print(spikes_safe_at_speed(my_spikes, 4))
