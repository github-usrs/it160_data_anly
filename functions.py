'''Michael Jolley and Cole Walther - PA 4 - 3/26/2024'''

import random
import matplotlib.pyplot as plt
import numpy as np
import statistics

class Student:
    def __init__(self, num_classes):
        self.grades = [random.randint(0, 100) for _ in range(num_classes)]

def generate_grades(num_students, num_classes):
    return [Student(num_classes) for _ in range(num_students)]

def plot_grades(students):
    for i, student in enumerate(students):
        plt.plot(student.grades, label=f'Student {i+1}')
    plt.legend()
    plt.show()

def calculate_statistics(students):
    statistics = []
    for i in range(len(students[0].grades)):
        grades = [student.grades[i] for student in students]
        max_grade = max(grades)
        min_grade = min(grades)
        avg_grade = sum(grades) / len(grades)
        median_grade = statistics.median(grades)
        std_dev = statistics.stdev(grades)
        statistics.append((max_grade, min_grade, avg_grade, median_grade, std_dev))
    return statistics

def plot_statistics(statistics):
    labels = ['Max', 'Min', 'Avg', 'Median', 'Std Dev']
    for i, class_statistics in enumerate(statistics):
        plt.plot(class_statistics, label=f'Class {i+1}')
    plt.xticks(range(len(labels)), labels)
    plt.legend()
    plt.show()

def plot_histogram(students):
    math_grades = [student.grades[0] for student in students]
    plt.hist(math_grades, bins=range(101), edgecolor='black')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.show()

def main():
    num_students = 20
    num_classes = 6
    students = generate_grades(num_students, num_classes)
    plot_grades(students)
    statistics = calculate_statistics(students)
    plot_statistics(statistics)
    plot_histogram(students)

if __name__ == "__main__":
    main()

'''
import random
import matplotlib.pyplot as plt
import numpy as np

class Student:
    def __init__(self):
        self.classAndGrade = {
            'Math': random.randint(0, 100),
            'Physics': random.randint(0, 100),
            'Recreation': random.randint(0, 100),
            'History': random.randint(0, 100),
            'English': random.randint(0, 100),
            'Chemistry': random.randint(0, 100)
        }

numStudents = random.randint(15, 25)

def generate_grades(numStudents):
    students = [Student() for _ in range(numStudents)]
    return students

def plotGrades():
    # Generate grades for a random number of students
    grades = generate_grades(numStudents)
    # Get the list of subjects
    subjects = list(grades[0].classAndGrade.keys())
    # Initialize a dictionary to store the total grades for each subject
    averages = {subject: 0 for subject in subjects}
    # For each student, add their grade for each subject to the total
    for student in grades:
        for subject in subjects:
            averages[subject] += student.classAndGrade[subject]
    # Calculate the average grade for each subject
    for subject in subjects:
        averages[subject] /= numStudents
    # Create a bar plot of the average grades for each subject
    fig, ax = plt.subplots()
    ax.bar(subjects, [averages[subject] for subject in subjects])
    ax.set_ylabel('Average Grade')
    ax.set_title('Average Grade by Subject')
    plt.show()

def calculateStatistics():
    # Generate grades for a random number of students
    grades = generate_grades(numStudents)
    # Get the list of subjects
    subjects = list(grades[0].classAndGrade.keys())
    # Initialize a dictionary to store the total grades for each subject
    averages = {subject: 0 for subject in subjects}
    # For each student, add their grade for each subject to the total
    for student in grades:
        for subject in subjects:
            averages[subject] += student.classAndGrade[subject]
    # Calculate the average grade for each subject
    for subject in subjects:
        averages[subject] /= numStudents
    # Print the average grade for each subject
    print('Average Grade by Subject:')
    for subject in subjects:
        print(f'{subject}: {averages[subject]}')
    # Print the total number of students
    print(f'Total number of students: {numStudents}')
    # Calculate and print the average GPA (assuming each subject is equally weighted and out of 100)
    print(f'Average GPA: {np.mean([sum(student.classAndGrade.values()) for student in grades]) / 600}')
'''
