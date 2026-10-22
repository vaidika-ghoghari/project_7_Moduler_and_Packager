# Modular & Packager – Multi-Utility Toolkit

A modular, menu-driven Python application that brings together essential utilities for date and time management, mathematical calculations, random data generation, UUID creation, file handling, and module exploration in one organized toolkit.

The project demonstrates how Python modules and packages can be used to build reusable, maintainable, and well-structured applications.

## 📌 Project Overview

The **Multi-Utility Toolkit** is a command-line application developed using Python 3 and its standard libraries. It organizes different utility functions into dedicated modules within a custom `Utilities` package, making the code easier to understand, maintain, and extend.

Users can interact with the application through a main menu, select the required operation, enter the necessary inputs, and view the results directly in the terminal.

This project focuses on practical implementation of Python modular programming, package management, exception handling, built-in libraries, and file operations.

## ✨ Key Features

### 1. Date and Time Utilities
- Display the current date and time.
- Calculate the difference between two dates.
- Format dates using custom formatting patterns.
- Measure elapsed time with a stopwatch.
- Run a countdown timer.

### 2. Mathematical Utilities
- Calculate the factorial of a non-negative integer.
- Calculate compound interest.
- Perform trigonometric calculations, including sine, cosine, and tangent.
- Calculate the areas of circles, rectangles, and triangles.

### 3. Random Data Generation
- Generate random numbers within a specified range.
- Generate lists of random integers.
- Create random passwords using letters and digits.
- Generate numeric one-time passwords (OTPs).

### 4. UUID Generation
- Generate universally unique identifiers (UUIDs) using Python's built-in `uuid` module.

### 5. File Management
- Create new files.
- Write content to files.
- Read existing file contents.
- Append new content to existing files.
- Handle common file-related errors.

### 6. Module Exploration
- Explore module attributes and functions using Python's `dir()` function.
- Inspect built-in Python modules.
- Explore custom modules from the `Utilities` package.

## 🗂️ Project Structure

```text
Modular-Packager/
│
├── main.py
│
└── Utilities/
    ├── __init__.py
    ├── datetime_utils.py
    ├── math_utils.py
    ├── random_utils.py
    ├── uuid_utils.py
    └── file_utils.py
```

### Architecture

- **`main.py`** — Provides the main menu, handles user interaction, and connects the utility modules.
- **`Utilities/__init__.py`** — Initializes the custom Python package.
- **`datetime_utils.py`** — Contains date and time-related functions.
- **`math_utils.py`** — Contains mathematical calculations and geometry operations.
- **`random_utils.py`** — Handles random number, password, and OTP generation.
- **`uuid_utils.py`** — Provides UUID generation functionality.
- **`file_utils.py`** — Handles basic file creation, reading, writing, and appending operations.

Each module has a specific responsibility, helping keep the application organized and reusable.

## 🛠️ Technologies and Concepts

**Language:** Python 3

**Standard Libraries:**
- `datetime` — Date and time operations.
- `time` — Stopwatch and countdown functionality.
- `math` — Mathematical and trigonometric calculations.
- `random` — Random number and data generation.
- `string` — Character sets for password generation.
- `uuid` — Unique identifier generation.
- `os` — Operating system and file-related utilities, where required.

**Core Concepts:**
- Python modules and packages.
- Functions and code reusability.
- Importing custom and built-in modules.
- Menu-driven program design.
- Loops and conditional statements.
- Exception handling and input validation.
- File handling.
- Module introspection using `dir()`.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your system.
- A terminal or command prompt.
- A code editor such as Visual Studio Code or Python IDLE (optional).

Verify your Python installation:

```bash
python --version
```

### Download the Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Alternatively, download the repository as a ZIP file and extract it.

Navigate to the project directory:

```bash
cd Modular-Packager
```

### Run the Application

Execute the following command:

```bash
python main.py
```

On systems where Python 3 uses a separate command, run:

```bash
python3 main.py
```

No third-party dependencies are required because the project uses Python's standard library.

## ▶️ How to Use

1. Start the application by running `main.py`.
2. View the available options in the main menu.
3. Select the utility you want to use.
4. Enter the requested values when prompted.
5. Review the result displayed in the terminal.
6. Return to the main menu to perform another operation.
7. Select the exit option to close the application.

## 📚 Learning Outcomes

Through this project, I practiced:

- Designing a modular Python application.
- Creating and importing custom modules and packages.
- Organizing related functions into separate files.
- Using Python's standard libraries for practical tasks.
- Building interactive, menu-driven applications.
- Handling invalid input and runtime errors.
- Performing basic file operations.
- Exploring module attributes and functions using `dir()`.
- Improving code readability, reusability, and maintainability.

## 🚀 Future Enhancements

Potential improvements include:

- Expanding the collection of mathematical and date-time utilities.
- Strengthening input validation and exception handling.
- Adding automated unit tests for individual modules.
- Introducing a graphical user interface (GUI).
- Enhancing file management with additional operations.
- Improving the overall user experience and menu navigation.

## 👨‍💻 Project Information

| Detail | Description |
|---|---|
| Project Name | Modular & Packager – Multi-Utility Toolkit |
| Programming Language | Python 3 |
| Application Type | Command-Line Application |
| Architecture | Modular, Package-Based |
| Dependencies | Python Standard Library |
| Purpose | Educational and Practical Learning |

## 🔗 Connect With Me

- **LinkedIn:** [Visit My LinkedIn Profile](https://www.linkedin.com/in/vaidika-ghoghari-2196a534a)
- **Email:** [Contact Me](mailto:ghogharivaidika@gmail.com)
- **Project Explanation Video:** [Watch the Project Explanation Video](https://drive.google.com/file/d/1q7HZ22hwbhWeB_zpb-U-MYZaq5-TnNYm/view?usp=sharing)

Feel free to connect with me, share feedback, or discuss this project.

---

**Developed as a practical Python project to strengthen modular programming, package organization, exception handling, and file management skills.**
