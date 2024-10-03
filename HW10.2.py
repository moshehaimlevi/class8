# START

# SECTION A

# TRY AND EXCEPT:
# בTRY אנו משתמשים בשביל לשים בקוד בגלל שיכול להיות שיהיה חריגה בקוד במידה ולא הקוד ירוץ כרגיל.
#   ב EXCEPT אם הקוד בTRY נכשל המטרה של EXCEPT גורמת לקוד לא לקרוס ולהמשיך כרגיל בעיקר בכתיבת מלא שורות בקוד.

# SECTION B
# הסיבה העיקרית שכדאי למנוע קריסה של הקוד זה בגלל שאנחנו רוצים השתוכנית תרוץ כמו שצריך במיוחד אחרי כתיבה של הרבה שורות של קוד.
# מבנה קוד זה יכול גם לתת לנו משוב על בעיוצ שקרו במהלך הקוד

# SECTION C
try:
    result = 88 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("Execution complete.")

# SECTION D

number: int = 0
while True:
    try:
        number = int(input('enter number: '))
        if not 10 <= number <= 50:
            raise ValueError(f'{number} not in range')
        break
    except ValueError as e:
        print(e)

# SECTION E

list1 = [19, 4, 26, 37]
sentinel = -999
while True:
    try:
        number= int (input("enter an index:"))
        if number == sentinel:
            print('crashing out')
            break
        index = int(number)
        print(f"Value at index {number}: {list1[number]}")
    except ValueError:
        print("Invalid input!.")
    except IndexError:
        print("Index out of range! .")

# SECTION 
