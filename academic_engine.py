def calculate_academic_performance(marks_dict):
    if not marks_dict:
        return 0, 0.0, "N/A"

    total = sum(marks_dict.values())
    percentage = round(total / len(marks_dict), 2)

    # Student must score at least 40 in each subject and 40% aggregate to pass
    has_failed_subject = any(score < 40 for score in marks_dict.values())
    result = "Pass" if (not has_failed_subject and percentage >= 40.0) else "Fail"

    return total, percentage, result


def prompt_marks_input():
    subjects = ["Math", "Physics", "CS"]
    marks = {}

    print("\n--- Enter Subject Marks (Out of 100) ---")
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks for {subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                print("Please enter valid marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numerical score.")

    return marks