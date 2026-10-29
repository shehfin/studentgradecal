from app import calculate_metrics

def test_calculate_metrics():
    marks = [80, 90, 70]
    total, average = calculate_metrics(marks)
    assert total == 240
    assert average == 80
