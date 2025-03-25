#ECOR 1042 Lab 4 - Individual submission for test1 function 

# import load_data module here
from load_data import *
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kaitlyn Ward"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101338155"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"

#==========================================#
# Do not modify the code alreayd provided.
def test_return_list() -> list[int]:
    # Complete the function with your test cases
    test_fail = 0
    test_pass = 0
    # test that student_school_list returns a list (3 different test cases required)
    try: 
        result1 = student_school_list('student-test.csv', 'GP')
        assert isinstance(student_school_list('student-test.csv', 'GP'), list) #checks if it's a list 
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    
    try:
        result2 = student_school_list('student-test.csv', 'ML')
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1    
   
    try:    
        result3 = student_school_list('student-test.csv', 'MS')
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e: 
        print(e)
        test_fail+=1
    
    # test that student_age_list returns a list (3 different test cases required)
    try:   
        result1 = student_age_list('student-test.csv', 18)
        assert isinstance(result1, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    
    try:
        result2 = student_age_list('student-test.csv', 15)
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    
    try:
        result3 = student_age_list('student-test.csv', 19)
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    # test that student_health_list returns a list (3 different test cases required)
    try:    
        result1 = student_health_list('student-test.csv', 1)
        assert isinstance(result1, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    try:
        result2 = student_health_list('student-test.csv', 5)
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    
    try:
        result3 = student_health_list('student-test.csv', 3)
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
    
    # test that student_failures_list returns a list (3 different test cases required)
    try:
        result1 = student_failures_list('student-test.csv', 0)
        assert isinstance(result1, list)
        test_pass += 1
    except AssertionError as e: 
        print(e)
        test_fail+=1
    
    try:
        result2 = student_failures_list('student-test.csv', 3)
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result3 = student_failures_list('student-test.csv', 1)
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1
   
    # test that load_data returns a list (6 different test cases required)
    try:
        result1 = load_data('student-test.csv', {"Failures" : 1})
        assert isinstance(result1, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result2 = load_data('student-test.csv', {"Age": 19})
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result3 = load_data('student-test.csv', {"Failures" : 4})
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e: 
        print(e)
        test_fail+=1

    try:
        result4 = load_data('student-test.csv', {"School" : "MB"})
        assert isinstance(result4, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result5 = load_data('student-test.csv', {"Health" : 4})
        assert isinstance(result5, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result6 = load_data('student-test.csv', {"School" : "GP"})
        assert isinstance(result6, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    # test that add_average returns a list (3 different test cases required)
    try: 
        result1 = add_average([{'School': 'GP', 'ID': 1, 'Age': 18,'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 6}])
        assert isinstance(result1, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result2 = add_average([{'School': 'GP', 'ID': 2, 'Age': 17,'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4,'FallGrade': 5, 'WinterGrade': 5}])
        assert isinstance(result2, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    try:
        result3 = add_average(([{'School': 'GP', 'ID': 3, 'Age': 15,'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10,'FallGrade': 7, 'WinterGrade': 8}]))
        assert isinstance(result3, list)
        test_pass += 1
    except AssertionError as e:
        print(e)
        test_fail+=1

    # return the a list with the number of tests that passed and the number that failed
    return [test_pass, test_fail]

# Do NOT include a main script in your submission
