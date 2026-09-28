def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average  

def classify_result(average):
    if average >= 87:
        return "Distinction"
    elif average >= 75:
        return "Pass"
    else:
        return "Fail"