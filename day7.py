# ========================================
# 1. Reading and Writing Files
# ========================================

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\nThis is a sample text file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# ========================================
# 2. Working with CSV
# ========================================

import csv

# Writing to a CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    print("\nCSV Content:")
    for row in reader:
        print(row)

# ========================================
# 3. Working with JSON
# ========================================

import json

# Writing to a JSON file
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling"]
}

with open("example.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading from a JSON file
with open("example.json", "r") as file:
    content = json.load(file)
    print("\nJSON Content:")
    print(content)

# ========================================
# 4. Error Handling: Exceptions and Try/Except
# ========================================

# Example 1: Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"\nError: {e}")
else:
    print("Result:", result)
finally:
    print("This will always execute.")

# Example 2: Handling file not found error
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"\nError: {e}")
else:
    print("File Content:", content)
finally:
    print("Execution complete.")