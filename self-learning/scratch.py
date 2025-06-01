# number = int(input("input your number: "))
# i = 1
# j = 1

# for i in range(number+1):
#     print("*"*(number-i))


# for i in range(number+1):
#     for j in range(i):
#         print("*"*j)

# n = int(input("Enter a number: "))

# for i in range(n):
#     spaces = abs(i - n // 2)
#     stars = n - 2 * spaces
#     print('_' * spaces + '*' * stars)

# n = int(input("Enter a number: "))
# if n <= 0:
#     print("Please enter a positive number.")
# else:
#     half = n // 2

#     # Top half (including middle line if odd)
#     for i in range(half + 1):
#         spaces = ' ' * i
#         stars = '*' * (n - 2 * i)
#         print(spaces + stars)

#     # Bottom half (mirror of top)
#     for i in range(half - 1, -1, -1):
#         spaces = ' ' * i
#         stars = '*' * (n - 2 * i)
#         print(spaces + stars)

'''
n=5
i=0
    spaces = 0 => abs(n - (n-i) //2)
    stars = 5 ==>

i=1
    spaces = 1 =>
    stars = 3 ==>


n=5
i=0
    spaces = abs(0-5//2) => 2
    stars = 5-2 * 2 = 1
    print('_' * 2 + '*' * 1) =>__*  
i=1
    spaces = abs(1-5//2) => 1
    stars = 5-2 * 1 = 3
    print('_' * 2 + '*' * 1) =>_***  

i=2
    spaces = abs(2-5//2) => 0
    stars = 5-2 * 1 = 3
    print('_' * 1 + '*' * 3) =>*****

i=3
    spaces = abs(3-5//2) => 1
    stars = 5-2 * 1 = 3
    print('_' * 1 + '*' * 3) =>_***

i=4
    spaces = abs(4-5//2) => 2
    stars = 5-2 * 2 = 1
    print('_' * 2 + '*' * 1) =>__*

what we want is
*****
_***
__*
_***
*****    
    
'''


# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# def average(nums):
#     return sum(nums) / len(nums)

# print(f"You entered: {numbers}")
# print("Sum: ",sum(numbers))
# print("Average: ", average(numbers))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] < arr[j + 1]:
#                 # Swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# numbers = [5, 3, 8, 2, 1]
# bubble_sort(numbers)
# print(numbers)  # [1, 2, 3, 5, 8]

# etl_class = {
#     "Doni": 28,
#     "Ihsan": 25,
#     "Ayi": 32
# }


# member_name = input("Enter a name: ")

# if member_name in etl_class:
#     print(f"{member_name} is {etl_class[member_name]} years old")
# else:
#     print(f"{member_name} not found.")
#     consent = input(f"Want to add {member_name}? (y/n): ")
#     if consent == "y":
#         member_age = int(input(f"Enter {member_name} age: "))
#         etl_class[member_name] = member_age
#         print(f"{member_name} added.")
#         print()
#         print("Updating member, current member is:")
#         for name, age in etl_class.items():
#             print(f"{name}: {age} yo")
#     else:
#         print("Got it. See you again!")

# another simplified code from gpt
# etl_class = {"Sarah": 24}

# name = input("Enter a name: ")

# age = etl_class.get(name)

# if age:
#     print(f"{name} is {age} years old.")
# else:
#     print(f"{name} not found.")
#     if input(f"Want to add {name}? (y/n): ").lower() == "y":
#         try:
#             etl_class[name] = int(input(f"Enter {name}'s age: "))
#             print(f"{name} added.")
#         except ValueError:
#             print("Invalid age entered.")


