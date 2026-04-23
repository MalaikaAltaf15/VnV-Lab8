from student_system import login, calculate_average

def test_login_success():
    assert login("admin", "1234") == True

def test_login_fail():
    assert login("user", "wrong") == False

def test_average():
    assert calculate_average([85, 90]) == 87.5


def test_average_decimal():
    assert calculate_average([85, 90]) == 87.5

def test_empty_marks():
    try:
        calculate_average([])
        assert False
    except ZeroDivisionError:
        assert True