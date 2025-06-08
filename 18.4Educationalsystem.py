class Studentsystem:
    def __init__(self):
        self.student = {}
        
    def add_student(self, student_id, name, age, grade):
        if student_id in self.student:
            print("Student ID already exists. try another ID.")
        else:
            self.student[student_id] = {"name": name, "age": age, "grade": grade}
            print(f"student {name} added Successfully!")

    def display_students(self):
        if not self.student:
            print("No student records available.")
        else:
            print("\nStudent Details:")
            for student_id, details in self.student.items():
                print(f"ID:{student_id}, Name:{details['name']}, Age:{details['age']}, Grade:{details['grade']}")

    def remove_student(self, student_id):
        if student_id in self.student:
            removed_student = self.student.pop(student_id)
            print(f"student {removed_student['name']} Removed sucessfully!")
        else:
            print("Student ID not foiund.")

def main():
    system = Studentsystem()

    while True:
        print("\nEducational system menu: ")
        print("1. Add student")
        print("2. Display student details")
        print("3. Remove student")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("ENter student grade: ")
            system.add_student(student_id, name, age, grade)
        
        elif choice == '2':
            system.display_students()

        elif choice == '3':
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)

        elif choice == '4':
            print( "Thank you for using the educational system. Goodbye!")
            break
        else:
            print("Invalid choice. please select a valid option")

if __name__ == "__main__":
    main()




