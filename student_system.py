def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

def calculate_average(marks):
    return sum(marks) // len(marks)   # WRONG (integer division)