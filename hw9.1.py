# start
# A + B:

temp_list: list[float] = []
temp: float = None
sentinel = -999
max_temp: float = None
min_temp: float = None
while True:
    temp: float = float(input("enter temp:"))
    if temp == sentinel:
        break
    if -50 > temp < 50:
        continue
    temp_list.append(temp)
print(temp_list)

#  SECTION C:
temp_list: list[float] = []
more_temp: list[float] = [-20.0, 39.1, 18.5]

temp_list.extend(more_temp)
print(temp_list.extend(more_temp))
print('after extend', temp_list)

# SECTION E:

max_temp = max(temp_list)
print("Maximum value:", max_temp)
min_temp = min(temp_list)
print("Minimum value:", min_temp)

# SECTION F

temp_list: list[float] = []
if 18.5 in temp_list:
    print(True)
else:
    print(False)
print()

# SECTION G

temp_list: list[float] = []
temp: float = -20.0
char_counter: int = 0
for temp in temp_list:
    if temp_list == temp:
        char_counter += 1
print(f"in '{temp_list}' the character '{temp}' repeats {char_counter} times.")

# SECTION H

temp_list: list[float] = []
average_temp = sum(temp_list) / len(temp_list)
print("Average temperature:", average_temp)

# SECTION I

temp_list: list[float] = []
for temp in temp_list:
    print(temp)
print()

# SECTION   J

temp_list: list[float] = []
for i in range(len(temp_list)):
    print(f"temp[{i}] = {temp_list[i]}", end=" | ")
print()

# SECTION K

temp_list: list[float] = []

del temp_list[0]

print("after deleting:", temp_list)

# SECTION L

temp_list: list[float] = []

for i in range(0, len(temp_list), 2)[::-1]:
    del temp_list[i]
print("with even index:", temp_list)

# SECTION M

temp_list: list[float] = []

while 18.5 in temp_list:
    temp_list.remove(18.5)

# SECTION N
temp_list: list[float] = []
temp_last = temp_list.pop()
print('pop last', temp_last)
print ()

# SECTION O

temp_list: list[float] = []
sorted_temperatures = temp_list.copy()
sorted_temperatures.sort()
print("Original temperatures:", temp_list)
print("Sorted temperatures:", sorted_temperatures)

# SECTION P
temp_list: list[float] = []
temp_list = temp_list.copy()
temp_list.sort()
print('after sort ', temp_list)
temp_list.sort(reverse=True)
print('after sort reverse ', temp_list)

# END















