# Question 1
from json.encoder import INFINITY


def hello_name(user_name):
	print(f"hello_{user_name}")

# Question 2
def first_odds():
	for i in range(100):
		if i % 2 != 0:
			print(i)

# Question 3
def max_num_in_list(a_list):
	max = -INFINITY
	for i in a_list:
		if i > max:
			max = i
	return max

# Question 4
def is_leap_year(year):
	return not(year % 100 == 0 and year % 400 != 0) and (year % 4 == 0)

# Question 5
def is_consecutive(list):
	last = list[0]
	for i in list[1:len(list)]:
		if last+1 != i:
			return False
		last = i
	return True

# print(is_consecutive([0,1,2,3,4]))
# print(is_consecutive([-4,-3,-2,-1,0]))
# print(is_consecutive([5,6,7]))
# print("\nTrues ^^ | False vv\n")
# print(is_consecutive([5,6,8]))
# print(is_consecutive([5,6,3]))
# print(is_consecutive([10,20,30]))