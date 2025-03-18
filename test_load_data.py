# ECOR 1042 Lab 4 - team submission

# import load_data module here

# Update "" with your the name of the active members of the team
__author__ = "Ethan Huang, Kyle Freeman, Abigale Cooper, Kaitlyn Ward"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T015"

#==========================================#

# Place test_return_list function here


# Place test_return_list_correct_lenght function here


# Place test_return_correct_dict_inside_list function here


# Place test_add_average function here
def test_add_average() -> list[int]:
    # Complete the function with your test cases
    
    test_values_1 = [
                    [{'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}], 

                   [{'School': 'GB', 'ID': 2, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                    
                    [{'School': 'GB', 'ID': 3, 'Age': 18, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                    [{'School': 'GB', 'ID': 4, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                    [{'School': 'GB', 'ID': 5, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                   []
                   ]
    
    test_values_2 = [
                [{'ID': 6, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}], 

                [{'School': 'GB', 'ID': 7, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                
                [{'School': 'GB', 'ID': 8, 'Age': 18, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 9, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 10, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}]
                ]
    
    test_values_3 = [
                [{'ID': 11, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}], 

                [{'School': 'GB', 'ID': 12, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],
                
                [{'School': 'GB', 'ID': 13, 'Age': 18, 'StudyTime': 7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 14, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}],

                [{'School': 'GB', 'ID': 15, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}]
                ]

    passed = 0
    failed = 0

    # test that the function does not change the lengh of the list
    # provided as input parameter (5 different test cases required)

    for test_1 in test_values_1:
        try:
            assert len(add_average(test_1)) <= 1
            passed += 1
        except:
            failed += 1

    # test that the function returns an empty list when it is called whith an empty list
    # test that the function inscrememnts the number of keys of the
    # dictionary inside the list by one  (5 different test cases required)
    for test_2 in test_values_2:
        num_keys = len(test_2[0])
        num_avg_keys = len(add_average(test_2)[0])
        try:
            assert num_avg_keys == num_keys + 1
            passed += 1
        except:
            failed += 1

    # test that the G_Avg value is properly calculated  (5 different test cases required)

    for test_3 in test_values_3:
        try:
            average_test = add_average(test_3)[0]
            assert average_test["AvgGrade"] == 12.5
            passed += 1
        except:
            failed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]


# Do NOT include a main script in your submission
