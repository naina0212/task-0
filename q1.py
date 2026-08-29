N = int(input())
numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]
total_sum = 0
even_count = 0
odd_count = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total_sum += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

reversed_list = []
for i in range(N - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Reversed:", *reversed_list)
