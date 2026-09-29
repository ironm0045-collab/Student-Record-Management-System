# Problem Statement: Student Record Management System

## Background
Managing student data in colleges and universities is often prone to clerical errors when handled manually through loose spreadsheets or handwritten logs. In particular, computing subject aggregates, percentage conversions, and applying institutional pass/fail cutoffs on large batches can easily result in mistakes.

To solve this, this project implements a console-based student record application written in Python. It provides a lightweight, local database to store student personal details and compute academic standings without relying on external database servers.

---

## Objectives & Core Requirements

1. **Student Registration:** Store essential student attributes including ID, full name, age, hostel status, state, degree program, and semester.
2. **Automated Marks Evaluation:** Take subject scores (Math, Physics, Computer Science), compute the total and percentage, and automatically determine whether a student has passed based on both subject-level minimums (>= 40) and aggregate percentage (>= 40%).
3. **Record Lookup & Updates:** Allow instructors or staff to look up students by their ID, review complete scorecards, and update marks if a student appears for re-evaluation.
4. **Summary Listing:** Output formatted overviews of all enrolled students directly in the terminal.
5. **Independent Testing:** Provide a self-contained test script to verify that pass/fail thresholds and percentage rounding calculate accurately.

---

## Design Boundaries

- **Interface:** Terminal-based command-line interface (CLI).
- **Data Persistence:** In-memory dictionary storage suited for lab demonstration and fast local lookups.
- **Audience:** Lab evaluators, faculty advisors, and departmental coordinators managing batch evaluation.