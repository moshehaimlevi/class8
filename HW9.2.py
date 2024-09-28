# start

number_list = []

sentinel = -999

while True:
    number: int = int(input('enter a number'))
    if number == -999:
        break
    if 0 <= number <= 10:
        number_list.append(number)
        statistics = {}
        for i in range(0, 11):
            count = number_list.count(i)
            if count > 0:
                statistics[i] = count
print("Final numbers entered:", number_list)

# end 
