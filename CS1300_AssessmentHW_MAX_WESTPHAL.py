#Getting input from the user
# Validating the input
#Storing the scores
#Calculating the average, grade, and standing
#Printing and formatting the final result




def main():
    name, scores = get_student_info()
    avg = calculate_average(scores)
    grade = determine_grade(avg)
    standing = determine_standing(avg)
    display_report(name, scores, avg, grade, standing)

def get_student_info():
    pass

def calculate_average(scores):
    pass

def determine_grade(avg):
    pass

def determine_standing(avg):
    pass

def display_report(name, scores, avg, grade, standing):
    pass





def main():
    name, scores = get_student_info()
    avg = calculate_average(scores)
    grade = determine_grade(avg)
    standing = determine_standing(avg)
    display_report(name, scores, avg, grade, standing)

def get_student_info():
    """Return the student's name and a list of validated scores."""
    pass
def calculate_average(scores):
    """Return the numeric average of the exam scores."""
    pass
def determine_grade(avg):
    """Return the letter grade based on the average."""
    pass
def determine_standing(avg):
    """Return the academic standing based on the average."""
    pass
def display_report(name, scores, avg, grade, standing):
    """Print the formatted student report."""
    pass






def get_student_info():
    name = input("Student name: ")
    scores = []
    for i in range(3):
        score = get_valid_score(i + 1)
        scores.append(score)
    return name, scores

def get_valid_score(exam_number):
    """Ask for a score and validate it."""
    while True:
        s = int(input(f"Exam {exam_number} score: "))
        if 0 <= s <= 100:
            return s
        print("Invalid score! Must be between 0 and 100.")
        
        
        
        

def calculate_average(scores):
    return sum(scores) / len(scores)

def determine_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def determine_standing(avg):
    if avg >= 90: return "Dean's List"
    elif avg >= 70: return "Good Standing"
    elif avg >= 60: return "Academic Probation"
    else: return "Academic Warning"
def display_report(name, scores, avg, grade, standing):
    border()
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    border()

def border():
    print("=" * 30)
    
    
    
    
    
    
    
    
def get_validated_input(prompt):
    """Return an integer between 0 and 100, retrying on bad input."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def get_student_info():
    name = input("Student name: ")
    scores = []
    for i in range(3):
        score = get_validated_input(f"Exam {i+1}: ")
        scores.append(score)
    return name, scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def determine_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def determine_standing(avg):
    if avg >= 90: return "Dean's List"
    elif avg >= 70: return "Good Standing"
    elif avg >= 60: return "Academic Probation"
    else: return "Academic Warning"

def border():
    print("=" * 30)

def display_report(name, scores, avg, grade, standing):
    border()
    print("STUDENT GRADE REPORT")
    border()
    print()
    print(f"Student: {name}")
    print(f"Exam 1: {scores[0]}")
    print(f"Exam 2: {scores[1]}")
    print(f"Exam 3: {scores[2]}")
    print("-" * 30)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    border()

def main():
    name, scores = get_student_info()
    avg = calculate_average(scores)
    grade = determine_grade(avg)
    standing = determine_standing(avg)
    display_report(name, scores, avg, grade, standing)
    
    
    
    

def calculate_average(scores):
    """
    Calculate the mean of a list of exam scores.
    Args:
        scores (list[int]): A list of integer exam scores (0–100).
    Returns:
        float: The average of the scores.
    """
    return sum(scores) / len(scores)

def determine_grade(avg):
    """
    Determine the letter grade based on a numeric average.
    Args:
        avg (float): The student's average exam score.
    Returns:
        str: A single letter grade ('A'–'F').
    """
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"
    
    
    
    
    
def test_grade_tracker():
    print("Running tests...")
    scores = [90, 80, 70]
    avg = calculate_average(scores)
    assert avg == 80, "Average calculation failed"
    assert calculate_average([100, 100, 100]) == 100
    assert calculate_average([0, 0, 0]) == 0
    assert determine_grade(95) == "A"
    assert determine_grade(85) == "B"
    assert determine_grade(75) == "C"
    assert determine_grade(65) == "D"
    assert determine_grade(50) == "F"
    assert determine_grade(90) == "A"
    assert determine_grade(89.99) == "B"

    print("All tests passed!")
    
    
    
    
    
    
    
"""
Student Grade Tracker
CS 1300 – Lecture 5 Mini-Project

A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.

Functions:
    get_student_info       – Prompt for and return student name + scores
    get_validated_input    – Helper: retry loop for score entry
    calculate_average      – Compute mean of a scores list
    determine_grade        – Map average to letter grade
    determine_standing     – Map average to academic standing
    border                 – Helper: print a decorative line
    display_report         – Print the formatted grade report
    main                   – Orchestrate the full program
    test_grade_tracker     – Run all unit tests
"""








"""
Student Grade Tracker
CS 1300 – Lecture 5 Mini-Project

A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.
"""

def get_validated_input(prompt):
    """
    Prompt the user for a score and retry until valid.
    Args:
        prompt (str): The text to display when asking for input.
    Returns:
        int: A validated exam score between 0 and 100.
    """
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def border():
    """Print a decorative border line."""
    print("=" * 30)

def get_student_info():
    """
    Collect the student's name and three validated exam scores.

    Returns:
        tuple: (name (str), scores (list[int]))
    """
    name = input("Student name: ")
    scores = []
    for i in range(3):
        score = get_validated_input(f"Exam {i+1}: ")
        scores.append(score)

    return name, scores

def calculate_average(scores):
    """
    Calculate the mean of a list of exam scores.
    Args:
        scores (list[int]): A list of exam scores.
    Returns:
        float: The average score.
    """
    return sum(scores) / len(scores)

def determine_grade(avg):
    """
    Determine the letter grade based on the numeric average.
    Args:
        avg (float): The student's average score.
    Returns:
        str: A letter grade ('A'–'F').
    """
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def determine_standing(avg):
    """
    Determine academic standing based on the numeric average.
    Args:
        avg (float): The student's average score.
    Returns:
        str: The academic standing description.
    """
    if avg >= 90: return "Dean's List"
    elif avg >= 70: return "Good Standing"
    elif avg >= 60: return "Academic Probation"
    else: return "Academic Warning"

def display_report(name, scores, avg, grade, standing):
    """
    Print a formatted student grade report.
    Args:
        name (str): Student name.
        scores (list[int]): List of exam scores.
        avg (float): Average score.
        grade (str): Letter grade.
        standing (str): Academic standing.
    """
    border()
    print("STUDENT GRADE REPORT")
    border()
    print()
    print(f"Student: {name}")
    print(f"Exam 1: {scores[0]}")
    print(f"Exam 2: {scores[1]}")
    print(f"Exam 3: {scores[2]}")
    print("-" * 30)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    border()

def main():
    """
    Orchestrate the full grade-tracking program.
    """
    name, scores = get_student_info()
    avg = calculate_average(scores)
    grade = determine_grade(avg)
    standing = determine_standing(avg)
    display_report(name, scores, avg, grade, standing)

def test_grade_tracker():
    """
    Run unit tests for calculation functions using
    the Arrange-Act-Assert pattern.
    """
    print("Running tests...")

    scores = [90, 80, 70]
    avg = calculate_average(scores)
    assert avg == 80, "Average calculation failed"
    assert calculate_average([100, 100, 100]) == 100
    assert calculate_average([0, 0, 0]) == 0
    assert determine_grade(95) == "A"
    assert determine_grade(85) == "B"
    assert determine_grade(75) == "C"
    assert determine_grade(65) == "D"
    assert determine_grade(50) == "F"
    assert determine_grade(90) == "A"
    assert determine_grade(89.99) == "B"

    print("All tests passed!")

if __name__ == "__main__":
    test_grade_tracker()
    main()
