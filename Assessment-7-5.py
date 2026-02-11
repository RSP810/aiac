# Task 1: Fixing Syntax Errors


# ❌ Code With Error
# def add(a, b)
#     return a + b

# ✅ Corrected Code
def add(a, b):
    return a + b

print("Task 1 Output:", add(5, 3))



# Task 2: Debugging Logic Errors in Loops


# ❌ Code With Error (Infinite Loop)
# i = 1
# while i <= 5:
#     print(i)
#     i -= 1

# ✅ Corrected Code
print("\nTask 2 Output:")
i = 1
while i <= 5:
    print(i)
    i += 1



# Task 3: Handling Runtime Errors (Division by Zero)


# ❌ Code With Error
# def divide(a, b):
#     return a / b
# print(divide(10, 0))

# ✅ Corrected Code
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print("\nTask 3 Output:", divide(10, 0))


# Task 4: Debugging Class Definition Errors


# ❌ Code With Error
# class Student:
#     def __init__(name, age):
#         name = name
#         age = age

# ✅ Corrected Code
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ram", 20)
print("\nTask 4 Output:", s1.name)


# Task 5: Resolving Index Errors in Lists


# ❌ Code With Error
# numbers = [10, 20, 30]
# print(numbers[5])

# ✅ Corrected Code
numbers = [10, 20, 30]

print("\nTask 5 Output:")
index = 5
if index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")