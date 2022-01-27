print("Hello World!")
message = "Hello World"
food = ["Banana", "Apple", "Lays", "Fish"]

# ki írja a message betűit
for letter in message:
    print(letter)

# ki írja az összes karaktert az első 'o'-ig és azzal együtt
for letter in message:
    print(letter)
    if "o" == letter.lower():
        break

# ki írja a message betűit kivéve az 'o'-t
for letter in message:
    if "o" != letter.lower():
        print(letter)

# ki írja a lista elemeit.
for item in food:
    print(item)

# ki írja azokat az elemeket a listából amik tartalmazzák az a betűt
for item in food:
    if "a" in item.lower():  # az item vizsgálata ugy hogy kicsi a betű
        print(item)

long_numbers = [123000, 345600, 478900, 1234567]

# ki írja a long_numbers-ből azokat az elemeket amikbe van 1-es
for number in long_numbers:
    if "1" in str(number):
        print(number)

# ki írja azokat a számokat amikbe van 1-es és 2-es is.
for number in long_numbers:
    if "1" and "2" in str(number):
        print(number)