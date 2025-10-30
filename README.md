# Student Management System (CLI)

## Features
- Create, Read, Update, Delete students
- JSON data persistence
- Logging
- Search by name and export to CSV
- Unit tests

## Run
1. Open terminal in project root
2. cd src
3. python main.py

## Tests
pip install pytest
python -m pytest tests/test_student_service.py

## Git workflow recommendation
- `main` branch protected
- create feature branches: `feature/add-student`, `feature/export-csv`
- commit messages: `feat(student): add student service persistence`, `fix(main): handle missing config`
