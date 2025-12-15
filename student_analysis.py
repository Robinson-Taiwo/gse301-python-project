# ============================================
# STUDENT ACADEMIC PERFORMANCE ANALYSIS SYSTEM
# ============================================

#  student records (list of dictionaries) 
students = [
    {
        "name": "Rasheed Fatia",
        "matric_number": "23/60AC389",
        "age": 21,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["ELE567", "Data Science", "Statistics"],
        "outstanding_courses": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric_number": "23/70JC093",
        "age": 20,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Maths"],
        "outstanding_courses": 0
    },
    {
        "name": "Moses Oyedele",
        "matric_number": "23/60AC011",
        "age": 22,
        "cgpa": 2.95,
        "is_active": False,
        "courses": ["AI", "Database"],
        "outstanding_courses": 1
    },
    {
        "name": "Timi Abidoye",
        "matric_number": "23/60AC200",
        "age": 19,
        "cgpa": 4.01,
        "is_active": True,
        "courses": ["Python", "DSA"],
        "outstanding_courses": 0
    },
    {
        "name": "Nimah Nina",
        "matric_number": "23/60AC552",
        "age": 18,
        "cgpa": 3.90,
        "is_active": True,
        "courses": ["Maths", "Physics"],
        "outstanding_courses": 0
    }
]

#  Department info stored as a tuple 
department_info = ("Religion Department", "Faculty of Technology", 2025)

#   courses offered 
courses_offered = set()
for student in students:
    for course in student["courses"]:
        courses_offered.add(course)

#  Demonstrating list slicing 
sample_scores = [45, 70, 82, 66, 78, 55, 90, 88, 60, 73]
top_three_scores = sample_scores[:3]
last_five_scores = sample_scores[-5:]
alternate_scores = sample_scores[::2]


#  Grade calculation using IF / ELIF / ELSE 
def calculate_grade(score):
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    # Match case for feedback
    match grade:
        case "A":
            print("Excellent performance")
        case "B":
            print("Very good performance")
        case "C":
            print("Good performance")
        case "D":
            print("Fair performance")
        case "E":
            print("Poor performance")
        case "F":
            print("Failed")

    return grade


#  Adding a new student with type casting and validation 
def add_new_student():
    print("Add New Student")

    name = input("Enter name: ")
    matric_number = input("Enter matric number: ")

    try:
        age = int(input("Enter age: "))
        cgpa = float(input("Enter CGPA: "))

        if age < 16 or age > 40:
            print("Invalid age entered")
            return

        if cgpa < 0.0 or cgpa > 5.0:
            print("Invalid CGPA entered")
            return

    except ValueError:
        print("Invalid input detected")
        return

    is_active = input("Is the student active (yes/no): ").lower() == "yes"
    courses = input("Enter courses (comma separated): ").split(",")

    students.append({
        "name": name,
        "matric_number": matric_number,
        "age": age,
        "cgpa": cgpa,
        "is_active": is_active,
        "courses": [course.strip() for course in courses],
        "outstanding_courses": 0
    })

    print("Student record added successfully.")


#  Graduation eligibility check using logical operators 
def check_graduation_eligibility(student):
    return (
        student["cgpa"] >= 2.5 and
        student["outstanding_courses"] == 0 and
        student["is_active"]
    )


#  Finding the top performing student 
def find_top_performer():
    top_student = students[0]
    for student in students:
        if student["cgpa"] > top_student["cgpa"]:
            top_student = student
    return top_student


#  Main menu system using MATCH CASE 
def run_menu():
    print("============================================")
    print("     Student Academic Performance System")
    print("============================================")
    print("Loading student records...")
    print(f"{len(students)} student profiles loaded successfully.")

    while True:
        print("--------------------------------------------")
        print("Menu Options")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Exit")
        print("--------------------------------------------")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("List of Students:")
                for index, student in enumerate(students, start=1):
                    print(f"{index}. {student['name']}")

            case "2":
                add_new_student()

            case "3":
                name = input("Enter student name: ")
                found = False

                for student in students:
                    if student["name"] == name:
                        found = True
                        print("Checking eligibility...")
                        print(f"Matric Number: {student['matric_number']}")
                        print(f"CGPA: {student['cgpa']}")
                        print(f"Outstanding Courses: {student['outstanding_courses']}")
                        print(f"Active Status: {student['is_active']}")

                        if check_graduation_eligibility(student):
                            print(f"{name} is eligible for graduation.")
                        else:
                            print(f"{name} is not eligible for graduation.")
                        break

                if not found:
                    print("Student not found.")

            case "4":
                top = find_top_performer()
                print("Top Performer:")
                print(f"Name: {top['name']}")
                print(f"Matric: {top['matric_number']}")
                print(f"CGPA: {top['cgpa']}")
                print(f"Courses: {top['courses']}")

            case "5":
                print("Exiting the system...")
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")


#  Program entry point 
run_menu()
