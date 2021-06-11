import random


def quick_sort(random_list):

	if len(random_list) > 1:
		random_center = random_list[random.randint(0, len(random_list)-1)]
		low = []
		for i in random_list:
			if i < random_center:
				low.append(i)

		eq = []
		for i in random_list:
			if i == random_center:
				eq.append(i)


		hight = []
		for i in random_list:
			if i > random_center:
				hight.append(i)

		random_list = quick_sort(low) + eq + quick_sort(hight)

	return random_list


random_list = [9, 5, -3, 4, 7, 8, -8]
final_list = quick_sort(random_list)
print(random_list)
print(final_list)