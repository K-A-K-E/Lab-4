# ECOR 1042 Lab 4 - Individual submission for test3 function

# import load_data module here

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ethan Huang"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101332254"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"

#==========================================#
# Do not modify the code already provided.

from load_data import student_school_list, student_health_list, student_failures_list, student_age_list, load_data, add_average

def test_return_correct_dict_inside_list() -> list[int]:
    # Complete the function with your test cases
    file = "student-test.csv"
    pass_counter = 0
    fail_counter = 0
    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    test_cases_school = {"GP": [{'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},{'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}],
                         "MS": [{'ID': 29, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'FallGrade': 11, 'WinterGrade': 10},{'ID': 32, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}],
                         "MB": [{'ID': 21, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 5, 'WinterGrade': 5},{'ID': 22, 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 12}]
                         }
    for case in test_cases_school:
        try:
            temp = test_cases_school[case]
            #n = len(student_school_list(file,case)) - 1
            func = student_school_list(file,case)
            assert func[0] == temp[0] and func[-1] == temp[-1], \
            "Test Case: \"" + str(case) + "\" failed"
        except AssertionError as msg:
            print(msg)
            fail_counter += 1
        else:
            pass_counter += 1
    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    test_cases_age = {
        18: [{'School': 'GP', 'ID': 10, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'MS', 'ID': 32, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}],
        15: [{'School': 'GP', 'ID': 20, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'CF', 'ID': 23, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 9}],
        17: [{'School': 'GP', 'ID': 100, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5},{'School': 'MS', 'ID': 31, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'FallGrade': 14, 'WinterGrade': 14}]
        }
    for case in test_cases_age:
        try:
            temp = test_cases_age[case]
            func = student_age_list(file, case)
            assert func[0] == temp[0] and func[-1] == temp[-1],\
                "Test Case: \"" + str(case) + "\" failed"
        except AssertionError as msg:
            print(msg)
            fail_counter += 1
        else:
            pass_counter += 1
    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    test_cases_health = {
        3: [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'BD', 'ID': 27, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 1, 'FallGrade': 13, 'WinterGrade': 12}],
        1: [{'School': 'MS', 'ID': 30, 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 7, 'FallGrade': 10, 'WinterGrade': 9}, {'School': 'MS', 'ID': 30, 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 7, 'FallGrade': 10, 'WinterGrade': 9}],
        5: [{'School': 'CF', 'ID': 24, 'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 12}, {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]
    }
    for case in test_cases_health:
        try:
            temp = test_cases_health[case]
            func = student_health_list(file, case)
            assert func[0] == temp[0] and func[-1] == temp[-1], \
                "Test Case: \"" + str(case) + "\" failed"
        except AssertionError as msg:
            print(msg)
            fail_counter += 1
        else:
            pass_counter += 1
    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    test_cases_failures = {
        0: [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}],
        3: [{'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}],
        2: [{'School': 'CF', 'ID': 23, 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 9}, {'School': 'CF', 'ID': 25, 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 6}]
    }
    for case in test_cases_failures:
        try:
            temp = test_cases_failures[case]
            func = student_failures_list(file, case)
            assert func[0] == temp[0] and func[-1] == temp[-1], \
                "Test Case: \"" + str(case) + "\" failed"
        except AssertionError as msg:
            print(msg)
            fail_counter += 1
        else:
            pass_counter += 1
    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    test_cases_load_data = [
        {"School": {"GP": [{'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},{'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]}},
        {"Age": {18: [{'School': 'GP', 'ID': 10, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'MS', 'ID': 32, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]}},
        {"Health": {3: [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'BD', 'ID': 27, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 1, 'FallGrade': 13, 'WinterGrade': 12}]}},
        {"Failures": {0: [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]}},
        {"Failures": {3: [{'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]}},
        {"School": {"MS": [{'ID': 29, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'FallGrade': 11, 'WinterGrade': 10},{'ID': 32, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]}}
    ]

    j = 0
    for case in test_cases_load_data:
        call = list(test_cases_load_data[j])[0] #School, Age, Health, Failures
        dict = test_cases_load_data[j][call]
        for temp in dict:
            try:
                result = dict[temp]
                func = load_data(file, {call: temp})
                assert func[0] == result[0] and func[-1] == result[-1], \
                    "Test Case: \"" + str(case) + "\" failed"
            except AssertionError as msg:
                print(msg)
                fail_counter += 1
            else:
                pass_counter += 1
        j += 1

    # test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    cases_avg = [[{'School': 'GP', 'ID': 10, 'Age': 18,'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 6}],
                 [{'School': 'GP', 'ID': 20, 'Age': 15,'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10,'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MS', 'ID': 32, 'Age': 18,'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2,'FallGrade': 9, 'WinterGrade': 8}],
                 [{'School': 'MB', 'ID': 21, 'Age': 16,'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12,'FallGrade': 5, 'WinterGrade': 5}, {'School': 'CF', 'ID': 23, 'Age': 15,'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 9}, {'School': 'BD', 'ID': 28, 'Age': 17,'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4,'FallGrade': 10, 'WinterGrade': 9}]
                 ]
    #case1 = [{'School': 'GP', 'ID': 10, 'Age': 18,'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 6}]
    #case2 = [{'School': 'GP', 'ID': 20, 'Age': 15,'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10,'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MS', 'ID': 32, 'Age': 18,'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2,'FallGrade': 9, 'WinterGrade': 8}]
    #case3 = [{'School': 'MB', 'ID': 21, 'Age': 16,'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12,'FallGrade': 5, 'WinterGrade': 5}, {'School': 'CF', 'ID': 23, 'Age': 15,'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 9}, {'School': 'BD', 'ID': 28, 'Age': 17,'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4,'FallGrade': 10, 'WinterGrade': 9}]

    cases_avg_results = [
        [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, {'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}],
        [{'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8, 'AvgGrade': 7.5}, {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8, 'AvgGrade': 8.5}],
        [{'School': 'MB', 'ID': 21, 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 5, 'WinterGrade': 5, 'AvgGrade': 5.0}, {'School': 'BD', 'ID': 28, 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 9, 'AvgGrade': 9.5}]
    ]
    i = 0
    for case in cases_avg_results:
        try:
            temp = cases_avg_results[i]
            func = add_average(cases_avg[i])
            assert func[0] == temp[0] and func[-1] == temp[-1], \
                "Test Case: \"" + str(case) + "\" failed"
        except AssertionError as msg:
            print(msg)
            fail_counter += 1
        else:
            pass_counter += 1
    i += 1
    # return the a list with the number of tests that passed and the number that failed
    return [pass_counter,fail_counter]

# Do NOT include a main script in your submission
print(test_return_correct_dict_inside_list())
