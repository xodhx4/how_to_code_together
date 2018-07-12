import sys

def readInputTextFile(filename):
    """Read input file(filename) and return list of int
    
    Arguments:
        filename {[string]} -- [name of input file]
    
    Returns:
        [list of int] -- [input list]
    """
    
    return int_list

def deleteOutlier(int_list):
    """Delelte outlier (not 10-20) int
    
    Arguments:
        int_list {[list of int]} -- [input list]
    
    Returns:
        [list of int] -- [outlier deleted list]
    """
    
    return modified_list

def remainOddOrEven(int_list):
    """Delete odd or even int by length of list
    
    Arguments:
        int_list {[list of int]} -- [outlier deleted list]
    
    Returns:
        [list of int] -- [only odd or even ints]
    """
    
    return modified_list

def countNumOfUnique(int_list):
    """Count number of diff int
    
    Arguments:
        int_list {[list of int]} -- [only odd or even ints]
    
    Returns:
        [int] -- [number of diff int]
    """
    
    return num_of_uniq

def myOwnCounter(filename):
    """Our Final Function
    
    Arguments:
        filename {[string]} -- [input file name]
    
    Returns:
        [int] -- [result]
    """
    
    return num_of_uniq

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = "input.txt"
    else:
        filename = sys.argv[1]
    print("Answer in {}".format(myOwnCounter(filename)))
