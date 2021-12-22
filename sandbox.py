numbers = []
sum_of_square = 0

for i in range(1, 101):
    numbers.append(i)
    sum_of_square += i ** 2    

square_of_sum = sum(numbers) ** 2
answer = square_of_sum - sum_of_square

print(numbers)
print(sum_of_square)
print(square_of_sum)
print(answer)