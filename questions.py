# Question 1
def hello_name(user_name):
	print(f"hello_{user_name}")

# Question 2
def first_odds():
	for i in range(100):
		if i % 2 != 0:
			print(i)

# Question 3
def max_num_in_list(a_list: list[int]):
	max = a_list[0]
	if not isinstance(max, int): 
		print("!!-- List must be <list[int]>")
		return
	for i in a_list[1:]:
		if not isinstance(i, int): 
			print("!!-- List must be <list[int]>")
			return
		if i > max:
			max = i
	return max

# Question 4
def is_leap_year(year: int):
	if not isinstance(year, int): 
		print("!!-- Year must be <int>")
		return
	return not(year % 100 == 0 and year % 400 != 0) and (year % 4 == 0)

# Question 5
def is_consecutive(a_list: list[int]):
	last = a_list[0]
	if not isinstance(last, int): 
		print("!!-- List must be <list[int]>")
		return
	for i in a_list[1:]:
		if not isinstance(i, int): 
			print("!!-- List must be <list[int]>")
			return
		if last+1 != i:
			return False
		last = i
	return True
