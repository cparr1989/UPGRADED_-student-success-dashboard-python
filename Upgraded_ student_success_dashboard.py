courses = {}

def add_course():
    course = input("Course name: ")
    courses[course] = {
        "hours": 0,
        "completed": 0,
        "missing": 0,
        "scores": [],
        "deadlines": [],
        "streak": 0
    }
    print("Course added.")

def add_study_session():
    course = input("Course name: ")

    if course not in courses:
        print("Course not found.")
        return

    hours = float(input("Hours studied: "))
    completed = int(input("Assignments completed: "))
    missing = int(input("Assignments missing: "))
    score = float(input("Quiz/Test score: "))
    deadline = input("Upcoming deadline: ")
    studied_today = input("Did you study today? yes/no: ").lower()

    courses[course]["hours"] += hours
    courses[course]["completed"] += completed
    courses[course]["missing"] += missing
    courses[course]["scores"].append(score)
    courses[course]["deadlines"].append(deadline)

    if studied_today == "yes":
        courses[course]["streak"] += 1
    else:
        courses[course]["streak"] = 0

    print("Study session saved.")

def calculate_gpa(avg):
    if avg >= 90:
        return 4.0
    elif avg >= 80:
        return 3.0
    elif avg >= 70:
        return 2.0
    elif avg >= 60:
        return 1.0
    else:
        return 0.0

def view_dashboard():
    print("\nStudent Success Dashboard")
    print("-------------------------")

    for course, data in courses.items():
        avg = sum(data["scores"]) / len(data["scores"]) if data["scores"] else 0
        total_assignments = data["completed"] + data["missing"]
        completion_rate = (data["completed"] / total_assignments) * 100 if total_assignments > 0 else 0
        gpa = calculate_gpa(avg)

        print(f"\nCourse: {course}")
        print(f"Hours Studied: {data['hours']}")
        print(f"Assignments Completed: {data['completed']}")
        print(f"Assignments Missing: {data['missing']}")
        print(f"Completion Rate: {completion_rate:.2f}%")
        print(f"Average Score: {avg:.2f}%")
        print(f"Estimated GPA: {gpa}")
        print(f"Study Streak: {data['streak']} days")

        print("Deadlines:")
        for deadline in data["deadlines"]:
            print("-", deadline)

        print("\nChart:")
        print("#" * int(avg / 5))

def view_summary():
    total_hours = sum(data["hours"] for data in courses.values())
    total_missing = sum(data["missing"] for data in courses.values())

    print("\nOverall Summary")
    print("---------------")
    print(f"Total Courses: {len(courses)}")
    print(f"Total Hours Studied: {total_hours}")
    print(f"Total Missing Assignments: {total_missing}")

    if total_missing == 0:
        print("Status: On Track")
    elif total_missing <= 2:
        print("Status: Needs Attention")
    else:
        print("Status: High Priority")

def main():
    while True:
        print("\nStudent Success Dashboard")
        print("1. Add Course")
        print("2. Add Study Session")
        print("3. View Dashboard")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            add_study_session()
        elif choice == "3":
            view_dashboard()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
