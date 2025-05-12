# pyfuncs 🐍⚡  

**A collection of reusable Python functions to speed up development.**  

This library provides a set of handy, efficient, and well-tested utility functions for common tasks in Python, including data processing, file operations, math helpers, and more.  

---

## 🔹 Features  

- **File Handling** – Read, write, and manipulate files easily.  
- **Data Processing** – Clean, filter, and transform data quickly.  
- **Math Utilities** – Common calculations and number operations.  
- **String Manipulation** – Formatting, validation, and text processing.  
- **Date & Time Helpers** – Simplify datetime operations.  
- **Web & API Utilities** – HTTP requests, URL parsing, and more.  

---

## 🔹 Installation  

Install via pip (if published to PyPI):  
```bash
pip install pyfuncs
Or clone the repository:

bash
git clone https://github.com/yourusername/pyfuncs.git
cd pyfuncs
pip install -e .
🔹 Quick Start
Example 1: File Operations
python
from pyfuncs.file_utils import read_json, write_csv

data = read_json("data.json")  
write_csv("output.csv", data)  
Example 2: Math Helpers
python
from pyfuncs.math_utils import clamp, factorial

print(clamp(15, 0, 10))  # Output: 10  
print(factorial(5))      # Output: 120  
Example 3: String Formatting
python
from pyfuncs.string_utils import slugify

print(slugify("Hello World!"))  # Output: "hello-world"  
🔹 Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Commit your changes (git commit -m "Add some feature").

Push to the branch (git push origin feature/your-feature).

Open a Pull Request.

🔹 License
This project is licensed under MIT License. See LICENSE for details.

🚀 Happy Coding! Let’s make Python even more powerful.
