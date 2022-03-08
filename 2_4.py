# # num1 = 1
# # num2 = 10
# # num3 = 1000
# # sum_of_all_numbers = num1 + num2 + num3

# # print("Sum is {0:n}".format(sum_of_all_numbers))

# list_of_numbers = [1, 10, 1000]
# # print(sum(list_of_numbers))
# print(list_of_numbers) # [1, 10, 1000]
# list_of_numbers.clear()
# print(list_of_numbers) # []
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers2 = [3, 100, 5]

# #Adding/concatenating arrays .extend 
# list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers) # 

# # Adding/concatenating arrays using +
# l1 = [1, 32, 4]
# l2 = [100, 200, 300]
# l3 = l1 + l2
# print(l3)

# words = ["Spam", "Wink", "Hi", "My", "In"]
# words.insert(len(words), "Hello")

# print("Words=====>", words)


grades = []

num = float(input("Enter the first grade: "))
grades.append(num)

num = float(input("Enter the second grade: "))
grades.append(num)

num = float(input("Enter the third grade: "))
grades.append(num)

num = float(input("Enter the forth grade: "))
grades.append(num)

num = float(input("Enter the fifth grade: "))
grades.append(num)

min_grade = min(grades)
grades.remove(min_grade)

min_grade = min(grades)
grades.remove(min_grade)

average = sum(grades) / len(grades)

print("Average Grade: {0:.2f}".format(average))