> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🧩 Functions and Methods

In programming, both **functions** and **methods** perform a task — they take inputs and produce outputs. However, they are **not the same thing**. Let’s look at the difference clearly.

***

## 🔹 Function

A **function** is an *independent operation* that **does not belong to any specific object**. In Python, many functions are built-in, such as `print()`, `len()`, and `type()`.

***

**🧠 Core Idea**

*   A function is **called directly by its name**.
*   It **takes arguments** inside parentheses.
*   It **is not tied to any particular data type**.

***

**💡 Example: `print()` function**

```python
# Function: print()
print("This is a function example")
```

🔍 Here, `print()` is a **function** that outputs the given text to the console. It works regardless of the type of data you provide (string, int, float, etc.).

```python
print(123)
print(3.14)
print(["a", "b", "c"])
```

***

## 🔸 Method

A **method** is a *function that belongs to a specific object* — for example, a string, list, or dictionary. A method is **called through the object using the dot operator (. )**.

***

**🧠 Core Idea**

*   A method **always works in the context of a specific data type**.
*   It **modifies or processes that object**.
*   Called in the form:  
    `object.method(arguments)`

***

**💡 Example: `split()` method**

```python
# Method: split()
text = "This is an example"
words = text.split()

print(words)
```

🔍 Here, `split()` is a **method** that belongs to the **string object (`str`)**. It splits the string into parts at spaces and returns a list.

```python
text = "apple,pear,orange"
fruits = text.split(",")
print(fruits)
# outputs: ['apple', 'pear', 'orange']
```

***

## ⚖️ Comparison: Function vs. Method

| Feature                   | Function                      | Method                             |
| ------------------------- | ----------------------------- | ---------------------------------- |
| Belongs to an object      | ❌ No                          | ✅ Yes                              |
| How it’s called           | `print("hi")`                 | `"hi".split()`                     |
| Purpose                   | General operation             | Operation for a specific data type |
| Examples                  | `print()`, `len()`, `range()` | `split()`, `append()`, `lower()`   |
| Affects the object itself | ❌ Usually no                  | ✅ Often yes                        |

***

## 🧭 Summary

*   **Function**: General, standalone operation → e.g., `print()`
*   **Method**: Operation tied to an object → e.g., `"text".split()`

💬 You can think of it like this:

> A function is like a tool in a toolbox.  
> A method is like a tool that is built into a specific machine.

***

# 🐍 Introduction to Python Functions

## 🎯 What Are Functions?

A **function** is a part of a program that performs a specific task. Functions are used to make code **clearer, reusable, and easier to maintain.**

> 💡 Think of a function as a “small machine” in your program — it takes input, does something, and returns a result.

***

## 📦 Why Use Functions?

Functions help you:

*   avoid repeating code (DRY – *Don’t Repeat Yourself*)
*   break a large program into smaller parts
*   make code easier to read and test
*   reuse the same operations in different programs

***

## 🧱 Structure of a Function

In Python, a function is defined using the keyword `def`. General form:

```python
def function_name(parameters):
    """Optional documentation comment (docstring)."""
    # Functionality
    return value  # optional
```

**💡 Example:**

```python
def greet():
    print("Hello, world!")

greet()
```

🔍 Here, `greet()` is a function that takes no parameters and returns nothing — it simply **prints** text.

***

## 🧮 Parameters and Arguments

A function can receive **parameters**, i.e., values it uses internally.

```python
def greet(name):
    print(f"Hello, {name}!")
```

**🔍 When we call:**

```python
greet("Ville")
```

**📤 Output:**

```
Hello, Ville!
```

🧩 *Parameter* is a variable in the function definition.  
🧩 *Argument* is the value passed to the function when calling it.

***

## 🔁 Return Values (`return`)

A function can **return a value** using the keyword `return`.

```python
def sum_numbers(a, b):
    return a + b

result = sum_numbers(3, 5)
print(result)  # 8
```

If a function does not include a `return` statement, it returns `None` by default.

***

## 💬 Documentation Comments (Docstring)

You can add a **docstring** at the beginning of a function to describe its purpose:

```python
def square(x):
    """Calculates the square of a given number."""
    return x * x

print(square(4))      # 16
print(square.__doc__) # Prints the docstring
```

***

## ⚙️ Default Parameter Values

You can define **default values** for function parameters:

```python
def greeting(name="guest"):
    print(f"Hello, {name}!")

greeting()         # Hello, guest!
greeting("Aino")   # Hello, Aino!
```

***

## ✳️ Returning Multiple Values

In Python, a function can return **multiple values at once**:

```python
def numbers():
    return 10, 20, 30

a, b, c = numbers()
print(a, b, c)  # 10 20 30
```

This returns the values as a **tuple**.

***

## 🔍 Functions in Practice – Example

Here’s a small program that uses multiple functions:

```python
def ask_name():
    return input("Enter your name: ")

def create_greeting(name):
    return f"Hello, {name}! Welcome to programming."

def main():
    name = ask_name()
    greeting = create_greeting(name)
    print(greeting)

if __name__ == "__main__":
    main()
```

**🔎 What happens?**

1.  The program asks the user for their name
2.  A function builds the greeting
3.  The main program prints it

***

## 🧩 Summary

| Concept   | Explanation                     | Example            |
| --------- | ------------------------------- | ------------------ |
| `def`     | Defines a function              | `def calculate():` |
| Parameter | Variable in function definition | `def f(x):`        |
| Argument  | Value passed to the function    | `f(10)`            |
| `return`  | Returns a value                 | `return result`    |
| `__doc__` | Documentation string            | `print(f.__doc__)` |

***

# 🖨️ Python’s `print()` Function – The Core of Output

`print()` is one of Python’s **most commonly used built-in functions**. It allows a program to **display information to the user** — whether it’s text, numbers, calculations, or variable values.

***

## 🧩 Basic Usage

```python
print("Hello world!")
```

**📤 Output:**

```
Hello world!
```

➡️ The text is printed to the program’s execution environment (usually the terminal or console). `print()` **does not return a value** — it simply **displays information to the user**.

***

## 🔢 Printing Multiple Values

`print()` can take **multiple arguments**, separated by commas:

```python
name = "Ville"
age = 47
print("Hello", name, "you are", age, "years old.")
```

**📤 Output:**

```
Hello Ville you are 47 years old.
```

💡 Note: `print()` automatically adds **a space** between arguments.

***

## 🔧 Line Breaks and the `end` Parameter

By default, `print()` adds a **newline (`\n`)** at the end of each output. This means every `print()` call starts on a new line. You can change this behavior using the **`end` parameter**:

```python
print("Hello", end=" ")
print("world!")
```

**📤 Output:**

```
Hello world!
```

🧠 Here, `end=" "` means that instead of a newline, a space is added at the end of the output.

***

## 🔁 Changing the Separator – `sep` Parameter

`sep` defines **what character is used** between arguments. By default, `sep=" "` (a space), but you can change it:

```python
print("apple", "banana", "orange", sep=", ")
```

**📤 Output:**

```
apple, banana, orange
```

***

## 🧮 Printing Calculations

`print()` can also display the results of calculations:

```python
print("5 + 3 =", 5 + 3)
```

**📤 Output:**

```
5 + 3 = 8
```

***

## 🪄 F-Strings – A Stylish Way to Combine Text and Variables

`print()` works perfectly with **f-strings**:

```python
name = "Ville"
age = 47
print(f"Hello {name}, you are {age} years old.")
```

**📤 Output:**

```
Hello Ville, you are 47 years old.
```

💡 F-strings are extremely useful because they make output more readable and clear.

---

### ✅ Extra Python Tip: Align Text with `f-strings`

You can use **format specifiers** inside an f-string to control alignment and width. For example:

```python
var = "word"
print(f"{var:>8}")
```

**What it does:**

**`:>8` means:**
 * `>` → **right-align** the value
 * `8` → **width of 8 characters**

So if `var = 42`, the output will be:

```
      42
```

(6 spaces + `42` to make a total width of 8.)

***

💡 Other options:

*   `:<8` → left-align
*   `:^8` → center-align
*   You can also combine with fill characters:  
    `print(f"{var:*^8}")` → `***42***`

***

## 🧠 Printing Without Newlines in Multiple Steps

If you want to print **on the same line in multiple steps**, use `end=""`:

```python
for i in range(3):
    print(i, end=" ")
```

**📤 Output:**

```
0 1 2
```

***

## 🧱 Special Characters: `\n`, `\t`, etc.

You can use **escape characters** in output to add special formatting:

| Character | Meaning   | Example                  | Output         |
| --------- | --------- | ------------------------ | -------------- |
| `\n`      | Newline   | `print("Hello\nworld")`  | Hello<br>world |
| `\t`      | Tab       | `print("Apple\tBanana")` | Apple Banana   |
| `\\`      | Backslash | `print("C:\\file")`      | C:\file        |

***

## 📚 `print()` Technically

The `print()` function is defined as follows:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

**Explanation:**

| Parameter  | Description                                             |
| ---------- | ------------------------------------------------------- |
| `*objects` | The objects to print (one or more)                      |
| `sep`      | Separator between multiple values (default is space)    |
| `end`      | What to add at the end of the output (default newline)  |
| `file`     | Where to print (default is console)                     |
| `flush`    | Whether to flush the buffer immediately (rarely needed) |

***

## 🧭 Example Using All Parameters

```python
import sys

print("A", "B", "C", sep="-", end="!", file=sys.stdout, flush=True)
```

**📤 Output:**

```
A-B-C!
```

***

## ✨ Summary

| Feature          | Description             | Example                    |
| ---------------- | ----------------------- | -------------------------- |
| Basic printing   | Prints text             | `print("Hello")`           |
| Multiple values  | Prints multiple objects | `print("A", "B")`          |
| Change separator | Changes spacing         | `print("A", "B", sep=",")` |
| Remove newline   | Prints on same line     | `print("A", end="")`       |
| F-string         | Adds variables to text  | `print(f"Name: {name}")`   |

***

# ✂️ Python’s `split()` Method

`split()` is a **method of string objects (`str`)** that **splits a string into parts** based on a specified **delimiter**. The result is a **list** containing the separate parts of the string.

***

## 🔹 Basic Usage

```python
text = "apple pear banana"
fruits = text.split()

print(fruits)
```

**📤 Output:**

```
['apple', 'pear', 'banana']
```

🧠 If no delimiter is specified, `split()` splits on **whitespace** by default.

***

## 🔸 Specify Your Own Delimiter

You can define the character or string to split on:

```python
text = "apple,pear,banana"
fruits = text.split(",")
print(fruits)
```

**📤 Output:**

```
['apple', 'pear', 'banana']
```

💡 Now the split happens at commas instead of spaces.

***

## ⚙️ Any Character Can Be a Delimiter

```python
text = "student;developer;programmer"
words = text.split(";")
print(words)
```

**📤 Output:**

```
['student', 'developer', 'programmer']
```

***

## 🔢 Limit the Number of Splits (`maxsplit`)

`split()` can take an optional second argument: 👉 `maxsplit`, which defines **how many splits to perform**.

```python
text = "a b c d e"
parts = text.split(" ", 2)
print(parts)
```

**📤 Output:**

```
['a', 'b', 'c d e']
```

🧠 Here, only **two splits** are performed, so the last part remains intact.

***

## 🧹 Handling Multiple Spaces

If the string contains multiple consecutive spaces, `split()` treats them as one **if no delimiter is specified**:

```python
text = "Python   is    fun"
words = text.split()
print(words)
```

**📤 Output:**

```
['Python', 'is', 'fun']
```

💡 This makes `split()` handy for processing text with irregular spacing.

***

## 📄 Practical Example – Processing a File Line

Imagine reading a line from a booking system file:

```python
line = "Room101|2025-11-05|Ville Heikkiniemi|0401234567|ville@example.com"
data = line.split("|")

print(data)
```

**📤 Output:**

```
['Room101', '2025-11-05', 'Ville Heikkiniemi', '0401234567', 'ville@example.com']
```

Then you can handle the data individually:

```python
room = data[0]
date = data[1]
name = data[2]

print(f"Booking: {name} reserved {room} for {date}")
```

**📤 Output:**

```
Booking: Ville Heikkiniemi reserved Room101 for 2025-11-05
```

***

## 🧭 `split()` vs. `rsplit()`

`rsplit()` works like `split()`, but **starts splitting from the right**:

```python
text = "a,b,c,d,e"
print(text.split(",", 2))   # splits from the left
print(text.rsplit(",", 2))  # splits from the right
```

**📤 Output:**

```
['a', 'b', 'c,d,e']
['a,b,c', 'd', 'e']
```

***

## ⚠️ Empty String

If `split()` is called on an empty string without a delimiter, the result is an empty list:

```python
print("".split())
```

**📤 Output:**

```
[]
```

***

## 🧩 Summary

| Feature           | Description      | Example                   | Output              |
| ----------------- | ---------------- | ------------------------- | ------------------- |
| Default delimiter | Space            | `"a b c".split()`         | `['a', 'b', 'c']`   |
| Custom delimiter  | Chosen character | `"a,b,c".split(",")`      | `['a', 'b', 'c']`   |
| Limit splits      | `maxsplit`       | `"a b c d".split(" ", 2)` | `['a', 'b', 'c d']` |
| Multiple spaces   | Treated as one   | `"a   b".split()`         | `['a', 'b']`        |
| Empty string      | Empty list       | `"".split()`              | `[]`                |

***

**🧠 `split()`**:

*   is a **method of string objects**
*   **splits text into parts** based on a delimiter
*   **returns a list**
*   works efficiently for processing files, logs, and text input