# start

# SECTION A
list1: list[int] = [i for i in range(95, 105 + 1, 1)]
print(list1)

# SECTION B
list2: list[int] = [i for i in range(10, 20 + 1, 2)]
print(list2)

# SECTION C
import random

list3: list[str] = [random.choice([False, True]) for i in range(5)]
print(list3)

# SECTION D
import random

list4: list[int] = [random.randint(1, 100) for i in range(10)]
print(list4)

# SECTION E
import random

list4: list[int] = [number for _ in range(10) if (number := random.randint(1, 100)) > 50]
print(list4)

# SECTION F
import random

list5: list[int] = [number for _ in range(10) if (number := random.randint(1, 100)) > 50]
print(list5)

# SECTION G
sentence: str = input ('enter your sentence:')
list6: list[str] = [letter for letter in sentence if letter != 't' and letter != ' ']
print(list6)

# SECTION H
import random
list7: list[int] = [random.randint(10, 99) for i in range(10)]
print(list7)
list7_1: list [int] = [number % 10 for number in list7]
print (list7_1)
