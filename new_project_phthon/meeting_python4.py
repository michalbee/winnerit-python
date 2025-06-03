"""
# מצגת מפגש 4

# HOME WORK תרגיל 1

print("----------------------")

print("תרגיל 1")

text = input("press string: ")

print("Simple Input string: ", text)

print("Simple Output: ", text[0:4])


# HOME WORK תרגיל 2

print("----------------------")

print("תרגיל 2")

text = input("press string: ")

print("Simple Input string: ", text)

new_text = text[-1] + text[:-1]

print("Simple Output: ", new_text)

#HOME WORK תרגיל 3

print("----------------------")

print("תרגיל 3")

text=input("press tring: ")

print("Simple Input string: ",text)

new_text=text[1::2]

print("Simple Output: ",new_text)


#CLASS WORK תרגיל 4

print("תרגיל 4")

text=input("press string: ")

print("----------------------")

print("Simple Input string: ",text)

print("Simple Output: ",text.upper())

# CLASS WORK תרגיל 5

print("----------------------")

print("תרגיל 5")

text = input("press string: ")

print("Simple Input string: ", text)

new_text = text[0:3].upper() + text[3:len(text) - 3].lower() + text[len(text) - 3:len(text)].upper()

print("Simple Output: ", new_text)


#HOME WORK תרגיל 1 רשימה מחרוזות

print("----------------------")

print("מחרוזות תרגיל 1")

text="ABCDEFGHIJKLMNOP"

print("Simple Input string: ",text)

print(text[0])

print(text[-1])

print(text[len(text)//2])

print(text[0::2])

print(text[1::2])

print(text[::-1])

# HOME WORK תרגיל 2 רשימה מחרוזות

print("----------------------")

print("מחרוזות תרגיל 2")

text = "red yellow green blue black white pink orang purple"

print("Simple Input string: ", text)

print(text.lower())

print(text.upper())

print(text.title())

print("words: ", text.split())

# HOME WORK תרגיל 3 רשימה מחרוזות

print("----------------------")

print("מחרוזות תרגיל 3")

number_str1 = "1920"

number_str2 = "1080"

print("Enter sfreen width in pixels: ", int(number_str1))

print("Enter sfreen height in pixels: ", int(number_str2))

print("resolution:", int(number_str1), "*", int(number_str2))

print("Total pixels:", int(number_str1) * int(number_str2))

"""
# HOME WORK תרגיל 4 רשימה מחרוזות

print("----------------------")

print("מחרוזות תרגיל 4")

numbers = list(range(1, 17))

sum = 0

print(numbers)
sum+=numbers.pop(-1)
sum+=numbers.pop(0)
sum+=numbers.pop(12)
sum+=numbers.pop(7)

print("המערך החדש",numbers)
print("סך האברים שהוסרו",sum)
if a>b:
    print (a)