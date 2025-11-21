from datetime import datetime
from lib.enrollment import Student, Course, Enrollment

def test_course_count():
    Enrollment.all.clear()
    student = Student("Alice")
    course1 = Course("Math")
    course2 = Course("Science")
    
    student.enroll(course1)
    student.enroll(course2)
    
    assert student.course_count() == 2
    print("✓ test_course_count passed")

def test_aggregate_average_grade():
    Enrollment.all.clear()
    student = Student("Bob")
    course1 = Course("Math")
    course2 = Course("Science")
    
    enrollment1 = Enrollment(student, course1)
    enrollment2 = Enrollment(student, course2)
    
    student._grades[enrollment1] = 85
    student._grades[enrollment2] = 95
    
    assert student.aggregate_average_grade() == 90
    print("✓ test_aggregate_average_grade passed")

def test_aggregate_average_grade_empty():
    Enrollment.all.clear()
    student = Student("Charlie")
    assert student.aggregate_average_grade() == 0
    print("✓ test_aggregate_average_grade_empty passed")

def test_aggregate_enrollments_per_day():
    Enrollment.all.clear()
    student1 = Student("Dave")
    student2 = Student("Eve")
    course = Course("History")
    
    enrollment1 = Enrollment(student1, course)
    enrollment2 = Enrollment(student2, course)
    
    result = Enrollment.aggregate_enrollments_per_day()
    today = datetime.now().date()
    
    assert result[today] == 2
    print("✓ test_aggregate_enrollments_per_day passed")

if __name__ == "__main__":
    test_course_count()
    test_aggregate_average_grade()
    test_aggregate_average_grade_empty()
    test_aggregate_enrollments_per_day()
    print("All tests passed!")