def calculate_metrics(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average

if __name__ == "__main__":
    sample_marks = [85, 90, 78, 92, 88]
    tot, avg = calculate_metrics(sample_marks)
    print(f"Total Marks: {tot}")
    print(f"Average Marks: {avg}")
