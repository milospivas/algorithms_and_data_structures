def find_duplicate_tnh(a):
	""" A solution to a problem of finding a duplicate among
	singly-occurring numbers of an array of length n,
	whose elements are integers in range [1, n],
	using Floyd's "Tortoise and Hare" cycle detection algorithm,
	by treating array elements like pointers.

	General algorithm for cycle detection:
		The Tortoise and the Hare both run from the same starting point S.
		Tortois runs one pointer at the time, while Hare runs 2x faster.
		If there's a cycle, they must meet at some point X, inside the cycle.
		
		If S is the starting point, and C is the start of the cycle, then:
			d(S,X) == d(S,C) + d(C,X), 			where d(A,B) is distance from A to B
		
		The Tortoise ran the distance d(S,X):
			first d(S,C), then d(C,X) inside the cycle.
		The Hare ran twise the distance:
			first d(S,C),
			then d(C,X) inside the cycle,
			than again a distance d(S,C) (inside the cycle) ***,
			and finally d(C,X) again.

		*** That means that the point C is exactly d(S,C) away from the point X!
		If we put one of our runners at the start S, keeping the other at X,
		and let them both run at Tortoise's slower pace,
		they'll meet exactly at the cycle starting point C.

	For the given task, since array elements are in range [1, n] we can treat them like pointers
	where each element x in the array points to array element a[x-1]
	"""

	def move1(i):
		""" Given array element i, treating array elements like pointers, move one step. """
		return a[i-1]

	def move2(i):
		""" Given array element i, treating array elements like pointers, move two steps. """
		return a[a[i-1]-1]

	# finding a valid starting point:
	start = -1
	for i, x in enumerate(a):
		if x > len(a):
			raise ValueError("Error. Array element out of given range.", x)
		if x-1 != i:
			# if a[i]-1 == i, both Tortoise and Hare would go into an infinite loop
			start = x
			break

	if -1 == start:
		raise ValueError("Error. There's no duplicates in the given list.", a)

	t, h = move1(start), move2(start)	# set both to start
	while t != h: 						# and until they bump into each-other at point X
		t, h = move1(t), move2(h) 		# let them run at different speeds
	
	t = start						# set one of them to the start,
	while t != h:					# and until they meet at the start of the cycle
		t, h = move1(t), move1(h)	# let them both run at the slow pace
	
	return t

a = [1, 1]
print(a, find_duplicate_tnh(a))

a = [1, 2, 1]
print(a, find_duplicate_tnh(a))

a = [1, 2, 3, 1, 4]
print(a, find_duplicate_tnh(a))

a = [4, 2, 3, 1, 4]
print(a, find_duplicate_tnh(a))

a = [1, 2, 3]
try:
	print(a, find_duplicate_tnh(a))
except ValueError as e:
	print(e)

a = [42]
try:
	print(a, find_duplicate_tnh(a))
except ValueError as e:
	print(e)
	
