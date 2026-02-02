> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 💡 Python’s Official Style Guide → PEP 8

[PEP 8](https://peps.python.org/pep-0008/) is Python’s official *style guide*, which defines how Python code should be written to make it clear, readable, and consistent. The purpose of the guide is to make collaboration easier, reduce errors, and make code more professional.

## 🔑 Key Principles

*   **Indentation**  
    Use four spaces per level. No tabs (IDE environments like Visual Studio Code automatically convert tabs to four spaces).

*   **Line Length**  
    The recommended maximum is 79 characters. Long expressions can be split across multiple lines.

*   **Blank Lines**  
    Use blank lines to separate logical sections.

*   **Imports**  
    Imports go at the top of the file, one per line, ordered as: standard library → third-party libraries → your own modules.

*   **Naming Conventions**

    *   functions and variables: `lowercase_with_underscores`
    *   classes: `CapWords`
    *   constants: `UPPER_CASE`

*   **Spacing and Layout**  
    Keep spaces clear, for example around operators (`a + b`), but avoid unnecessary spaces inside parentheses.

*   **Comments and Documentation**  
    Comments should be understandable and up to date. Docstrings are written with triple quotes for functions, classes, and modules.

## 🎯 Why is PEP 8 Important?

*   Improves code **readability** and **maintainability**.
*   Makes collaboration **smoother**, since everyone follows the same rules.
*   Provides a foundation for **professional Python development**.

***

# 🧠 **Variables and Arithmetic Operations**

## 1️⃣ What is a Variable?

A variable is a named storage location where a program can store information. You can think of a variable as a box with a name, into which you can put values.

*   A variable **is created when it is assigned a value**.
*   Its contents can be used in programming at any time.
*   The value can also change — hence the name *variable*.

***

**💡 Example:**

```python
age = 25
name = "Ville"
temperature = -3.5
```

## 2️⃣ Naming Variables

Python allows:

✔ Letters  
✔ Numbers (not at the beginning)  
✔ Underscore `_`

Best practices:

*   Use descriptive names: `total_price`, `average_speed`
*   Use snake\_case style: words separated by underscores
*   Do not start with a number

❌ Avoid: `1name`, `x`, `Price€`

***

## 3️⃣ Basic Data Types in Python Variables

| Type    | Example          | Usage             |
| ------- | ---------------- | ----------------- |
| `int`   | `age = 30`       | Whole numbers     |
| `float` | `temp = 3.14`    | Decimal numbers   |
| `str`   | `text = "Hello"` | Text data         |
| `bool`  | `is_open = True` | True/False values |

***

## 4️⃣ Arithmetic Operations in Python

**💡 Basic Calculations:**

| Operation        | Symbol | Example                           |
| ---------------- | ------ | --------------------------------- |
| Addition         | `+`    | `5 + 3`                           |
| Subtraction      | `-`    | `10 - 2`                          |
| Multiplication   | `*`    | `7 * 2`                           |
| Division         | `/`    | `10 / 2` → result is always float |
| Integer Division | `//`   | `10 // 3` → result is 3           |
| Modulus          | `%`    | `10 % 3` → result is 1            |
| Exponentiation   | `**`   | `2 ** 3` → result is 8            |

***

## 5️⃣ Calculating with Variables

Variables can be used just like regular numbers:

```python
a = 10
b = 3

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print(sum_result, difference, product, quotient)
```

***

**💡 Updating a Variable’s Value**

```python
counter = 0
counter = counter + 1
```

A shorter and more common way:

```python
counter += 1
```

Also available: `-=`, `*=`, `/=`, `//=`, `%=`

***

## 6️⃣ Arithmetic in Practice – A Small Reservation System Example

Imagine a simple reservation system that calculates the booking price:

```python
hours = 5
price_per_hour = 12.5

total_price = hours * price_per_hour

print("The total booking price is:", total_price, "€")
```

Output:

```
The total booking price is: 62.5 €
```

***

## 7️⃣ Combining Text and Numbers

Text and numbers must be combined using the **str()** function if you use the `+` operator:

```python
age = 20
print("Age is " + str(age))
```

Or use an f-string (recommended modern approach):

```python
print(f"Age is {age}")
```

***

# 🗂️ **Working with Lists**

## 1️⃣ What is a List?

A list is an ordered collection of values.  
You can think of a list as a shelf where each position has a number and a value.

*   List values can be *of any type*
*   Lists are mutable (they can be changed)
*   Values are accessed by index  
    → indexes start at 0

***

**💡 Example:**

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "Ville", True, 3.14]
```

***

## 2️⃣ Accessing Values from a List

**💡 By Position (Index):**

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[2])  # cherry
```

***

**💡 Last Element:**

```python
print(fruits[-1])  # cherry
```

***

## 3️⃣ Changing a Value

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"

print(fruits)  # ["apple", "orange", "cherry"]
```

***

## 4️⃣ Adding and Removing Elements

**💡 Add to List**

```python
numbers = [1, 2, 3]

numbers.append(4)       # adds to the end
numbers.insert(1, 10)   # adds at position 1

print(numbers)  # [1, 10, 2, 3, 4]
```

***

**💡 Remove from List**

```python
numbers.remove(10)   # removes value 10
numbers.pop()        # removes the last element
numbers.pop(0)       # removes element at index 0
```

***

## 5️⃣ List Length

```python
names = ["Liisa", "Matti", "Ville"]
print(len(names))   # 3
```

***

## 6️⃣ Looping Through a List

**💡 For Loop:**

```python
cars = ["Audi", "BMW", "Volvo"]

for car in cars:
    print(car)
```

***

**💡 With Indexes:**

```python
for i in range(len(cars)):
    print(i, cars[i])
```

***

## 7️⃣ Sorting and Reversing a List

**💡 Sort:**

```python
numbers = [5, 1, 8, 3]
numbers.sort()

print(numbers)  # [1, 3, 5, 8]
```

***

**💡 Reverse Sort:**

```python
numbers.sort(reverse=True)
```

***

**💡 Reverse Without Sorting:**

```python
numbers.reverse()
```

***

## 8️⃣ List Comprehension — Efficient List Operations

A short way to create lists:

```python
numbers = [x * 2 for x in range(5)]
print(numbers)  # [0, 2, 4, 6, 8]
```

***

**💡 Example from a Reservation System: Create a List of Name Tags**

```python
names = ["Ville", "Anna", "Matti"]
tags = [name.lower() for name in names]
```

***

# 🧩 **Two-Dimensional Lists (2D Lists)**

A two-dimensional list = a list whose elements are lists. You can imagine it as a matrix or a table:

```
[ [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]
```

## 1️⃣ Creating

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## 2️⃣ Accessing Values

```python
print(matrix[0][1])  # result 2
print(matrix[2][0])  # result 7
```

First index = row  
Second index = column

***

## 3️⃣ Iterating Through a Two-Dimensional List

**💡 Traditional Way:**

```python
for row in matrix:
    for value in row:
        print(value)
```

***

**💡 With Indexes:**

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

***

## 4️⃣ Practical Example of a Two-Dimensional List

Imagine a reservation system where we create a 7-day, 24-hour booking calendar initialized with 0 (free):

```python
calendar = [[0 for hour in range(24)] for day in range(7)]

# Mark Monday at 10:00 as booked
calendar[0][10] = 1

print(calendar[0][10])  # 1 (booked)
```

***