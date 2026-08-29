rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    matrix.append(row)

largest = matrix[0][0]
smallest = matrix[0][0]
total_sum = 0
even_count = 0
odd_count = 0

for i in range(rows):
    for j in range(cols):
        num = matrix[i][j]
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total_sum += num
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

reversed_matrix = []
for i in range(rows - 1, -1, -1):
    reversed_matrix.append(matrix[i])

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
for row in reversed_matrix:
    print(*row)
