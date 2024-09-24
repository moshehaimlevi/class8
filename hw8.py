# start

numbers: list[int] = [1,100]

for i in range(1,100):
    numbers.append(i)
print(numbers[0])
print(numbers[-1])

print("the length is ", len(numbers))
print('the numbers are', numbers[5:15])
print('the numbers are', numbers[80 + 2:])
print('the numbers are', numbers[2:19])
print('the numbers are', numbers[::-1])
print('the numbers are', numbers[0:100:2])
print('the numbers are', numbers[1:101:10])
print('the numbers are', numbers[99+1:66-1:-3])

numbers.insert(52, 999)
print(numbers)

numbers.pop(100)
print(numbers)


numbers = [i for i in range(100) if i % 3 == 0]
print(numbers)
numbers = [i for i in range(100) if i % 7 == 0]
print(numbers)



