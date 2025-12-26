# Embarking on Your Codewars Journey

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Codewars](https://img.shields.io/badge/codewars-kata-red.svg)

A collection of Codewars kata solutions completed as part of the Coding Temple Software Engineering Bootcamp. This repository demonstrates fundamental Python programming concepts through practical problem-solving exercises.

## 📋 Table of Contents

- [About](#about)
- [Kata Solutions](#kata-solutions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Author](#author)

## 🎯 About

This repository contains solutions to introductory Codewars challenges, focusing on building strong foundational skills in Python programming. Each solution emphasizes clean, readable code and best practices.

## 🧩 Kata Solutions

### Task 1: Even or Odd
**Difficulty:** 8 kyu  
**Description:** Determines whether a given integer is even or odd.

```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

**Concepts:** Conditionals, modulo operator, basic logic

---

### Task 2: Convert a Number to a String
**Difficulty:** 8 kyu  
**Description:** Converts a numeric value into its string representation.

```python
def number_to_string(num):
    return str(num)
```

**Concepts:** Type conversion, built-in functions

---

### Task 3: Remove String Spaces
**Difficulty:** 8 kyu  
**Description:** Removes all whitespace characters from a string.

```python
def no_space(x):
    return("".join(x.strip().split()))
```

**Concepts:** String manipulation, method chaining

---

### Task 4: Vowel Count
**Difficulty:** 7 kyu  
**Description:** Counts the number of vowels (a, e, i, o, u) in a given string.

```python
def get_count(sentence):
    vowel_repo = "aeiou"
    vowel_count = 0
    for character in sentence:
        if character in vowel_repo:
            vowel_count += 1
        else:
            continue
    return vowel_count
```

**Concepts:** Loops, iteration, string membership testing, counters

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of Python syntax

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CT_Embarking_on_your_Codewars_Journey.git
   ```

2. Navigate to the project directory:
   ```bash
   cd CT_Embarking_on_your_Codewars_Journey
   ```

## 💻 Usage

Run the Python file to test the functions:

```bash
python assignment.py
```

You can also import individual functions in a Python interpreter:

```python
from assignment import even_or_odd, number_to_string, no_space, get_count

# Test examples
print(even_or_odd(42))           # Output: "Even"
print(number_to_string(123))     # Output: "123"
print(no_space("Hello World"))   # Output: "HelloWorld"
print(get_count("hello world"))  # Output: 3
```

## 📚 Learning Objectives

Through these kata solutions, this project demonstrates:

- ✅ Fundamental Python syntax and data types
- ✅ Control flow structures (conditionals, loops)
- ✅ String manipulation techniques
- ✅ Type conversion and built-in functions
- ✅ Problem-solving and algorithmic thinking
- ✅ Code readability and organization

## 👤 Author

**Matthew Arney**

- Program: Software Engineering Bootcamp
- Focus: Full-Stack Development

---

## 📝 Notes

This repository is part of the Coding Temple curriculum and serves as an introduction to competitive programming and code challenges. Each solution prioritizes clarity and demonstrates core Python concepts essential for software development.

## 🔗 Resources

- [Codewars](https://www.codewars.com/) - Practice coding challenges
- [Python Documentation](https://docs.python.org/3/) - Official Python docs
- [Coding Temple](https://codingtemple.com/) - Software Engineering Bootcamp

---

*Last Updated: December 2025*