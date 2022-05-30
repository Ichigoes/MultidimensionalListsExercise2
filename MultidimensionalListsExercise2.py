n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for idx in range(n):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][n - 1 - idx])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))
