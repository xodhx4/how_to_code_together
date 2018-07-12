import pytest
import os
from readInputTextFile import readInputTextFile
from deleteOutlier import deleteOutlier
from remainOddOrEven import remainOddOrEven
from countNumOfUnique import countNumOfUnique
from myOwnCounter import myOwnCounter

dirname = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dirname, "input_ex.txt")

def test_readInputTextFile():
    func_list = readInputTextFile(filename)
    answer_list = [6, 13, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]

    assert func_list == answer_list


def test_deleteOutlier():
    input_list = [6, 13, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]
    func_list = deleteOutlier(input_list)
    answer_list = [13, 15, 13, 11, 16, 19, 12, 15, 14]

    assert func_list == answer_list

def test_remainOddOrEven():
    input_list = [13, 15, 13, 11, 16, 19, 12, 15, 14]
    func_list = remainOddOrEven(input_list)
    answer_list = [13, 15, 13, 11, 19, 15]

    assert func_list == answer_list
    
def test_countNumOfUnique():
    input_list = [13, 15, 13, 11, 19, 15]
    func = countNumOfUnique(input_list)

    assert func == 4

def test_myOwnCounter():
    func = myOwnCounter(filename)

    assert func == 4