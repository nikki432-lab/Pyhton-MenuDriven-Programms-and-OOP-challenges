#Step1. Defining the student class(Encapsulating marks within the student object)

class Student:
    def __init__(self, name , roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {} #.__ private attribute encapsulation

    def add_marks(self, subject, score):
        self.__marks[subject] = score

    def get_marks(self):
        return self.__marks

#Step2. Abstract report card class(Defining a abstract method blueprint for grading systems)

from abc import ABC, abstractmethod

class  Reportcard(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass


#Step3. Implement grading logic(Inheritance and polymorphism) apply a grade calculation and pass/fail criteria

class Finalreportcard(Reportcard):
    def __init__(self, student):
        self.student = student

    def calculate_grade(self):
        marks = self.student.get_marks()
        average_score = sum(marks.values()) / len(marks) if marks else 0

        if average_score >= 80:
            return "A"
        elif average_score >= 60:
            return "B"
        elif average_score >= 50:
            return "C"
        elif average_score >= 35:
            return "D"
        else:
            return "F"

    def generate_report(self):
        grade = self.calculate_grade()
        overall_status = "Pass" if grade != "F" else "Fail"
        marks = self.student.get_marks()
        
        report = f"\nStudent Report Card\n"
        report += f"Name: {self.student.name}\nRoll.No: {self.student.roll_no}\n"
        report += f"\nSubjects and Marks:\n"

        for subject, score in marks.items():
            subject_status = "Pass" if score >= 35 else "Fail"
            report += f"{subject}: {score} ({subject_status})\n"

        report += f"\nOverall Grade: {grade}\nOverall Result: {overall_status}\n"
        return report


#Step4. Creating the Menu-Driven-Interface(Interactive command line interface(CLI) based system for user input)

def main():
    students = {}

    while True:
        print("\nStudent Report Card System.")
        print("1. Add student and marks.")
        print("2. Generate Report Card.\n3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            student = Student(name, roll_no)

            # Fix inside option '1' (Adding Student & Marks)
            while True:
                subject = input("Enter subject name (or type 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                score = float(input(f"Enter marks for {subject}: "))
                student.add_marks(subject, score)  # Correctly add marks to the student
                students[roll_no] = student  # Store the student instance in dictionary

        
        elif choice == '2':
            roll_no = input("Enter roll number: ")
            if roll_no in students:
                report_card = Finalreportcard(students[roll_no])
                print(report_card.generate_report())
            else:
                print("Student not found.")
        
        elif  choice == '3':
            print("Exiting....")
            break
        else:
            ("Invalid choice. please try again.")

if __name__ == "__main__":
    main()

        


            
