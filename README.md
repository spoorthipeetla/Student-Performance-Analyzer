# Student Performance Analyzer

A robust, terminal-based Python application that tracks, analyzes, and exports student academic performance.

This project was built to demonstrate core Python fundamentals, including dynamic data structures (lists and dictionaries), control flow, error handling, and persistent data storage (File I/O).

## Features

* **Dynamic Data Entry:** Allows users to input an unlimited number of students and their respective subject marks.
* **Crash-Proof Input:** Utilizes `try/except` blocks to catch user input errors (e.g., typing text instead of numbers) without crashing the program.
* **Automated Grading:** Calculates individual averages and automatically assigns letter grades (A, B, C, D, Fail) and qualitative feedback.
* **Pass/Fail Logic:** Scans individual subject marks to determine absolute Pass/Fail status (a score below 35 in *any* subject results in an automatic fail).
* **Class Analytics:** Identifies the class topper, total passing students, total failing students, and the overall class average.
* **Data Export (File I/O):** * Generates a detailed `student_database.csv` containing the full class roster and individual stats.
  * Generates a quick-glance `class_summary.txt` report with high-level class analytics.

## How to Run

1. Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.
2. Clone this repository or download the script.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the script.
5. Run the following command:
   ```bash
   python main.py