# ECOR 1042 Lab 4 - Individual submission for test4 function

# import load_data module here
from load_data import add_average

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kyle Freeman"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101341567"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-15"

#==========================================#
# Do not modify the code alreayd provided.


def test_add_average() -> list[int]:
    # Complete the function with your test cases
    
    test_cases_1 = [
                    [{'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}, 
                     {'ID': 1, 'Age': 17, 'StudyTime': 6.0, 'Failures': 3, 'Health': 7, 'Absences': 2, 'FallGrade': 19, 'WinterGrade': 13}], 

                   [{'School': 'GB', 'ID': 2, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                    
                    [{'School': 'GB', 'ID': 3, 'Age': 19, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 3, 'WinterGrade': 3}, 
                     {'School': 'MS', 'ID': 20, 'Age': 17, 'StudyTime': 9.0, 'Health': 3, 'Absences': 7, 'FallGrade': 18, 'WinterGrade': 17}],

                    [{'School': 'MS', 'ID': 89, 'Age': 21, 'StudyTime': 3.0, 'Failures': 3, 'Absences': 1, 'FallGrade': 6, 'WinterGrade': 6}, 
                     {'School': 'GB', 'ID': 43, 'Age': 20, 'StudyTime': 2.0, 'Failures': 7, 'Absences': 2, 'FallGrade': 1, 'WinterGrade': 13}, 
                     {'School': 'GB', 'ID': 54, 'Age': 20, 'StudyTime': 10.0, 'Failures': 7, 'Absences': 3, 'FallGrade': 8, 'WinterGrade': 6}],

                    [{'School': 'GB', 'ID': 72, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                   []
                   ]
    test_answers_1 = [2, 1, 2, 3, 1, 0]
    
    test_cases_2 = [
                [{'ID': 6, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}], 

                [{'School': 'GB', 'ID': 7, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                
                [{'School': 'GB', 'ID': 8, 'Age': 18, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 9, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 10, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}]
                ]
    
    test_cases_3 = [
                [{'ID': 11, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 6}], 

                [{'School': 'GB', 'ID': 12, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                
                [{'School': 'GB', 'ID': 13, 'Age': 18, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 10}],

                [{'School': 'GB', 'ID': 14, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Absences': 7, 'FallGrade': 8, 'WinterGrade': 8}],

                [{'School': 'GB', 'ID': 15, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 15, 'WinterGrade': 14}]
                ]
    test_answers_3 = [9.0, 12.5, 11.0, 8.0, 14.5]

    passed = 0
    failed = 0
    test_num_1 = 0
    test_num_2 = 0
    test_num_3 = 0
    i = 0
    j = 0

    # test that the function does not change the lengh of the list
    # provided as input parameter (5 different test cases required)

    for test_1 in test_cases_1:
        try:
            test_num_1 += 1
            assert len(add_average(test_1)) == test_answers_1[i], f"test {test_num_1} for length of list failed."
            passed += 1
            i += 1
        except AssertionError as msg:
            print(msg)
            failed += 1
            i += 1

    # test that the function returns an empty list when it is called whith an empty list
    # test that the function inscrememnts the number of keys of the
    # dictionary inside the list by one  (5 different test cases required)
    for test_2 in test_cases_2:
        num_keys = len(test_2[0])
        num_avg_keys = len(add_average(test_2)[0])
        test_num_2 += 1
        try:
            assert num_avg_keys == num_keys + 1, f"test {test_num_2} for having the correct amount of keys failed."
            passed += 1
        except AssertionError as msg:
            print(msg)
            failed += 1

    # test that the G_Avg value is properly calculated  (5 different test cases required)

    for test_3 in test_cases_3:
        try:
            test_num_3 += 1
            average_test = add_average(test_3)[0]
            assert abs(average_test["AvgGrade"] - test_answers_3[j]) < 0.001, f"test {test_num_3} for calculating the correct average grade failed."
            # assert average_test["AvgGrade"] == test_answers_3[j]
            passed += 1
            j += 1
        except AssertionError as msg:
            print(msg)
            failed += 1
            j += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]

# Do NOT include a main script in your submission
