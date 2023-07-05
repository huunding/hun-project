for i in range(1, 6):
    for j in range(1,11):
        print(i * j, end="")
    print()
for i in range(1, 6):
    print(str(i) * i)
def print_numbers1():
    for i in range(1, 6):
        print(str(i) * i)
def count_words(string):
    words = string.split()
    return len(words)
numbers = []
while True:
    num = int(input("Integer? "))
    if num == 0:
        break
    if num % 2 == 0:
        numbers.append(num)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No even numbers were entered.")
max_value = int(input("Max value? "))
count = 0
for num in range(1, max_value + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")

    count += 1
    if count % 20 == 0:
        print()

print()
def digit_sum(number):
    number = abs(number)  # Convert negative numbers to positive
    digit_sum = 0

    while number != 0:
        digit = number % 10  # Extract the last digit
        digit_sum += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit from the number

    return digit_sum
def digit_sum(number):
    number = abs(number)  # Convert negative numbers to positive
    digit_sum = 0

    while number != 0:
        digit = number % 10  # Extract the last digit
        digit_sum += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit from the number

    return digit_sum
def is_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lowercase_string = string.lower()  # Convert string to lowercase for case-insensitive comparisondef average_of_2(num1, num2):
    return (num1 + num2) / 2

    if lowercase_string in vowels:
        return True
    else:
        return False
