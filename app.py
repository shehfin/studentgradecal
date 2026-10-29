def calculate_metrics(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average

def calculate_grade(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

if __name__ == "__main__":
    sample_marks = [85, 90, 78, 92, 88]
    tot, avg = calculate_metrics(sample_marks)
    grade = calculate_grade(avg)
    print(f"Total Marks: {tot}")
    print(f"Average Marks: {avg}")
    print(f"Final Grade: {grade}")
