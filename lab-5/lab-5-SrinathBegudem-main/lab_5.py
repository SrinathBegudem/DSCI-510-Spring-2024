# Lab 5
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def transform_tuple(original_tuple: tuple) -> tuple[int, int]:
    even_sum = 0
    odd_sum = 0

    for i in original_tuple:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return even_sum, odd_sum

# invoke the function with relevant args of your choice
result = transform_tuple((1, 2, 3, 4, 5, 6))
print(result)



# ----------------- Question 2 -----------------
def grade_summary(student_grades):
    dict_final = {}
    for student, grades in student_grades.items():
        average = round(sum(grades) / len(grades), 2)
        maximum = max(grades)
        dict_final[student] = {"average": average, "highest": maximum}
    return dict_final

result = grade_summary({"Alice": [88, 92, 100], "Bob": [75, 78, 80]})
print(result)



# ----------------- Question 3 -----------------
def unique_letters(string1: str, string2: str) -> tuple[set, set]:
    set1 = set(string1) - set(string2)
    set2 = set(string2) - set(string1)
    return set1, set2


# invoke the function with relevant args of your choice
result = unique_letters('banana', 'papaya')
print(result)
