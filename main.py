from grading_utils import calculate_average, classify_result

marks = [100, 94, 77, 86]

average = calculate_average(marks)
result = classify_result(average)

print("Average marks:", average)
print("Result:", result)