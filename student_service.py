import json
import os
from datetime import datetime

class StudentService:
    def __init__(self, data_file, log_file):
        self.data_file = data_file
        self.log_file = log_file
        self.students = self._load_students()

    def _log(self, message):
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now()}] {message}\n")

    def _load_students(self):
        try:
            if not os.path.exists(self.data_file):
                return []
            with open(self.data_file, "r") as file:
                return json.load(file)
        except Exception as e:
            self._log(f"Error loading students: {e}")
            return []

    def _save_students(self):
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.students, file, indent=4)
        except Exception as e:
            self._log(f"Error saving students: {e}")

    def add_student(self, student):
        self.students.append(student.to_dict())
        self._save_students()
        self._log(f"Added student: {student.name}")

    def get_all_students(self):
        return self.students

    def find_student(self, student_id):
        return next((s for s in self.students if s["student_id"] == student_id), None)

    def update_student(self, student_id, updated_data):
        student = self.find_student(student_id)
        if student:
            student.update(updated_data)
            self._save_students()
            self._log(f"Updated student: {student_id}")
            return True
        return False

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self._save_students()
            self._log(f"Deleted student: {student_id}")
            return True
        return False
