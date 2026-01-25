> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🧩 Why do programs need different data types?

## 🧠 1. What does a data type mean?

A data type defines **what kind of values a variable can hold** and **what operations can be performed** on those values.  
Data types are fundamental principles of programming—they tell the computer how to process data.

> For example, you can perform calculations with numbers, but you can’t directly add text together.

---

## 💬 2. Why are data types needed?

A computer ultimately processes everything as bits (0 and 1).  
The programmer’s job is to specify **how these bits should be interpreted**.

### 💡 Example:

```
01000001
```

*   If interpreted as a **character (char)** → it’s the letter `A`
*   If interpreted as a **number (int)** → it’s the value `65`

So the same bit sequence can mean different things depending on the data type.  
A data type **gives meaning to data.**

---

## 🎯 3. Data types help programs work correctly

Without data types, a program wouldn’t know:

*   how much memory to allocate
*   what kinds of calculations are allowed
*   how to display or store the information

### 🔍 Example in Python:

```python
a = 5        # integer (int)
b = 2.5      # decimal number (float)
c = "5"      # text (str)

print(a + b)     # works → result 7.5
print(a + c)     # error → cannot add int + str
```

---

## 📦 4. Different data types serve different purposes

| Data Type | Example                      | Purpose                     |
| --------- | ---------------------------- | --------------------------- |
| `int`     | 10                           | calculations, counters      |
| `float`   | 3.14                         | decimals, measurements      |
| `str`     | "Hello world"                | text, names, messages       |
| `bool`    | True / False                 | condition checks, decisions |
| `list`    | \[1, 2, 3]                   | storing multiple values     |
| `dict`    | {"name": "Ville", "age": 35} | key–value pairs             |

---

## 🧱 5. Using data types makes programs more reliable

When the correct data types are used:  
✅ Fewer errors  
✅ Code is easier to read and maintain  
✅ Program runs more efficiently  
✅ Security improves (cannot process incorrect data)

---

## 🧮 6. Practical analogy

Think of data types as **containers in a kitchen**:

| Container     | Corresponds to data type | What it can hold      |
| ------------- | ------------------------ | --------------------- |
| Glass         | `float`                  | water, juice (liquid) |
| Plate         | `str`                    | bread, cheese (text)  |
| Measuring cup | `int`                    | whole measurements    |

If you try to pour juice onto a plate, it doesn’t work—just like trying to add text and numbers in a program!

---

## ✨ 7. Summary 

**Different data types are needed so that:**

*   the computer knows what kind of data it’s handling
*   the program uses memory and calculations correctly
*   errors can be detected early
*   code stays clear and reliable

> ➕ Data types are the building blocks of programming—without them, programs would just be a chaotic collection of bits!

---

# 🧩 Data Types in Practice – Example: Reservation System

Imagine we are building a small **reservation system** where users can book **meeting rooms** or **other resources**.

The program needs various kinds of information:

*   Who is booking
*   What is being booked
*   When it is booked
*   Whether the booking is confirmed

All of these are represented using **different data types**.

---

## 🧍 1. User Information → *string (`str`)* and *integer (`int`)*

The user’s name, email, and ID are stored as text (strings).  
If the user has an age or an ID number, those are integers.

```python
user_name = "Mika Virtanen"        # str
user_email = "mika@virtanen.com"   # str
user_age = 22                      # int
```

➡️ These are used to identify the person making the booking and possibly to check, for example, that they are over 15 years old.

---

## 🕒 2. Reservation Time → *date and time (`datetime`)*

Each reservation has a **start and end time**.  
In Python, these can be handled with the `datetime` type, which allows comparisons and calculations.

```python
from datetime import datetime

start_time = datetime(2025, 10, 30, 14, 0)
end_time = datetime(2025, 10, 30, 16, 0)
```

➡️ This makes it possible to check whether reservations overlap.

---

## 🏠 3. Reserved Resource → *string (`str`)*

The name or identifier of the resource is usually text:

```python
resource_name = "Meeting Room A"  # str
```

If resources have **capacity** (e.g., 10 people), it can be stored as an integer:

```python
capacity = 10  # int
```

---

## ✅ 4. Reservation Confirmed or Not → *boolean (`bool`)*

Is the reservation approved, canceled, or still pending?  
For this, we use the `bool` type.

```python
confirmed = True    # reservation is confirmed
canceled = False    # reservation is not canceled
```

➡️ These values help the interface display only active reservations.

---

## 📋 5. Reservation Lists → *list (`list`)*

The system usually has multiple reservations.  
They can be stored in a list, making it easy to iterate through all reservations:

```python
reservations = ["Reservation 1", "Reservation 2", "Reservation 3"]
```

Or as a list of objects/dictionaries if we want to keep more details:

```python
reservations = [
    {"user": "Mika", "resource": "Meeting Room A", "time": "14:00-16:00"},
    {"user": "Satu", "resource": "Meeting Room B", "time": "12:00-13:00"}
]
```

---

## 🧠 6. A Single Reservation → *dictionary (`dict`)*

All the details of a single reservation can be collected into one dictionary:

```python
reservation = {
    "user_name": "Mika Virtanen",   # str
    "resource": "Meeting Room A",   # str
    "start": datetime(2025, 10, 30, 14, 0),  # datetime
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": True,              # bool
    "participants": 4               # int
}
```

➡️ This is convenient because all parts of the reservation are in one structure.

---

## 🧱 7. Summary of Data Types Used

| Data Type  | Purpose                                   | Example                               |
| ---------- | ----------------------------------------- | ------------------------------------- |
| `str`      | Names, emails, resource names             | `"Mika Virtanen"`, `"Meeting Room A"` |
| `int`      | Age, capacity, identifiers                | `22`, `10`, `12345`                   |
| `float`    | Price or duration                         | `2.5` hours                           |
| `bool`     | Whether reservation is confirmed/canceled | `True`, `False`                       |
| `datetime` | Reservation time                          | `datetime(2025, 10, 30, 14, 0)`       |
| `list`     | Multiple reservations or users            | `[reservation1, reservation2, ...]`   |
| `dict`     | All details of one reservation            | `{"user": ..., "resource": ...}`      |

---

## 💬 8. Why is this important?

When the reservation system uses **the correct data types**, the program works correctly and reliably:

*   Overlapping reservations can be prevented using time (`datetime`)
*   User identification works based on text (`str`)
*   Capacity can be compared as numbers (`int`)
*   Reservation logic is clear (`bool`)

---

## 🧩 Complete Example

```python
from datetime import datetime

reservation = {
    "user_name": "Mika Virtanen",
    "resource": "Meeting Room A",
    "start": datetime(2025, 10, 30, 14, 0),
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": True,
    "participants": 4
}

print(f"Reservation: {reservation['resource']} at {reservation['start'].strftime('%H:%M')}–{reservation['end'].strftime('%H:%M')}")
```

📤 Output:

```
Reservation: Meeting Room A at 14:00–16:00
```

---

# 🧩 Python Data Types with Examples

In Python, everything is an object—including data types.  
A data type tells you **what kind of data a variable contains** and **how it can be processed**.

---

## 🔢 1. Integers – `int`

Integers are numbers without decimals.

```python
age = 25
students = 32
year = 2025

print(age + 5)      # 30
print(year - 2000)  # 25
print(students * 2) # 64
```

💡 **Use:** counters, ages, quantities, identifiers  
📏 **Example:** user’s age, number of reserved seats

---

## 💧 2. Decimal Numbers – `float`

Decimal numbers include fractional parts.  
They are suitable for measurements and monetary calculations.

```python
temperature = 21.5
price = 9.99
duration = 2.5  # hours

print(temperature + 2.0)  # 23.5
print(price * 2)          # 19.98
```

💡 **Use:** prices, measurements, percentages  
📏 **Example:** reservation duration in hours

---

## ⚙️ 3. Complex Numbers – `complex`

The `complex` type is used for mathematical calculations involving **real and imaginary parts**.  
Rarely used in basic programming, but important in scientific computing.

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
print(z * 2)   # (6+8j)
```

💡 **Use:** electrical engineering, physics, signal processing  
📏 **Example:** complex forms of voltage and current

---

## 🧵 4. Strings – `str`

Strings store text.  
They can be concatenated, formatted, and sliced.

```python
name = "Mika Virtanen"
room = 'Meeting Room A'

print("Welcome, " + name + "!")
print(f"Reservation made for {room}.")
```

💡 **Use:** names, emails, textual data  
📏 **Example:** resource name, user’s email

---

## ✅ 5. Boolean Values – `bool`

`bool` indicates whether a condition is **true (True)** or **false (False)**.

```python
confirmed = True
over_15 = False

if confirmed:
    print("Reservation confirmed ✅")
else:
    print("Reservation pending ❌")
```

💡 **Use:** decisions, conditions, logical checks  
📏 **Example:** whether the user is over 15 years old

---

## 📋 6. Lists – `list`

A list is an **ordered and mutable** collection of values.

```python
reservations = ["A", "B", "C"]

print(reservations[0])  # A
reservations.append("D")
print(reservations)     # ["A", "B", "C", "D"]
```

💡 **Use:** storing multiple values, repetitive structures  
📏 **Example:** list of all reservations

---

## 🗂️ 7. Dictionaries – `dict`

A dictionary contains **key–value pairs**, similar to JSON.

```python
reservation = {
    "user": "Mika Virtanen",
    "room": "Meeting Room A",
    "confirmed": True
}

print(reservation["user"])  # Mika Virtanen
```

💡 **Use:** data structures, API data, database objects  
📏 **Example:** a single reservation

---

## 📦 8. Tuples – `tuple`

A tuple is similar to a list, but it is **immutable**.

```python
time_slot = ("14:00", "16:00")

print(time_slot[0])  # 14:00
# time_slot[0] = "13:00"  # ❌ Error
```

💡 **Use:** fixed values, coordinates, time intervals  
📏 **Example:** reservation start and end time

---

## 🧮 9. Sets – `set`

A `set` contains **only unique values** and does not preserve order.

```python
resources = {"A", "B", "A"}
print(resources)  # {"A", "B"}

resources.add("C")
print(resources)  # {"A", "B", "C"}
```

💡 **Use:** removing duplicates, set operations  
📏 **Example:** unique resources

---

## 🧩 10. Frozen Sets – `frozenset`

`frozenset` is like `set`, but **immutable**.

```python
permissions = frozenset({"view", "edit"})
# permissions.add("delete")  # ❌ Error
```

💡 **Use:** fixed sets of values, e.g., permissions

---

## 🕹️ 11. Range – `range`

`range` generates a sequence of integers, often used in loops.

```python
for i in range(3):
    print(i)
# 0, 1, 2
```

💡 **Use:** loops, counters  
📏 **Example:** iterating through hours in a reservation day

---

## 🧱 12. Bytes and Bytearray – `bytes`, `bytearray`

Used for storing binary data, such as files or data transmitted over a network.

```python
data = b"Hello"
print(data[0])  # 72 (ASCII code)

mutable_data = bytearray(b"Hi")
mutable_data[0] = 65  # 'A'
print(mutable_data)   # bytearray(b'Ai')
```

💡 **Use:** data transfer, file handling, cryptography

---

## 🚫 13. NoneType – `None`

`None` means **no value**.  
It is Python’s way of representing emptiness or undefined state.

```python
result = None

if result is None:
    print("No result available yet.")
```

💡 **Use:** return values, uninitialized variables  
📏 **Example:** reservation not yet confirmed → `confirmed = None`

---

## 🧠 14. Summary Table

| Data Type   | Description          | Mutable | Example              | Typical Use             |
| ----------- | -------------------- | ------- | -------------------- | ----------------------- |
| `int`       | Integer              | ✅       | `42`                 | counters, quantities    |
| `float`     | Decimal number       | ✅       | `3.14`               | prices, measurements    |
| `complex`   | Complex number       | ✅       | `3+4j`               | technical calculations  |
| `str`       | Text                 | ✅       | `"Hello"`            | names, messages         |
| `bool`      | Boolean              | ✅       | `True`               | conditions, checks      |
| `list`      | Ordered collection   | ✅       | `[1, 2, 3]`          | multi-value data        |
| `tuple`     | Immutable list       | ❌       | `(1, 2)`             | fixed values            |
| `set`       | Unique values        | ✅       | `{1, 2, 3}`          | set operations          |
| `frozenset` | Immutable set        | ❌       | `frozenset({1, 2})`  | fixed permissions       |
| `dict`      | Key–value pairs      | ✅       | `{"name": "Eemeli"}` | data structures         |
| `range`     | Sequence of integers | ✅       | `range(0, 5)`        | loops                   |
| `bytes`     | Binary data          | ❌       | `b"Hello"`           | data transfer           |
| `bytearray` | Mutable binary data  | ✅       | `bytearray(b"Hi")`   | editable binary data    |
| `NoneType`  | No value             | —       | `None`               | uninitialized variables |

---

## 🧩 15. Example Program: Data Types in a Reservation System

```python
from datetime import datetime

reservation = {
    "user": "Mika Virtanen",   # str
    "age": 22,                 # int
    "room": "Meeting Room A",  # str
    "start": datetime(2025, 10, 30, 14, 0),
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": None,         # NoneType (not yet approved)
    "price": 25.50,            # float
    "participants": ["Satu", "Antti", "Joonas"], # list
    "time_slot": ("14:00", "16:00"),  # tuple
    "permissions": frozenset({"view"}), # frozenset
}

print(f"{reservation['user']} booked {reservation['room']} from {reservation['time_slot'][0]}–{reservation['time_slot'][1]}")
if reservation["confirmed"] is None:
    print("Reservation is pending ⏳")
```

📤 **Output:**

```
Mika Virtanen booked Meeting Room A from 14:00–16:00
Reservation is pending ⏳
```

---

## ✨ Summary

Python’s data types cover everything:

🔹 Numbers (`int`, `float`, `complex`)  
🔹 Text and logic (`str`, `bool`)  
🔹 Collections (`list`, `tuple`, `set`, `dict`)  
🔹 Special cases (`range`, `bytes`, `NoneType`, `frozenset`)

> 🎯 When you know how to choose the right data type, your program will be faster, less error-prone, and easier to understand.

---

# 🔄 Python Type Conversions

Python is a **dynamically typed language**, meaning a variable’s type is determined automatically by its value.  
However, programmers often need to **convert one data type to another** to process data correctly.

---

## 🧠 1. Why are type conversions needed?

Programs often deal with data in different forms:

*   🧾 **User input** always comes as text (`str`)
*   ➕ **Calculations** only work with numbers (`int` or `float`)
*   ✅ **Boolean values** (`bool`) are needed for conditions
*   🔢 **Output** combines text and numbers

> 👉 In these cases, you need to convert the type before using it.

---

## 🧩 2. Two Ways to Convert Types

### 1️⃣ Implicit Conversion (*automatic*)

Python does this automatically when it’s safe:

```python
num_int = 5
num_float = 2.5
result = num_int + num_float  # int → float

print(result)        # 7.5
print(type(result))  # <class 'float'>
```

💡 Here, Python converted the `int` value to `float` automatically so the calculation could be done without losing information.

---

### 2️⃣ Explicit Conversion (*explicit conversion*)

The programmer performs the change manually using conversion functions such as:

```python
int()   float()   str()   bool()   list()   tuple()   set()
```

---

## 🔢 3. Converting to Numbers (`int`, `float`)

### 🔸 Text → integer (`int`)

```python
text = "42"
num = int(text)
print(num + 1)   # 43
```

### 🔸 Text → decimal (`float`)

```python
price_text = "19.99"
price = float(price_text)
print(price * 2)  # 39.98
```

💡 **Remember:** The text must be *in the correct format*, otherwise you’ll get an error:

```python
int("42a")  # ❌ ValueError
```

---

## 🧮 4. Converting to Text (`str`)

All values can be converted to a string:

```python
age = 25
print("Age is " + str(age) + " years.")
```

or with an **f-string (recommended)**:

```python
print(f"Age is {age} years.")
```

💡 F-strings are a modern and clear way to combine text with different data types.

---

## ✅ 5. Converting to Boolean (`bool`)

In Python, almost all values can be interpreted as true or false.

| Value                                | Interpreted as |
| ------------------------------------ | -------------- |
| `0`, `0.0`, `""`, `[]`, `{}`, `None` | `False`        |
| All other values                     | `True`         |

```python
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("Hello"))  # True
```

💡 This is often used in conditionals:

```python
username = "Ville"
if username:
    print("Username provided")
```

---

## 📋 6. Converting to Collections (`list`, `tuple`, `set`)

Python allows conversions between different collection types.

### 🔸 Tuple → List

```python
t = ("A", "B", "C")
lst = list(t)
print(lst)  # ['A', 'B', 'C']
```

### 🔸 List → Tuple

```python
lst = ["A", "B", "C"]
t = tuple(lst)
print(t)  # ('A', 'B', 'C')
```

### 🔸 List → Set (removes duplicates)

```python
lst = ["A", "A", "B"]
unique = set(lst)
print(unique)  # {'A', 'B'}
```

---

## 🧱 7. Conversion to Binary (`bytes` and `bytearray`)

```python
text = "Hello"
binary = bytes(text, "utf-8")
print(binary)  # b'Hello'

# back to text
decoded = binary.decode("utf-8")
print(decoded)  # Hello
```

💡 **Use:** in data transfer, file handling, web applications

---

## 🚫 8. Conversion to “Empty” (`NoneType`)

If you don’t want to assign a value to a variable yet, use `None`:

```python
result = None

if result is None:
    print("No result yet.")
```

---

## 🧠 9. Practical Example – Reservation System

User input comes as text.  
The program converts it to the correct data types before processing:

```python
# User inputs
participants_input = "5"
price_input = "12.50"
confirmed_input = "True"

# Convert data types
participants = int(participants_input)
price = float(price_input)
confirmed = confirmed_input == "True"  # str → bool

total = participants * price

print(f"Participants: {participants}, Total Price: {total} €, Confirmed: {confirmed}")
```

📤 **Output:**

```
Participants: 5, Total Price: 62.5 €, Confirmed: True
```

---

## 🧩 10. Summary Table

| Conversion      | Function               | Example          | Result    |
| --------------- | ---------------------- | ---------------- | --------- |
| Text → Integer  | `int()`                | `int("5")`       | `5`       |
| Text → Float    | `float()`              | `float("3.14")`  | `3.14`    |
| Number → Text   | `str()`                | `str(42)`        | `"42"`    |
| List → Tuple    | `tuple()`              | `tuple([1,2,3])` | `(1,2,3)` |
| Tuple → List    | `list()`               | `list((1,2,3))`  | `[1,2,3]` |
| List → Set      | `set()`                | `set([1,1,2])`   | `{1,2}`   |
| Value → Boolean | `bool()`               | `bool("")`       | `False`   |
| Text → Binary   | `bytes(text, "utf-8")` | `"A"`            | `b"A"`    |
| Binary → Text   | `decode()`             | `b"A".decode()`  | `"A"`     |

---

## ✨ 11. Summary

*   🧩 Python can sometimes convert data types automatically (*implicit conversion*)
*   👨‍💻 Most of the time, the programmer must do it manually (*explicit conversion*)
*   💡 Conversions are needed to combine different data types safely and logically

> 🎯 The right type conversion is like translation — it ensures all parts of the program “speak the same language.”

---