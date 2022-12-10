def sum_with_range(start, end):
    sum = 0
    for x in range(start, end):
        sum += x
    return sum

print(sum_with_range(1, 10))
print(sum_with_range(20, 30))