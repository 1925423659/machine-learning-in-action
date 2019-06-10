import sys
import numpy

def exercise_numpy_random_rand():
    print('<<<', sys._getframe().f_code.co_name)
    array = numpy.random.rand(4, 4)
    print(array)
    print('>>>')

def exercise_numpy_mat():
    print('<<<', sys._getframe().f_code.co_name)
    array = numpy.random.rand(4, 4)
    print(array, type(array))
    matrix = numpy.mat(array)
    print(matrix, type(matrix))
    print('>>>')

def exercise_matrix_I():
    print('<<<', sys._getframe().f_code.co_name)
    array = numpy.random.rand(4, 4)
    matrix = numpy.mat(array)
    print(matrix)
    matrix_I = matrix.I
    print(matrix_I)
    print('>>>')


# exercise_numpy_random_rand()
# exercise_numpy_mat()
exercise_matrix_I()