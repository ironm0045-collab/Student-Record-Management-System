from data_store import students
from academic_engine import calculate_academic_performance, prompt_marks_input

def display_record(student_id):
    student_id = student_id.strip().upper()
    if student_id not in students:
        print(f"\n[!] Student record for ID '{student_id}' was not found.")
        return

    s = students[student_id]
    print("\n" + "=" * 40)
    print(f"       STUDENT PROFILE: {student_id}")
    print("=" * 40)
    print(f" Name        : {s['Name']}")
    print(f" Age         : {s['Age']}")
    print(f" Residence   : {s['Status']}")
    print(f" Home State  : {s['State']}")
    print(f" Program     : {s['Course']}")
    print(f" Semester    : {s['Semester']}")
    print("-" * 40)

    marks = s.get("Marks", {})
    if marks:
        formatted_marks = ", ".join([f"{k}: {v}" for k, v in marks.items()])
        print(f" Marks       : {formatted_marks}")
        print(f" Total       : {s.get('Total', 0)} / {len(marks) * 100}")
        print(f" Percentage  : {s.get('Percentage', 0.0)}%")
        print(f" Result      : {s.get('Result', 'N/A')}")
    print("=" * 40)


def search_student():
    sid = input("\nEnter Student ID to search: ").strip()
    display_record(sid)


def add_student():
    print("\n--- Register New Student ---")
    sid = input("Enter Student ID: ").strip().upper()

    if sid in students:
        print(f"Error: A student with ID '{sid}' already exists in the system.")
        return

    name = input("Enter full name: ").strip()
    
    while True:
        try:
            age = int(input("Enter age: "))
            if 15 <= age <= 100:
                break
            print("Please enter a realistic student age (15-100).")
        except ValueError:
            print("Invalid input. Age must be an integer.")

    status = input("Status (Hosteller / Day Scholar): ").strip()
    state = input("Home State: ").strip().title()
    course = input("Degree / Course: ").strip()
    
    while True:
        try:
            semester = int(input("Current Semester: "))
            if 1 <= semester <= 12:
                break
            print("Semester must be between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid semester number.")

    marks = prompt_marks_input()
    total, percentage, result = calculate_academic_performance(marks)

    students[sid] = {
        "Name": name,
        "Age": age,
        "Status": status,
        "State": state,
        "Course": course,
        "Semester": semester,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Result": result
    }

    print(f"\nStudent '{name}' ({sid}) added successfully.")


def update_marks():
    sid = input("\nEnter Student ID to update marks: ").strip().upper()
    if sid not in students:
        print(f"Student '{sid}' not found.")
        return

    print(f"Entering new marks for {students[sid]['Name']} ({sid})...")
    marks = prompt_marks_input()
    total, percentage, result = calculate_academic_performance(marks)

    students[sid]["Marks"] = marks
    students[sid]["Total"] = total
    students[sid]["Percentage"] = percentage
    students[sid]["Result"] = result

    print(f"Academic records updated for {students[sid]['Name']}.")


def display_all_students():
    if not students:
        print("\nNo student records available in the database.")
        return

    print("\n" + "-" * 78)
    print(f"{'ID':<10} | {'Name':<22} | {'Course':<18} | {'%':<8} | {'Result':<8}")
    print("-" * 78)
    for sid, s in students.items():
        pct_str = f"{s.get('Percentage', 0.0):.1f}%"
        print(f"{sid:<10} | {s['Name']:<22} | {s['Course']:<18} | {pct_str:<8} | {s.get('Result', 'N/A'):<8}")
    print("-" * 78)
    print(f"Total enrolled students: {len(students)}\n")