from student_manager import (
    display_record,
    search_student,
    add_student,
    update_marks,
    display_all_students
)
from data_store import students

def main_menu():
    while True:
        print("\n--- MANAGEMENT MENU ---")
        print("1. Search Student by ID")
        print("2. Add New Student Profile")
        print("3. Update Student Marks")
        print("4. View All Students")
        print("5. Return to Main Screen")

        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            search_student()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 5.")


def main():
    while True:
        print("\n==========================================")
        print("     STUDENT RECORD MANAGEMENT SYSTEM     ")
        print("==========================================")
        print("Commands: Enter a [Student ID] | 'NEW' | 'MENU' | 'EXIT'")

        command = input(">> ").strip().upper()

        if not command:
            continue
        elif command == "EXIT":
            print("Exiting system. Have a great day!")
            break
        elif command == "MENU":
            main_menu()
        elif command == "NEW":
            add_student()
        elif command in students:
            display_record(command)
        else:
            print(f"'{command}' is neither a known Student ID nor a valid command.")
            print("Type 'MENU' to view all operations, or enter an ID like 'VIT001'.")


if __name__ == "__main__":
    main()