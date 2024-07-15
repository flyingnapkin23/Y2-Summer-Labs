import random
tempatures = random.sample(range(26, 40), 7)
days_of_week = ["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
good_days_count = 0
max = 26 
min = 40
max_day = "Saturday"
min_day = "Saturday"
all_temp = 0
for i in range (len(tempatures)):

	if tempatures[i] > max:
		max = tempatures[i]
		max_day = days_of_week[i]

	if tempatures[i] < min:
		min = tempatures[i]
		min_day = days_of_week[i]

	if tempatures[i] % 2 == 0:
		good_days_count += 1
		print (days_of_week[i]," is a good day!")

	all_temp += tempatures[i]

average = all_temp / 7

average_list = []
average_list_day = []

for i in range (len(tempatures)):
	if tempatures[i]> average:
		average_list.append(tempatures[i])
		average_list_day.append(days_of_week[i])


for i in range (len(tempatures)):
	print("On ", days_of_week[i], " the tempaerature is ", tempatures[i])

	if tempatures[i] % 2 == 0:
		good_days_count += 1
		print (days_of_week[i]," is a good day!")
print (max_day, " is the day with the highest temperature of ", max)
print (min_day, " is the day with the lowest temperature of ", min)
print (average, " is the average temperature for this week!")

for i in range (len(average_list)):
	print (average_list_day[i], " is a day with and above average temperature with the temperature of ", average_list[i])

def min_find_remove (temps):
	min = 40
	for i in range (len(temps)):
		if temps[i] < min:
			min = temps[i]
	temps.remove(min)
	return min


sorted_temp = []

tempatures_copy = tempatures

for i in range (len(tempatures_copy)):
	sorted_temp.append(min_find_remove(tempatures_copy))
for i in range (len(sorted_temp)):
	print(sorted_temp[i], ", ")