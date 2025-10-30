import json
from models.student import Student
from services.student_service import StudentService

class StudentInformationSystem:
    def __init__(self):
        with open("../config.json") as config_file:
            config = json.load(config_file)
        self.service = StudentService(config["data_file"], config["log_file"])

    def display_menu(self):
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

    def add_student(self):
        try:
            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            course = input("Enter Course: ")
            student = Student(student_id, name, email, course)
            self.service.add_student(student)
            print("✅ Student added successfully!")
        except Exception as e:
            print("❌ Error adding student:", e)

    def view_students(self):
        students = self.service.get_all_students()
        if not students:
            print("No students found.")
            return
        print("\n--- All Students ---")
        for s in students:
            print(f"{s['student_id']} | {s['name']} | {s['email']} | {s['course']}")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        name = input("New Name: ")
        email = input("New Email: ")
        course = input("New Course: ")
        updated = self.service.update_student(student_id, {
            "name": name,
            "email": email,
            "course": course
        })
        print("✅ Updated successfully!" if updated else "❌ Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        deleted = self.service.delete_student(student_id)
        print("✅ Deleted successfully!" if deleted else "❌ Student not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()
