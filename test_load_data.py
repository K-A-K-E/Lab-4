# ECOR 1042 Lab 4 - team submission

# import load_data module here
from load_data import *

# Update "" with your the name of the active members of the team
__author__ = "Ethan Huang, Kyle Freeman, Abigale Cooper, Kaitlyn Ward"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T015"

#==========================================#

# Place test_return_list function here
def test_return_list() -> list[int]:
    # Complete the function with your test cases
    test_fail = 0
    test_pass = 0
    # test that student_school_list returns a list (3 different test cases required)
    count = 3
    try: 
        result1 = student_school_list('student-test.csv', 'GP')
        assert isinstance(result1, list) #checks if it's a list 
        test_pass += 1
        count -= 1
       
        result2 = student_school_list('student-test.csv', 'ML')
        assert isinstance(result2, list)
        test_pass += 1
        count-= 1
        
        result3 = student_school_list('student-test.csv', 'MS')
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1
    except: 
        test_fail += count
    # test that student_age_list returns a list (3 different test cases required)
    try:   
        count = 3
        result1 = student_age_list('student-test.csv', 18)
        assert isinstance(result1, list)
        test_pass += 1
        count -= 1

        result2 = student_age_list('student-test.csv', 15)
        assert isinstance(result2, list)
        test_pass += 1
        count -= 1

        result3 = student_age_list('student-test.csv', 19)
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1
    except:
        test_fail += count

    # test that student_health_list returns a list (3 different test cases required)
    try:    
        count = 3
        result1 = student_health_list('student-test.csv', 1)
        assert isinstance(result1, list)
        test_pass += 1
        count -= 1

        result2 = student_health_list('student-test.csv', 5)
        assert isinstance(result2, list)
        test_pass += 1
        count -= 1

        result3 = student_health_list('student-test.csv', 3)
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1
    except:
        test_fail += count
    # test that student_failures_list returns a list (3 different test cases required)
    try:
        count = 3
        result1 = student_failures_list('student-test.csv', 0)
        assert isinstance(result1, list)
        test_pass += 1
        count -= 1

        result2 = student_failures_list('student-test.csv', 3)
        assert isinstance(result2, list)
        test_pass += 1
        count -= 1

        result3 = student_failures_list('student-test.csv', 1)
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1
    except:
        test_fail += count
    # test that load_data returns a list (6 different test cases required)
    try:
        count = 6
        result1 = load_data('student-test.csv', {"Failures" : 1})
        assert isinstance(result1, list)
        test_pass += 1
        count -= 1

        result2 = load_data('student-test.csv', {"Age": 19})
        assert isinstance(result2, list)
        test_pass += 1
        count -= 1

        result3 = load_data('student-test.csv', {"Failures" : 4})
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1

        result4 = load_data('student-test.csv', {"School" : "MB"})
        assert isinstance(result4, list)
        test_pass += 1
        count -= 1

        result5 = load_data('student-test.csv', {"Health" : 4})
        assert isinstance(result5, list)
        test_pass += 1
        count -= 1

        result6 = load_data('student-test.csv', {"School" : "GP"})
        assert isinstance(result6, list)
        test_pass += 1
        count -= 1
    except:
        test_fail += count

    # test that add_average returns a list (3 different test cases required)
    try: 
        count = 3
        result1 = add_average([{'School': 'GP', 'ID': 1, 'Age': 18,'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6,'FallGrade': 5, 'WinterGrade': 6}])
        assert isinstance(result1, list)
        test_pass += 1
        count -= 1

        result2 = add_average([{'School': 'GP', 'ID': 2, 'Age': 17,'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4,'FallGrade': 5, 'WinterGrade': 5}])
        assert isinstance(result2, list)
        test_pass += 1
        count -= 1

        result3 = add_average(([{'School': 'GP', 'ID': 3, 'Age': 15,'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10,'FallGrade': 7, 'WinterGrade': 8}]))
        assert isinstance(result3, list)
        test_pass += 1
        count -= 1
    except:
        test_fail += count

    # return the a list with the number of tests that passed and the number that failed
    return [test_pass, test_fail]




# Place test_return_list_correct_lenght function here
def test_return_list_correct_length() -> list[int]:
    # Complete the function with your test cases
    file = 'student-test.csv'
    test = [0, 0]

    # test that student_school_list returns a list with the correct length (3 different test cases required)
    schools = ["GP", "ML", "MS"]
    length = [3, 0, 4]
    for i in range(len(schools)):
        try:
            assert len(student_school_list(file, schools[i])
                       ) == length[i], "wrong length for school list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # test that student_age_list returns a list  with the correct length (3 different test cases required)
    age = [17, 18, 2]
    length = [6, 4, 0]
    for i in range(len(age)):
        try:
            assert len(student_age_list(file, age[i])
                       ) == length[i], "wrong length for age list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # test that student_health_list returns a list  with the correct length (3 different test cases required)
    health = [3, 10, 5]
    length = [8, 0, 3]
    for i in range(len(health)):
        try:
            assert len(student_health_list(file, health[i])
                       ) == length[i], "wrong length for health list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # test that student_failures_list returns a list   with the correct length(3 different test cases required)
    failures = [2, 0, 4]
    length = [2, 11, 0]
    for i in range(len(failures)):
        try:
            assert len(student_failures_list(file, failures[i])
                       ) == length[i], "wrong length for failures list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # test that load_data returns a list  with the correct length (6 different test cases required)

    loadData = [{"Age": 18}, {"Health": 1}, {"Health": 2},
                {"School": "GP"}, {"Failures": 1}, {"All": 0}]
    length = [4, 1, 0, 3, 1, 15]
    for i in range(len(loadData)):
        try:
            assert len(load_data(file, loadData[i])
                       ) == length[i], "wrong length for load_data list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # test that add_average returns a list   with the correct length (3 different test cases required)
    average = [[{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}], [{'School': 'MB', 'ID': 21, 'Age': 16, 'StudyTime': 2,
                                                                                                                                                         'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 5, 'WinterGrade': 5}], [{'School': 'BD', 'ID': 26, 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}]]
    length = [1, 1, 1]
    for i in range(len(average)):
        try:
            assert len(add_average(average[i])
                       ) == length[i], "wrong length for add average list"
            test[0] += 1
        except AssertionError as error:
            test[1] += 1

    # return the a list with the number of tests that passed and the number that failed

    return test

    # Do NOT include a main script in your submission




# Place test_return_correct_dict_inside_list function here
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





# Place test_add_average function here
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
            passed += 1
            j += 1
        except AssertionError as msg:
            print(msg)
            failed += 1
            j += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]


# Do NOT include a main script in your submission
