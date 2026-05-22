from datetime import datetime

print("Welcome to The Interactive Personal Data Collector")
print()
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in ft: "))
favourite_number = int(input("Please enter your favourite number: "))
print()
print("Thank you! Here is the information we collected:")

print()
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})")
print()

current_year = datetime.now().year
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")
print()
print("Thank you for using The Interactive Personal Data Collector. Goodbye!")
