> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 📥 Inputs as Part of Programming

## 🧠 Why Do Programs Need Inputs?

Every program solves a problem. To solve that problem, the program must receive **information from the user**, the environment, or another system. This information is called **input**.

Input enables, for example:

*   providing a name, age, address, or other text
*   making choices (y/n, yes/no)
*   entering numbers for calculations
*   selecting files
*   submitting a form on a web page
*   triggering an action (e.g., “Start reservation,” “Send order”)
*   decision-making (what the program does next)

Without inputs, a program would always be **completely static** → It would perform exactly the same task every time with unchanging data.

***

## 📦 Different Forms of Input

Input can come from many sources:

**✔️ User Inputs (human → program)**

Examples:

*   text typed into a field
*   entering a number
*   selecting radio buttons or dropdown lists
*   clicking a button with a mouse

***

**✔️ Files (file → program)**

Examples:

*   reading a CSV or JSON file
*   processing an image or video file
*   analyzing a log file

***

**✔️ Web Requests (browser → server)**

Examples:

*   HTTP POST form data to a web service
*   API call (e.g., JSON data)

***

**✔️ Sensors and Devices (physical world → program)**

Examples:

*   temperature sensors
*   IoT devices
*   keyboard / touchscreen

***

**✔️ Environment Variables**

Example: server environment variables:

```bash
DATABASE_URL=postgres://...
```

The program **reads the input**, processes it, and produces **output**.

***

## ✍️ Inputs in Different Interfaces

The interface determines **how**, **when**, and **in what form** input is received.

***

**🖥️ Command-Line Application (CLI), e.g., our Python scripts**

*   Input is typed from the keyboard.
*   Uses the `input()` function.
*   Great for learning: simple, direct, focuses on logic.
*   Input validation and control are the programmer’s responsibility.

**Example: Handling Python CLI input:**

```py
name = input("Enter your name: ")
print("Hello", name)
```

***

**🌐 Graphical User Interface (GUI)**

*   Input comes from text fields, buttons, menus.
*   Technologies: Tkinter, PyQt, React, Flutter, Electron…
*   Code reacts to events: “button clicked,” “text changed.”

***

**🌍 Web Interface**

*   Inputs are HTML elements:

  ```html
  <input type="text" name="email">
  <input type="number" name="age">
  <button type="submit">Send</button>
  ```

*   Data is sent to the server:

    *   as **GET** parameters
    *   as **POST** form data
    *   as JSON in an API call

***

**🤖 Backend System Inputs**

*   API calls
*   Cron jobs
*   Database queries
*   Webhooks

***

## ✅ How Is Input Processed on a Web Page?

Let’s look at a short practical flow.

**1️⃣ HTML Input**

```html
<form action="/submit" method="POST">
    <input type="text" name="username" placeholder="Your name">
    <input type="number" name="age">
    <button type="submit">Send</button>
</form>
```

***

**2️⃣ Browser Sends Data to the Server**

For example, in POST format:

```
username=Ville&age=38
```

***

**3️⃣ Server Processes the Data (e.g., Python/Flask)**

```py
from flask import request

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["username"]
    age = int(request.form["age"])
    return f"Hello {name}, you are {age} years old."
```

***

**🔧 What Happened?**

1.  The user entered data into the form.
2.  The browser packaged it in `application/x-www-form-urlencoded` format.
3.  The server unpacked the data.
4.  The code validated and used the input.

***

## ✨ How Is This Different from Our Python Scripts?

**🧪 Python Script → Inputs Are Handled in the Same Program**

*   Input is given via the command line.
*   There is no separate browser layer.
*   Validation and error handling are done directly in the code.
*   Input flow and logic are fully under the programmer’s control.

**Example in a script:**

```py
name = input("Your name: ")
age = int(input("Your age: "))
print(name, age)
```

***

**🌍 On the Web → Input Passes Through Multiple Layers**

| Layer         | Role                         |
| ------------- | ---------------------------- |
| HTML          | Input fields                 |
| Browser       | Sends data to the server     |
| HTTP protocol | Transports the data          |
| Backend code  | Receives and validates input |
| Database      | Stores the data              |

**🔍 Web Inputs Have More Risks:**

*   SQL injections
*   XSS (Cross-Site Scripting)
*   CSRF (Cross-Site Request Forgery)
*   Fake forms
*   Spam injections

**That’s why the web requires:**

*   backend validation
*   frontend validation
*   security measures

***

**☝️ In Python Command Line, the biggest issue is:**

*   wrong data type (e.g., user types “cat” when a number is expected)

***

## 🗂️ The Role of Inputs in Programming Thinking

Inputs are part of the broader programming process:

**🎯 Input → Processing → Output**

The basic formula of programming:

```
Input → Logic → Result
```

***

**🎛️ Input Controls Program Flow**

*   conditional choices
*   functions that take arguments
*   loops that depend on user input

***

**🔁 Input Enables Program “Interactivity”**

Without inputs, a program is just a passive machine.

***

## 🛕 Connection to This Course

In this course:

*   We start with **command-line inputs**, because:

    *   they are simple
    *   they reveal the basic structures of programming
    *   they strengthen thinking skills: conditions, loops, error handling, validation

*   Later in your studies:

    *   web forms
    *   API endpoint inputs
    *   values inserted into databases

**When you master handling `input()`:**

*   you understand how data flows into a program
*   moving to web programming becomes easier
*   validation and data type thinking are already familiar

***

## 💡 Example: Same Idea in Python Script and on the Web

**🐍 Python (CLI)**

```py
name = input("Enter your name: ")
print("Hello", name)
```

***

**🌐 Web (HTML + Backend)**

```html
<form action="/hello" method="POST">
    <input type="text" name="nimi">
    <button>Send</button>
</form>
```

**Backend:**

```py
name = request.form["name"]
return f"Hello {name}"
```

***

🟩 The idea is the same → Only the **interface and data flow path change**.

***

# 🧲 Using Python `input` Inputs

## 💻 What Does `input()` Do?

```py
name = input("Enter your name: ")
print("Hello", name)
```

*   `input("...")` **displays the text** to the user.
*   The program **waits for input**.
*   The line the user types **is always returned as a string (`str`)**.

> Important: `input()` never returns `int` or `float` directly — you must convert it yourself.

***

## 🔎 Converting Input to Different Data Types

**Integer (`int`)**

```py
age_str = input("Enter your age (years): ")
age = int(age_str)  # type conversion str -> int
print("Next year you will be", age + 1)
```

👉 If the user types something that can’t be converted to an integer (e.g., "cat"), the program crashes with a `ValueError`. That’s why we need validation (see below).

***

**Floating-Point (Decimal) Number (`float`)**

```py
height_str = input("Enter your height in meters (e.g., 1.75): ")
height = float(height_str.replace(",", "."))  # convert comma to dot
print("Height in meters:", height)
```

*   Finnish users often write a **decimal comma** — you can fix it with `replace(",", ".")`.

***

**Boolean (`bool`)**

It’s often more convenient to interpret yes/no input yourself:

```py
answer = input("Do you want to continue? (y/n): ").strip().lower()

if answer == "y":
    proceed = True
elif answer == "n":
    proceed = False
else:
    print("Unknown answer, assuming we won't continue.")
    proceed = False
```

***

**What Data Types Mean in Practice**

*   `str` – names, addresses, messages
*   `int` – counts, quantities, ages, points
*   `float` – prices, measurements, temperatures
*   `bool` – yes/no choices, states (on/off)

***

## ✅❌ Input Validation → Basic Principles

Core question: **“Is the input valid?”**

Typical validation steps:

1.  Is the input **empty**?
2.  Is the input of the **correct type** (integer, float…)?
3.  Is the value **within an allowed range** (e.g., 0–120)?
4.  Is the input one of the **allowed options** (e.g., "y", "n")?

***

**1️⃣ Example: Age Between 0–120**

```py
age_str = input("Enter your age (0–120): ")

if not age_str.isdigit():
    print("Error: age must be an integer.")
else:
    age = int(age_str)
    if 0 <= age <= 120:
        print("Thank you, your age is", age)
    else:
        print("Error: age must be between 0–120.")
```

***

**2️⃣ Repeated Asking Until the Input Is Valid**

Often we want to **ask again** until the user provides a correct input.

```py
while True:
    age_str = input("Enter your age (0–120): ")

    if not age_str.isdigit():
        print("Error: enter an integer.")
        continue  # go back to the start of the while loop

    age = int(age_str)

    if 0 <= age <= 120:
        print("Thank you, your age is", age)
        break  # exit the loop
    else:
        print("Error: age must be between 0–120.")
```

***

**3️⃣ `try` / `except` – Handling Errors in Input**

`isdigit()` doesn’t work for all kinds of numbers (e.g., -5, 3.14). In those cases, `try/except` is a good tool.

```py
while True:
    inp = input("Enter an integer: ")

    try:
        number = int(inp)
        print("You entered:", number)
        break
    except ValueError:
        print("Error: that was not an integer. Try again.")
```

**Same for floating-point numbers:**

```py
while True:
    inp = input("Enter temperature (°C): ")

    try:
        temperature = float(inp.replace(",", "."))
        print("The temperature is", temperature, "°C")
        break
    except ValueError:
        print("Error: enter a number, e.g., 21.5")
```

***

## 🔗 Input Chains → Multiple Inputs in Sequence

An **input chain** = the program asks several things in sequence, and later questions may depend on earlier answers.

**Example: Simple Reservation Prompt**

```py
print("Welcome to the reservation system!")

name = input("Enter your name: ").strip()
date = input("Enter reservation date (dd.mm.yyyy): ").strip()
duration_str = input("Reservation duration in hours: ").strip()

try:
    duration = int(duration_str)
except ValueError:
    print("Error: duration must be an integer. Using default 1 h.")
    duration = 1

print("\nSummary:")
print(f"Name: {name}")
print(f"Date: {date}")
print(f"Duration: {duration} h")
```

**Extras for Input Chains:**

*   Clean the input: `.strip()`, `.lower()`, `.upper()`
*   Check choices against a list:

```py
types = ["auto", "vene", "mökki"]
type_ = input("What would you like to reserve (auto/vene/mökki)? ").strip().lower()

if type_ not in types:
    print("Unknown type, defaulting to 'auto'.")
    type_ = "auto"
```

***

## 🔁 Ending and Restarting a Program Using Inputs

A common pattern: the program has a **main loop** that repeats until the user wants to quit.

**➡️ Simple “shall we continue?” structure**

```py
while True:
    number_str = input("Enter a number, I will double it: ")
    try:
        number = float(number_str.replace(",", "."))
        print("Double value:", number * 2)
    except ValueError:
        print("Error: that was not a number.")
    
    cont = input("Do you want to calculate another number? (y/n): ").strip().lower()
    if cont != "y":
        print("Program ends. Bye!")
        break
```

*   `while True:` runs indefinitely until a `break` statement is executed.
*   The user **decides** when the program ends.

***

**👉🏻 A small menu-based program**

Here the user can choose an action or exit the program entirely:

```py
def calculate_sum():
    a = float(input("Enter the first number: ").replace(",", "."))
    b = float(input("Enter the second number: ").replace(",", "."))
    print("The sum is:", a + b)

def calculate_average():
    count_str = input("How many numbers? ")
    try:
        count = int(count_str)
    except ValueError:
        print("Error: count must be an integer.")
        return

    numbers = []
    for i in range(count):
        number = float(input(f"Enter number {i+1}: ").replace(",", "."))
        numbers.append(number)

    avg = sum(numbers) / len(numbers)
    print("The average is:", avg)

while True:
    print("\nMENU")
    print("1) Calculate the sum of two numbers")
    print("2) Calculate the average of multiple numbers")
    print("3) Exit the program")

    choice = input("Choose (1-3): ").strip()

    if choice == "1":
        calculate_sum()
    elif choice == "2":
        calculate_average()
    elif choice == "3":
        print("Thanks for using the program, it will now end.")
        break  # program ends
    else:
        print("Unknown choice, please try again.")
```

**Here:**

*   **Program restart** = return to the menu.
*   **Program exit** = choose “3” and `break`.

> ☝️ You could also use `sys.exit()`, but `break` and loops are often clearer for beginners.

***

## 🎯 Summary

*   `input()` **always returns a string** → perform the necessary type conversions (`int`, `float`, `bool`).
*   **Validation** is important: don’t blindly trust the user.
    *   Check whether the input has the correct format.
    *   Use `while` + `try/except` when needed.
*   **Input chains** form small “forms” on the command line — multiple inputs in sequence.
*   You can **end** and **restart actions** using:
    *   a main loop (`while True`)
    *   menus (1, 2, 3, …)
    *   the `break` command when the user chooses to quit.

***