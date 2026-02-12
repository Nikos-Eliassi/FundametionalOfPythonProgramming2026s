> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 📁 Files, Operating System, and Python: What Happens?

File handling is one of the most important aspects of programming. Every application, from small scripts to large services, **reads**, **writes**, **updates**, and **deletes** data using mechanisms provided by the operating system.

## 🧠 How Does the Operating System See a File?

The operating system manages everything related to files:

*   where they are located (storage device, path)
*   who can read/write (permissions)
*   how data flows between the program and storage media (I/O stack)
*   how files are locked, cached, and synchronized

When a program opens a file, the OS provides a `file handle`, which the program uses to access the file.

***

## 📖 What Happens When a File Is Read?

For example, in Python:

```py
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

The operating system does the following:

1.  **📌 Path Check**  
    Does the file exist? Are permissions correct?

2.  **🔑 File Opening**  
    The OS associates a file handle with the program → `f` is just a *pointer* to this handle.

3.  **📤 Data Transfer**  
    Data is read from disk into a **buffer** and then to the program: reading doesn’t happen “bit by bit”; the OS optimizes the process.

4.  **📦 Representation in Python**  
    File content is converted into a string (`str`) or bytes (`bytes`), depending on the mode.

***

## ✍️ What Happens When Writing to a File?

Example:

```py
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("New content")
```

The OS does:

1.  **📌 Path Check**  
    Is writing allowed? Is there enough disk space?

2.  **🧽 Possible File Clearing**  
    `w` mode empties the file before writing.

3.  **📥 Buffering**  
    Data doesn’t go directly to disk → it’s first written to a *buffer*.

4.  **💾 Flush → Sync → Disk**  
    The OS writes data to disk, often with a slight delay:

    *   `f.write` → buffer
    *   `f.flush` → OS
    *   `fsync` → physical disk

Writing is multi-step, and the OS optimizes it for speed.

***

## 🧲 Why Is Proper File Opening and Closing So Important?

**✔️ 1. Prevent Data Corruption**  

If a file remains open, the last writes may stay in the buffer → not saved to disk.

***

**✔️ 2. Free Resources**  

Open files consume:

*   file handles (limited per process)
*   memory (buffers)
*   possible locks (`file locks`)

***

**✔️ 3. Release File Locks**  

If a file is locked, other applications can’t access it → **issues in multi-user systems**.

***

**✔️ 4. Easier Error Handling**  

Using `with open(...)` ensures the file closes automatically — even if an error occurs.

***

## 🐍 Proper Python Usage

**📦 Reading a File**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

***

**✍️ Writing to a File**

```py
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello world!\n")
```

***

**➕ Appending to a File**

```py
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Added line\n")
```

***

**💾 Reading a File Line by Line**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

***

## ⚠️ Danger Zones → These Will Crash Scripts and Programs!

**❌ 1. File Not Closed**

→ data may not be saved  
→ OS lock remains active  
→ resource leak

That’s why **never use**:

```py
f = open("data.txt", "w")
f.write("Hello")
# f.close() was forgotten!
```

***

**❌ 2. Writing Without Permissions**

→ `PermissionError`  
→ program may crash  
→ logs won’t update

***

**❌ 3. Accidental File Wipe**

`w` mode **always overwrites** the file.  
Safer options:

*   `a` (append)
*   or `r+` if you want to read and write without clearing

***

**❌ 4. File Paths: Windows vs Linux**

Windows → `C:\\data\\file.txt`  
Linux → `/home/user/data/file.txt`

Better approach:

```py
from pathlib import Path

path = Path("data") / "log.txt"
```

***

**❌ 5. Large Files → Memory Issues**

`f.read()` reads the ENTIRE file at once.

Better approach:

```py
for chunk in f.read(1024):
    process(chunk)
```

***

**❌ 6. Concurrent Writes**

→ data can get corrupted  
→ requires locks or transactions

***

## 🎓 Summary

| Aspect       | Why Important?                        | Python Example             |
| ------------ | ------------------------------------- | -------------------------- |
| File Opening | Creates a connection to the file      | `open("file.txt")`         |
| File Handle  | OS provides a resource to the program | `f = open(...)`            |
| Reading      | Data → buffer → program               | `f.read()`                 |
| Writing      | Program → buffer → disk               | `f.write()`                |
| Closing      | Frees resources + saves data          | `f.close()` or `with open` |
| Danger Zones | Prevent crashes and data errors       | `with open(...)`           |

***

# 🐍 Bad vs Good Practices in Python

The web is full of tips and tricks for file handling. Since a script/program interacts with files and the file system through the operating system, wrong practices can cause unpredictable situations. The OS often runs multiple programs simultaneously, so resources are shared. The same applies to users — there may be multiple users accessing resources at the same or different times.

## 1️⃣ Forgotten `close()` → “It works anyway…”

**❌ Bad Practice**

```py
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
# f.close() was forgotten
```

**Why is this a problem?**

*   The file may **remain open**:

    *   Buffers may not flush correctly.
    *   OS resources are consumed (too many open files).
    *   In long-running services, this becomes a major issue.

***

**✅ Better Practice → Use `with` Statement**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# File is automatically closed here
```

***

## 2️⃣ Opening in Wrong Mode and Losing Data

**❌ Bad Practice → “Just open with `w` and write”**

```py
# Intended to add a new log entry, but...
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("New log line\n")
```

**Why is this a problem?**

*   `w` mode **empties the entire file first**.
*   If logs or data are important, you destroy all previous content every time.

***

**✅ Better Practice → Use `a` or More Careful Logic**

```py
# Append new lines to the existing file
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log line\n")
```

Or check first:

```py
from pathlib import Path

log_path = Path("log.txt")
if log_path.exists():
    mode = "a"
else:
    mode = "w"

# THIS WORKS TOO: mode = "a" if log_path.exists() else "w"

with open(log_path, mode, encoding="utf-8") as f:
    f.write("New log line\n")
```

***

## 3️⃣ The All-Swallowing `except:` Hides Errors

**❌ Bad Practice → “Let’s just fix it with try–except”**

```py
try:
    f = open("data.txt", "r")
    data = f.read()
    f.close()
except:
    print("Something went wrong")
```

**Why is this a problem?**

*   `except:` catches **everything**:

    *   including programming errors (IndentationError, NameError, etc.)
    *   including KeyboardInterrupt (Ctrl+C)
*   You don’t see **what actually went wrong**.
*   Errors are easily hidden → harder to debug.

***

**✅ Better Practice → Narrow the error and use `with`**

```py
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found – check the path.")
except PermissionError:
    print("No permission to read the file.")
```

If needed, you can add a “general” catch, but separately:

```py
except Exception as e:
    print(f"Unexpected error: {e}")
```

***

## 4️⃣ Using `eval()` on File Contents → A Security Classic 💣

You sometimes see tips online like “read settings or data with the `eval` function.”

**❌ Really Bad Practice**

```py
with open("config.txt", "r", encoding="utf-8") as f:
    config = eval(f.read())  # e.g. "{'debug': True}"
```

**Why is this dangerous?**

*   `eval()` executes **any Python code**:

    *   if an attacker can modify the file → arbitrary code execution
    *   never suitable for situations where data comes from outside
*   This is a direct security risk.

***

**✅ Better Practice → Use a Safe Format**

For example, JSON:

```py
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(config["debug"])
```

***

## 5️⃣ Loading Everything into Memory at Once → Works in a Demo, Not in Production

**❌ Bad Practice → Read megabytes or gigabytes at once**

```py
with open("really_big_file.log", "r", encoding="utf-8") as f:
    data = f.read()  # entire file into memory
    # processing...
```

**Why can this be a problem?**

*   If the file is large:

    *   memory usage grows massively
    *   the script slows down and may crash
*   Works in “sample code,” but not in real environments.

***

**✅ Better Practice → Line by Line or in Chunks**

**Line by line:**

```py
with open("really_big_file.log", "r", encoding="utf-8") as f:
    for line in f:
        process(line)
```

---

**In chunks:**

```py
def read_in_chunks(file_obj, chunk_size=1024):
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data

with open("big.bin", "rb") as f:
    for chunk in read_in_chunks(f):
        process_binary(chunk)
```

***

## 6️⃣ Hard-Coded Paths → “Works on my machine” 🧨

**❌ Bad Practice**

```py
# Hard-coded Windows path
f = open("C:\\Users\\Ville\\Desktop\\data\\tiedot.txt", "r", encoding="utf-8")
```

**Why is this bad?**

*   It won’t work:

    *   for another user
    *   on another operating system
    *   on a server
*   Breaks portability (the classic “works on my machine” syndrome).

***

**✅ Better Practice → Relative Paths and `pathlib`**

```py
from pathlib import Path

base_dir = Path(__file__).parent  # directory where the script resides
data_file = base_dir / "data" / "tiedot.txt"

with open(data_file, "r", encoding="utf-8") as f:
    content = f.read()
```

***

## 7️⃣ Multiple Functions Sharing a “Global” File Handle

**❌ Bad Practice → Global file handle**

```py
f = open("data.txt", "r", encoding="utf-8")

def read_first_line():
    return f.readline()

def read_second_line():
    return f.readline()

# somewhere:
print(read_first_line())
print(read_second_line())
f.close()
```

**Why is this bad?**

*   Functions depend on *global state* → harder to test.
*   If someone forgets to close or changes the state of `f` → side effects.
*   Violates good programming style (functions should be as clear and predictable as possible).

***

**✅ Better Practice → Pass the filename or content as a parameter**

```py
from pathlib import Path

def read_first_two_lines(path: Path) -> tuple[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline().rstrip("\n")
        second = f.readline().rstrip("\n")
    return first, second

path = Path("data.txt")
line1, line2 = read_first_two_lines(path)
print(line1, line2)
```

***

## 8️⃣ Race Condition: `if exists` + `open`

You often see online:

```py
import os

if os.path.exists("data.txt"):
    f = open("data.txt", "x")  # "create new file"
else:
    f = open("data.txt", "w")
```

**Why can this be bad?**

*   If at the same moment another process creates or deletes the file:

    *   between the condition and the open call → **race condition**
*   Rarely an issue in small student scripts, but important to understand.

***

**✅ Better Practice → Rely on `open` directly with error handling**

```py
from pathlib import Path

path = Path("data.txt")

try:
    # "x" → create the file if it does not exist
    with open(path, "x", encoding="utf-8") as f:
        f.write("Initial content\n")
except FileExistsError:
    # file already exists
    with open(path, "a", encoding="utf-8") as f:
        f.write("Appended line\n")
```

***

## 🎯 Summary → What to “smell” as wrong?

When browsing code examples online, alarm bells should ring if you see:

*   ❌ File is opened with `open()` but `close()` is missing and `with` is not used.
*   ❌ `w` mode is used “just to be safe” without considering it clears the file.
*   ❌ `eval()` is used on file contents.
*   ❌ All data is read into memory at once, even though it could be processed line by line.
*   ❌ Hard-coded paths that work only in a single environment.
*   ❌ Global file handles passed around between functions.
*   ❌ All-swallowing `except:` blocks without specificity.

***

# 🗂️ Alternative Ways to Manage Data Beyond Files

Files are a good solution for small and simple needs, but when data grows, becomes complex, or requires more efficient queries, other solutions are needed. Here are the main categories:

***

## 1️⃣ Relational Databases (SQL Databases)

**Examples:** PostgreSQL, MySQL, MariaDB, SQLite  
**Use Case:** Structured data with clear tables, columns, keys, and relationships.

**Strengths:**

*   🔍 Powerful queries (SQL language)
*   🔐 Security and user permissions
*   🔁 Transactions → data integrity
*   📊 Suitable for complex relational models

**Where used?**  
Web applications, financial systems, booking systems, student projects.

***

## 2️⃣ NoSQL Databases

**Examples:** MongoDB (document store), Redis (key–value), Cassandra (scalable clusters)

**Strengths:**

*   📈 Highly scalable for large datasets
*   🧩 Flexible structure (no predefined schema required)
*   ⚡ Fast key-value lookups

**Where used?**  
IoT data, logs, real-time applications, massive data streams.

***

## 3️⃣ Cloud-Based Data Services

**Examples:** Firebase, AWS DynamoDB, Azure Cosmos DB

**Strengths:**

*   🌐 Data automatically available from multiple locations
*   🛠️ Built-in APIs and authentication
*   🔧 Scaling without self-maintenance

**Where used?**  
Mobile apps, startup projects, global web traffic.

***

## 4️⃣ Log Services and Time-Series Databases

**Examples:** Elasticsearch, InfluxDB, Kafka

**Strengths:**

*   📈 Great for large event streams
*   ⏱️ Optimized for time-ordered data
*   🔍 Excellent search functionality (Elasticsearch)

**Where used?**  
Monitoring, logging, sensor data, analytics.

***

## 5️⃣ Structured File Formats (Lightweight Solution)

**Examples:** JSON, CSV, YAML, Parquet

**Strengths:**

*   📁 Easy to read and edit
*   🧪 Good for small development-phase data
*   🔄 Compatible with almost all languages

**Where used?**  
Config files, small datasets, data import/export for analytics.

***

## 🎯 When to Use What?

| Need                               | Recommendation           |
| ---------------------------------- | ------------------------ |
| Small project, simple data         | JSON / CSV               |
| Student building first web app     | SQLite → PostgreSQL      |
| Mobile app or real-time chat       | Firebase / Redis         |
| Large system, many users           | PostgreSQL / MySQL       |
| Analytical data, large log volumes | Elasticsearch / InfluxDB |
| Global data traffic                | DynamoDB / Cosmos DB     |

***

## 🧠 Summary

A file is just **one way** to store data. When data size, complexity, or application requirements grow, an OS-level file is no longer enough → you need a data service that provides:

*   better queries
*   data integrity
*   transactions
*   multi-user support
*   scalability
*   security
*   backups