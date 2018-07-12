import pytest
import exercise

def test_readInputTextFile():
    func_list = exercise.readInputTextFile("input_ex.txt")
    answer_list = [6, 14, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]

    assert func_list == answer_list


def test_deleteOutlier():
    input_list = [6, 14, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]
    func_list = exercise.deleteOutlier(input_list)
    answer_list = [14, 15, 13, 11, 16, 19, 12, 15, 14]

    assert func_list == answer_list

def test_remainOddOrEven():
    input_list = [14, 15, 13, 11, 16, 19, 12, 15, 14]
    func_list = exercise.remainOddOrEven(input_list)
    answer_list = [13, 15, 13, 11, 19, 15]

    assert func_list == answer_list
    
def test_countNumOfUnique():
    input_list = [13, 15, 13, 11, 19, 15]
    func = exercise.countNumOfUnique(input_list)

    assert func == 4

def test_myOwnCounter():
    func = exercise.myOwnCounter("input_ex.txt")

    assert func == 4