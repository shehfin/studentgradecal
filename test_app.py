from app import calculate_metrics, calculate_grade

def test_calculate_metrics():
    marks = [80, 90, 70]
    total, average = calculate_metrics(marks)
    assert total == 240
    assert average == 80

def test_calculate_grade():
    assert calculate_grade(95) == 'A'
    assert calculate_grade(82) == 'B'
    assert calculate_grade(55) == 'F'
