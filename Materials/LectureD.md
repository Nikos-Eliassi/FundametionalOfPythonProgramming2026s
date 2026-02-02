> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🐍 Loops in Python

## 🔁 What is a loop?

> *A loop repeats the same block of code multiple times.*

> [!NOTE]  
> 💡 A program itself is already a loop. Python’s `Main` part is referred to as the main loop. `Main` can be executed from the first line and end after the last line. However, programs are often designed so that `Main` only stops when an external interruption occurs, as in the example below:

```py
import time

def main():
    print("Program running. Press Ctrl+C to exit.")
    try:
        while True:
            # Do something or wait
            print("Executing...")
            time.sleep(1)  # Waits 1 second
            pass  # Empty loop
    except KeyboardInterrupt:
        print("\nInterrupted. Closing the program.")

if __name__ == "__main__":
    main()
```

***

The most important loops in Python are:

*   🌀 **`for`** — iterates over an iterable (list, string, range, file, etc.)
*   🔂 **`while`** — repeats as long as a condition is true

***

## 🧩 `for` Loop in Practice

**✅ Basic form**

```py
for name in ["Anna", "Bashir", "Chen"]:
    print(f"Hello {name}!")
```

***

**🔢 `range()` → integer ranges**

```py
for i in range(5):          # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):   # 2,4,6,8
    print(i)
```

***

**🧮 `enumerate()` → both index and value**

> [!NOTE]  
> 💡 Learn this! → Excellent with lists

```py
students = ["Aino", "Ben", "Cai"]
for idx, name in enumerate(students, start=1):
    print(idx, name)
```

***

**🔗 `zip()` → iterate multiple sequences in parallel**

```py
usernames = ["anna", "ben", "cai"]
roles = ["student", "admin", "student"]

for u, r in zip(usernames, roles):
    print(f"{u} → {r}")
```

***

**🗂 Iterating over a dictionary**

```py
user = {"id": 17, "name": "Alex", "role": "student"}
for key, value in user.items():
    print(key, value)
```

***

## ⏳ `while` Loop → condition-controlled repetition

> [!NOTE]  
> 💡 Learn this! **→ When the condition is no longer met, execution stops.**

```py
balance = 3
while balance > 0:
    print("Access valid.")
    balance -= 1
print("No access.")
```

⚠️ **Beware:** if the condition never becomes false → **infinite loop!** → Pressing CTRL-C often helps terminate it.

***

## 🧭 `break`, `continue`, and the loop `else`

*   🛑 **`break`** stops the loop immediately
*   ⏩ **`continue`** jumps to the next iteration
*   🧩 **`else`** runs only if no `break` occurred

```py
users = ["alice", "bob", "root", "carl"]
for u in users:
    if u == "root":
        print("Admin found!")
        break
else:
    print("No admin found.")
```

***

If an element is empty:

```py
rows = ["Ville;08:00;room101", "", "Anna;09:00;lab2"]
for r in rows:
    if not r.strip():
        continue
    print("Processing:", r)
```

***

## 🧱 Nested loops

```py
days = ["Mon", "Tue"]
times = ["08:00", "10:00"]
for d in days:
    for t in times:
        print(d, t)
```

> [!NOTE]  
> 💡 Keep loops short, and split into logical functions when needed.

***

## ⚡ Looping vs. List Comprehension

**🧠 Traditional**

```py
numbers = [1, 2, 3, 4]
squared = []
for n in numbers:
    squared.append(n * n)
```

***

**✨ List comprehension (shorter and often faster)**

```py
numbers = [1, 2, 3, 4]
squared = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
```

***

## 🧠 Best Practices

✅ Don’t modify a list while iterating over it  
✅ Use `enumerate()` for clarity  
✅ Use `break` and `continue` judiciously

***

## 🧱 Typical Use Cases

**🧮 Accumulation**

```py
total = 0
for price in [12.5, 8.0, 3.5]:
    total += price
```

***

**🔍 Search**

```py
target = "ben"
for name in ["anna", "ben", "cai"]:
    if name == target:
        print("Found!")
        break
```

***

**🎯 Filtering**

```py
emails = ["a@x.com", "error", "b@y.com"]
valid = [e for e in emails if "@" in e]
```

***

**🧩 Parallel Lists**

```py
starts = ["08:00", "09:00", "10:00"]
rooms  = ["101", "202", "303"]
for s, r in zip(starts, rooms):
    print(f"{s} → room {r}")
```

***

## 🧾 Checklist

| Item                                             | Mastered |
| ------------------------------------------------ | -------- |
| 🔁 Difference between `for` and `while`          | ✔️       |
| 🧮 `range`, `enumerate`, `zip`                   | ✔️       |
| 🧱 `break`, `continue`, `else`                   | ✔️       |
| 🔍 Basic patterns (accumulation, search, filter) | ✔️       |
| ⚠️ Pitfalls (infinite while, modifying list)     | ✔️       |

***

## 🧠 Summary → **Remember These**

*   `for`: iterate over a sequence or collection
*   `while`: repeat until condition is false
*   `break` and `continue`: control loop flow
*   `else`: runs only if loop wasn’t interrupted
*   `List comprehensions`: efficient and clear

***

# 🚦 Conditional Statements in Python

## 📍 Why Use Conditionals?

Programming constantly involves making decisions:

*   What happens if the user logs in with the wrong password?
*   What if a file line is empty?
*   What if the booking date is in the past?

👉 **Conditionals allow the program to choose the execution path.**

***

In Python, the key structures are:

*   `if`
*   `elif`
*   `else`

***

## 🧩 Basic Structure

```py
if condition:
    # executed if condition is true
elif another_condition:
    # executed if previous was false, but this is true
else:
    # executed if none of the above conditions were true
```

Example:

```py
age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

***

## 🔢 Common Comparison Operators

| Operator | Purpose                  | Example        |
| -------- | ------------------------ | -------------- |
| `==`     | equal to                 | `a == 10`      |
| `!=`     | not equal to             | `a != 5`       |
| `<`      | less than                | `age < 15`     |
| `<=`     | less than or equal to    | `price <= 100` |
| `>`      | greater than             | `points > 80`  |
| `>=`     | greater than or equal to | `age >= 18`    |

***

## ⚙️ Logical Operators

Used to combine conditions:

| Operator | Meaning                   | Example                         |
| -------- | ------------------------- | ------------------------------- |
| `and`    | both must be true         | `age >= 18 and role == "admin"` |
| `or`     | at least one must be true | `points > 90 or bonus == True`  |
| `not`    | negates the value         | `not active`                    |

Example:

```py
age = 20
role = "student"

if age >= 18 and role == "student":
    print("Adult student")
```

***

## 📁 Conditionals in File Handling

This pattern appears in reservation systems, data cleaning, and log reading  **→ Copy the code and ask AI tools for clarification on each line and command if needed**

```py
with open("reservations.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        
        if not line:  # empty line
            continue
        
        parts = line.split("|")
        if len(parts) != 4:
            print("⚠️ Invalid line:", line)
            continue
        
        name, date, time, room = parts
        
        if not room.startswith("room"):
            print("❌ Invalid room:", room)
            continue
        
        print(f"OK: {name} → {room}")
```

***

**Conditionals can be used to (for example):**

*   filter out invalid lines
*   ensure correct value structure
*   prevent the program from crashing

***

## 🧠 Writing Clean Conditions (Best Practices)

**✔️ Good**

```py
if user and user.is_admin:
    ...
```

***

**👉 What does this do?**

1.  `if user`

    *   Checks that the `user` variable **is not empty** (not None, not False, not an empty string, dict, or list).
    *   In Python, this is the “pythonic” way to check existence.

2.  `user.is_admin`

    *   Directly checks if the user is an admin.
    *   No need to compare to `True` because if `is_admin` is a boolean, it works as a condition.

***

**⭐ Why is this good?**

*   Short and clear
*   Accepted and idiomatic in Python
*   Easy to read:  
    **“If user exists AND is admin…”**
*   Avoids unnecessary code
*   Doesn’t compare a boolean to a boolean

***

**❌ Bad**

```py
if user != None and user.is_admin == True:
    ...
```

***

**👉 What’s wrong with this?**

1.  **Unnecessary comparison `!= None`**

    *   In Python, `if user` is enough.
    *   `!= None` is clunky and non-idiomatic.
    *   If you want to be formal, use `is not None`.

2.  **Unnecessary comparison `== True`**

    *   Boolean values don’t need to be compared to True/False.
    *   Just use `if user.is_admin`.

3.  **Code is longer and harder to read**

    *   Extra words add no value.
    *   Makes the code heavier and beginner-like.

4.  **Logic is less safe**

    *   If `user` is `None`, Python evaluates `user != None` first → OK
    *   But if conditions are later changed incorrectly, it can lead to errors like  
        `"NoneType" object has no attribute 'is_admin'"`.

***

**🛑 Summary of the bad points**

*   Too much text
*   Less Pythonic
*   Compares booleans incorrectly
*   Doesn’t add safety
*   Harder to read and maintain

***

**📝 Tips**

*   Use **clear conditions** (avoid overly long combinations)
*   Break conditions into helper variables if needed

***

## 🎯 Nested Conditionals (nested if)

```py
age = 20
member = True

if age >= 18:
    if member:
        print("Access granted")
    else:
        print("Membership required")
else:
    print("Underage")
```

> [!NOTE]  
> 💡 If nested conditions become too deep, consider using `elif` or splitting logic into functions.

***

## 🚦 Conditionals in String Handling

```py
email = "test@example.com"

if "@" in email:
    print("Valid email")
else:
    print("⚠️ Invalid email")
```

```py
name = ""

if not name:
    print("Name is missing")
```

***

## 🔀 Ternary Operator (short if)

A compact way to choose a value:

```py
age = 20
status = "adult" if age >= 18 else "child"
print(status)
```

***

## 📊 Conditionals and Numbers

```py
points = 85

if points >= 90:
    print("Excellent")
elif points >= 75:
    print("Good")
elif points >= 50:
    print("Fair")
else:
    print("Failed")
```

***

## 🏁 Summary

📌 Conditionals are a key part of program decision-making. They can:

*   filter inputs
*   validate values
*   prevent errors
*   guide the program along the correct paths

> [!NOTE]  
> 💡 When you combine conditionals with loops and file handling, you can build more robust and fault-tolerant programs → such as reservation systems.

***

# 🧩 Practical Examples

**Printing a list without a trailing separator**

> [!NOTE]  
> 💡 Functions now include `input` → This makes the program easy to run using Visual Studio Code’s *play* button.

```py
def print_list():
    items = ["apple", "banana", "pear", "kiwi"]
    print("Fruits: ", end="")
    for i in range(len(items)):
        if i < len(items) - 1:
            print(items[i], end="-")
        else:
            print(items[i])  # Last item without '-'

def main():
    print_list()
    
    # Wait for user input before closing
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
```

**Same as above, but using the `join` method**

```py
def print_list():
    items = ["apple", "banana", "pear", "kiwi"]
    print("Fruits: ", end="")
    print("-".join(items))

def main():
    print_list()
    
    # Wait for user input before closing
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
```