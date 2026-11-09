def get_best_students(students: list[dict]) -> list[dict]:
    best_students = []
    best_average_grade = 0
    for student in students:
        grades = student["grades"]
        if grades is None:
            average_grade = 0
        else:
            average_grade = sum(grades) / len(grades)
        if average_grade > best_average_grade:
            best_average_grade = average_grade
            best_students = [student]
        elif average_grade == best_average_grade:
            best_students.append(student)
    return best_students