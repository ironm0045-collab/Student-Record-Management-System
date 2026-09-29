# Student Record Management System

A Python-based command-line tool designed for managing student profiles and calculating academic performance scores.

---

## Project Overview

This project was built to simplify student data entry and scorecard calculation. It organizes records by Student ID and calculates totals, percentages, and pass/fail results across three core subjects: Mathematics, Physics, and Computer Science.

The code is separated into distinct modules:
- Data storage dictionary
- Academic calculation engine
- Record management operations
- Main command-line interface
- Automated test script

---

## Key Capabilities

- **Direct ID Query:** Enter any student ID directly from the main screen to print their scorecard.
- **New Student Enrollment:** Register student details (Name, Age, Hosteller/Day Scholar, State, Course, Semester) along with subject marks.
- **Automatic Grading & Results:** Evaluates passing status based on achieving at least 40 marks in each individual subject and an overall 40% aggregate.
- **Scorecard Editing:** Update marks for any existing student and have totals and results recomputed instantly.
- **Batch Table Display:** View all enrolled students in a formatted tabular terminal layout.
- **Built-in Verification:** Includes validation tests to test edge cases in calculations.

---

## Technical Details

- **Language:** Python 3.8+
- **Modules Used:** Standard library only (`sys`, `assert`, built-in data types)
- **Dependencies:** None (no third-party pip packages needed)

---

## Project Structure

```text
├── .gitattributes          # Git line-ending normalization settings
├── .gitignore              # Files ignored by Git
├── requirements.txt        # Notes on environment requirements
├── academic_engine.py      # Computes marks, percentages, and pass criteria
├── data_store.py           # In-memory dictionary storing student profiles
├── main.py                 # CLI loop and menu navigation
├── student_manager.py      # Functions for adding, querying, and updating records
├── test_system.py          # Unit assertions for score calculation
├── PROBLEM_STATEMENT.md    # Problem statement and requirements
└── README.md               # Project documentation
```

---

## How to Run

1. Clone or download the repository to your machine.
2. Open a terminal inside the project directory.
3. Start the application:
   ```bash
   python main.py
   ```
4. To run system validation tests:
   ```bash
   python test_system.py
   ```

---

## Author
**Gupta Shourya Manohar**  
B.Tech CSE (Core)  
VIT Bhopal University
