> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🗂️ **Dictionary in Python → An Efficient Key–Value Data Structure**

## 📘 What Is a Dictionary?

A **dictionary** (also called a hash table or map) is a built-in Python data type that stores information as **key–value pairs**.

```python
{
    key1: value1,
    key2: value2,
    ...
}
```

A dictionary is an excellent choice when you want to:

*   look up data **by key**,
*   associate things with each other (e.g., name → phone number),
*   store structured data where each record has a clear identity.

***

## 🎯 Why Is a Dictionary Useful?

**✔️ Fast Lookup**

Access is usually **O(1)** → very fast.

***

**✔️ Readability**

The key tells you *what* the value represents:

```python
user["email"]
reservation["date"]
```

***

**✔️ Flexible Structure**

Values can be:

*   strings
*   integers
*   lists
*   other dictionaries
*   even functions!

***

**✔️ Easy to Modify**

You can add, remove, or update keys on the fly.

***

## 🔧 Creating a Dictionary

**Basic form:**

```python
user = {
    "name": "Ville",
    "email": "ville@example.com",
    "age": 40
}
```

***

**Empty dictionary:**

```python
data = {}
# or
data = dict()
```

***

**Adding a key–value pair:**

```python
user["phone"] = "040-123-4567"
```

***

## 🔍 Retrieving Values

**Direct lookup (error if key is missing):**

```python
print(user["name"])
```

***

**Safe lookup with `.get()` (does not raise an error):**

```python
print(user.get("address"))       # returns None if not found
print(user.get("address", "No address"))  # returns default value
```

This is especially useful during practice when keys might be missing.

***

Here’s the English translation with **update and delete operations included**:

***

## ✏️ Modifying a Dictionary

**Updating a value:**

```python
user["email"] = "new-mail@example.com"
```

***

**Adding or updating multiple values at once with `update()`:**

```python
user.update({
    "email": "new-mail@example.com",
    "phone": "040-123-4567"
})
```

***

**Deleting a key:**

```python
del user["age"]
# or safely:
user.pop("age", None)
```

***

**Clearing all values:**

```python
user.clear()
```

***

## 🔁 Iteration (Looping Through a Dictionary)

**Loop through keys only:**

```python
for key in user:
    print(key)
```

***

**Loop through keys and values:**

```python
for key, value in user.items():
    print(key, value)
```

***

**Values only:**

```python
for value in user.values():
    print(value)
```

***

## 🧱 Nested Dictionaries

**A dictionary can contain other dictionaries:**

```python
reservation = {
    "user": {"name": "Ville", "role": "admin"},
    "resource": {"id": 5, "name": "Meeting room"},
    "date": "2025-12-04"
}

print(reservation["user"]["role"])
```

**Output:**

```
admin
```

Structured data is very common, for example in [JSON formats](https://en.wikipedia.org/wiki/JSON).

***

## 🧪 Dictionary vs List

| Feature       | Dictionary                              | List               |
| ------------- | --------------------------------------- | ------------------ |
| Order         | Preserves insertion order (Python 3.7+) | Ordered            |
| Lookup method | By key                                  | By index           |
| Best use case | Structured data, identifiers            | Ordered collection |

Example in a reservation system:

*   **List** → multiple reservations in order
*   **Dictionary** → fields of a single reservation by keys

***

## ⚠️ Pitfalls and Considerations

**❗ Keys must be *unique***

```python
d = {"a": 1, "a": 2}
print(d)  # {"a": 2}
```

***

**❗ Keys must be *hashable***

Typically:

*   `str` ✔️
*   `int` ✔️
*   `tuple` ✔️
*   `list` ✖️ not allowed

***

**❗ `.get()` is better than `[ ]` in uncertain situations**

***

## ✨ Best Practices

**✔️ Use clear, descriptive keys**

```python
good = {"price": 10.5}
bad  = {"p": 10.5}
```

***

**✔️ Combine dictionaries into meaningful units**

Example reservation:

```python
reservation = {
    "id": 1,
    "user_id": 3,
    "room": "A123",
    "date": "2025-12-04"
}
```

***

**✔️ Use dictionary comprehension**

```python
squares = {x: x*x for x in range(5)}
```

***

## 🧰 Example: Storing a User

```python
def create_user(name, email, age):
    return {
        "name": name,
        "email": email,
        "age": age
    }

user = create_user("Ville", "ville@example.com", 40)
print(user)
```

***

## 🎓 Summary

A dictionary is one of Python’s most important data structures and is used in almost every application → from web development to data structures and file formats like JSON.

***

# 🧱 **Object-Oriented Programming → What and Why?**

## 📜 Background and History

In the 1970s and 1980s, software systems grew rapidly in complexity. Traditional procedural programming (where programs consisted of long chains of functions and subroutines) became difficult to manage. There arose a need to model programs in a way similar to the real world.

Pioneers included:

*   **Simula** (1967) → the first language to introduce the concept of classes.
*   **Smalltalk** (1972) → the first pure object-oriented language where *everything* was an object.
*   In the 1990s: **C++**, **Java**, **Python**, and later **C#** brought object-oriented programming into widespread use.

The core historical idea was:

> “If programs are modeled like real-world entities and phenomena, they become easier to understand, maintain, and extend.”

Object-oriented programming quickly became one of the main paradigms in software development, and today it is used almost everywhere — from web and mobile apps to games and server-side systems.

***

## 🧠 What Is an Object?

An object in a program is a **unit** that combines:

*   **data** (attributes)
*   **behavior** (methods / functions)

You can think of an object as a “small program inside a program.”  
For example, a Dog object contains:

*   data: name, age, breed
*   actions: bark(), eat(), sleep()

So an object is *data + behavior + interface under one logical unit*.

***

## 🎯 Why Use Objects?

Here are the main reasons from a software engineering perspective:

**✔️ Structure and Manageability**

Objects break a large program into smaller logical units.  
As the program grows, an object-oriented structure remains much easier to maintain.

***

**✔️ Reusability**

Classes can create multiple objects, and classes can inherit from other classes.  
This reduces repetitive code and supports efficient development.

***

**✔️ Easier to Modify**

If, for example, the engine calculation in a car changes, you only update the Engine class.  
You don’t need to fix the entire program.

***

**✔️ Abstraction and Encapsulation**

An object hides its internal workings.  
The user gets clear methods (an “interface”) without needing to know how the object works internally.

***

**✔️ A Natural Way to Model the World**

When designing an application:

*   user → object
*   reservation → object
*   game character → object
*   bank account → object

This approach is intuitive, especially for large projects.

***

# 🐍 Object-Oriented Programming in Python

In Python, object-oriented programming (OOP) is a core part of the language, but Python does not force you to use it. You can write procedural scripts or build large object-oriented systems → the choice is yours. This flexibility makes Python an excellent teaching language.

## 🔑 Common Object-Oriented Programming Terms

### 🧱 **1. Class**

A blueprint or template for creating objects.  
Defines attributes (data) and methods (behavior).

```python
class Car:
    pass
```

***

### 🚗 **2. Object (Instance)**

A concrete instance created from a class.

```python
c = Car()  # c is an object
```

***

### 🎒 **3. Attribute (Field / Property)**

A variable that belongs to an object or class.

```python
self.name = "Alice"
```

*   **Instance attribute** → specific to each object
*   **Class attribute** → shared across all objects

***

### ⚙️ **4. Method**

A function defined inside a class.

```python
def drive(self):
    print("Driving")
```

***

### 🏗️ **5. Constructor (`__init__`)**

A special method called when creating an object; initializes attributes.

```python
def __init__(self, name):
    self.name = name
```

***

### 📦 **6. Encapsulation**

Bundling data + behavior together, and controlling access.

Examples:

*   Private attributes (`_hidden`)
*   Public methods

***

### 🧬 **7. Inheritance**

A class can inherit attributes and methods from another class.

```python
class ElectricCar(Car):
    pass
```

***

### 🔁 **8. Polymorphism**

Same interface, different behavior.

Example: two classes both have `.start()`, but each implements it differently.

***

### 🔄 **9. Overriding**

Subclass replaces a method from its parent class.

```python
class ElectricCar(Car):
    def start(self):
        print("Silently starting...")
```

***

### ➕ **10. Overloading** *(Python supports limited overloading)*

Same method name with different parameter sets.  
Python mainly emulates this using default arguments or `*args`.

***

### 🧩 **11. Composition**

Building complex objects from smaller objects.

```python
class Engine:
    ...

class Car:
    def __init__(self):
        self.engine = Engine()
```

***

### 🧱 **12. Aggregation**

A weaker form of composition — objects can exist independently.

***

### 🧰 **13. Abstraction**

Hiding internal details; showing only the necessary interface.

***

### 🎛️ **14. Interface (Python: Protocol, ABC)**

A group of method signatures that a class promises to implement.

Using `abc` module:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

***

### 📚 **15. Namespace**

A “container” where names (variables, functions, classes) live.

Examples:

*   Local namespace
*   Global namespace
*   Class namespace

***

### 📦 **16. `self`**

Represents the current object instance inside a class method.

***

### 🏭 **17. Classmethod (`@classmethod`)**

A method that receives the class (`cls`) instead of the instance.

Useful for alternate constructors like `.from_list()`.

***

### 🧪 **18. Staticmethod (`@staticmethod`)**

A method inside a class that does not access instance or class data.

***

### 📐 **19. Property (`@property`)**

Allows method-based attribute access that looks like a normal attribute.

```python
@property
def area(self):
    return self.width * self.height
```

***

### 🧱 **20. `__dunder__` Methods (Magic Methods)**

Special methods Python uses for operator overloading and object behavior.

Examples:

*   `__init__`
*   `__repr__`
*   `__str__`
*   `__len__`
*   `__eq__`
*   `__add__`

***

## 🔧 Defining a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def bark(self):           # method
        print(f"{self.name} barks!")
```

**What’s happening here?**

*   `class Dog:`  
    Defines a class.
*   `__init__`  
    Python automatically calls this when creating a new object.
*   `self`  
    Refers to *this* object. Every method in a class receives `self` as its first parameter.
*   `self.name` and `self.age`  
    These are stored inside the object.

***

## 🐾 Creating an Object

```python
my_dog = Dog("Max", 5)
my_dog.bark()
```

Output:

```
Max barks!
```

**Explanation**

*   `Dog("Max", 5)` creates a new object.
*   `my_dog` is a reference to that object.
*   `my_dog.bark()` calls the object’s method.

***

## 🗂️ Attributes and Methods

Inside an object, you can have:

*   **Attributes** (data)
*   **Methods** (functions that operate on that data)

Example with an added method:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")
```

***

## 🧬 Inheritance

Inheritance allows you to extend a class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats food.")

class Dog(Animal):          # Dog INHERITS from Animal
    def bark(self):
        print(f"{self.name} barks!")
```

Usage:

```python
d = Dog("Buddy")
d.eat()
d.bark()
```

Output:

```
Buddy eats food.
Buddy barks!
```

***

## 🔒 Encapsulation in Practice

Python does not enforce strict `private` attributes, but uses naming conventions:

*   `_name` → “don’t use this outside without a good reason”
*   `__name` → name mangling, makes the attribute harder to access

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # semi-private

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```

***

## 🧱 Difference Between Class and Object

| Concept    | Explanation                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| **Class**  | A structure, blueprint, or template that defines what objects can be created. |
| **Object** | A concrete instance of a class with its own state.                            |

Analogy:

*   **Class = mold**
*   **Object = item made from the mold**

***

## 📦 Example: A Small App Built with Objects

```python
class Reservation:
    def __init__(self, user, resource, date):
        self.user = user
        self.resource = resource
        self.date = date

    def summary(self):
        return f"{self.user} booked {self.resource} on {self.date}"


res1 = Reservation("Ville", "Meeting Room", "2025-12-10")
print(res1.summary())
```

Output:

```
Ville booked Meeting Room on 2025-12-10
```

This demonstrates the main idea of objects: ➡️ **Combine data and related behavior into one logical unit.**