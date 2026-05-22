# Interactive Personal Data Collector 🧾

## 📌 Project Description

The **Interactive Personal Data Collector** is a beginner-friendly Python project that collects personal information from the user using input statements and displays detailed information about the entered data.

This project demonstrates important Python concepts such as:

- Variables
- Data Types
- Type Casting
- User Input
- String Formatting
- Memory Address Identification
- Date & Time Handling
- Arithmetic Operations

The program also calculates the user's approximate birth year using the current year and the entered age.

---

# 🚀 Features

✅ Collects user information interactively  
✅ Displays variable data types  
✅ Displays memory addresses using `id()`  
✅ Uses Python `datetime` module  
✅ Calculates approximate birth year  
✅ Beginner-friendly and easy to understand  
✅ Uses formatted output with f-strings  

---

# 🛠 Technologies Used

- Python 3
- Python Standard Library (`datetime` module)

---

# 📂 Project Structure

```bash
PR. 1 Fundamental Booster
│
├── PR. 1 Fundamental Booster.png
├── PR. 1 Fundamental Booster.py
└── readme.md
```

---

# 🧠 Concepts Used

## 1. Variables

Variables are used to store user information.

Example:

```python
name = input("Please enter your name: ")
```

---

## 2. Data Types

This project uses multiple Python data types:

| Data Type | Example |
|----------|----------|
| String (`str`) | Name |
| Integer (`int`) | Age |
| Float (`float`) | Height |

---

## 3. Type Casting

Type casting converts one data type into another.

Example:

```python
age = int(input("Please enter your age: "))
```

- `int()` converts input into integer
- `float()` converts input into decimal number

---

## 4. f-Strings

Used for formatted output.

Example:

```python
print(f"Name: {name}")
```

---

## 5. type() Function

The `type()` function is used to display the data type of a variable.

Example:

```python
type(name)
```

Output:

```python
<class 'str'>
```

---

## 6. id() Function

The `id()` function displays the memory address of a variable.

Example:

```python
id(name)
```

---

## 7. datetime Module

The `datetime` module is used to get the current year.

Example:

```python
current_year = datetime.now().year
```

---

# ⚙️ How the Program Works

## Step 1

The program displays a welcome message.

```python
print("Welcome to The Interactive Personal Data Collector")
```

---

## Step 2

The user enters:

- Name
- Age
- Height
- Favourite Number

---

## Step 3

The program stores the data in variables.

---

## Step 4

The program displays:

- Entered value
- Data type
- Memory address

---

## Step 5

The program calculates approximate birth year.

Formula used:

```python
birth_year = current_year - age
```

---

# 💻 Code Explanation

## Importing Module

```python
from datetime import datetime
```

Imports the `datetime` class from the `datetime` module.

---

## Taking Input

```python
name=input("Please enter your name: ")
```

Takes user input and stores it in the `name` variable.

---

## Integer Conversion

```python
age=int(input("Please enter your age: "))
```

Converts entered age into integer.

---

## Float Conversion

```python
height=float(input("Please enter your height in meters: "))
```

Converts height into floating-point value.

---

## Displaying Information

```python
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
```

Displays:

- Variable value
- Data type
- Memory address

---

## Birth Year Calculation

```python
current_year=datetime.now().year
birth_year=current_year-age
```

Calculates approximate birth year using current year.

---

# ▶️ How to Run the Program

## Step 1: Open Terminal

Navigate to the project folder.

```bash
cd PR.1 FUNDAMENTAL BOOSTER
```

---

## Step 2: Run Python File

```bash
python '.\PR. 1 Fundamental Booster.py'
```

---

# 🖥 Output

![Project Output](PR.%201%20Fundamental%20Booster.png)
---

# 🎯 Learning Outcomes

After completing this project, I learned:

- How to take user input in Python
- How to work with multiple data types
- How to perform type conversion
- How to use Python built-in functions
- How to use the `datetime` module
- How to format output professionally

---

# 📚 Beginner Friendly

This project is perfect for Python beginners who want to practice:

- User Input
- Variables
- Functions
- Type Casting
- Basic Python Logic

---

# 👨‍💻 Author

## Krish Patel

Data Analytics Learner.

---

# 🔗 Resources

- **GitHub Repository**: [https://github.com/patel0506/PR.-1-Fundamental-Booster/tree/master](https://github.com/patel0506/PR.-1-Fundamental-Booster/tree/master)

- **Video Tutorial**: [Watch Video](video.mp4)