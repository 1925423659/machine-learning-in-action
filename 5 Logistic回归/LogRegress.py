# coding:UTF-8

import numpy
import math

def load_dataset():
    data_array = []
    label_array = []
    f = open('testSet.txt')
    for line in f.readlines():
        array = line.strip().split('\t')
        data_array.append([1.0, float(array[0]), float(array[1])])
        label_array.append(int(array[2]))
    return data_array, label_array

def sigmoid(input):
    return 1.0 / (1 + numpy.exp(-input))

def grad_ascent(data_array, label_array):
    data_matrix = numpy.mat(data_array)
    label_matrix = numpy.mat(label_array)
    m, n = numpy.shape(data_matrix)
    alpha = 0.001
    cycles = 500
    weights = numpy.ones((n, 1))
    for i in range(cycles):
        h = sigmoid(data_matrix * weights)
        error = label_matrix.transpose() - h
        weights = weights + alpha * data_matrix.transpose() * error
    return weights

def stoc_grad_ascent_1(data_matrix, label_matrix):
    m, n = numpy.shape(data_matrix)
    alpha = 0.01
    weights = numpy.ones(n)
    for i in range(m):
        h = sigmoid(sum(data_matrix[i] * weights))
        error = label_matrix[i] - h
        weights = weights + alpha * error * data_matrix[i]
    return weights

def stoc_grad_ascent_2(data_matrix, label_matrix, num_iter=150):
    import random

    m, n = numpy.shape(data_matrix)
    weights = numpy.ones(n)
    for iter in range(num_iter):
        range_m = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + i + iter) + 0.01
            index = int(random.uniform(0, len(range_m)))
            h = sigmoid(sum(data_matrix[index] * weights))
            error = label_matrix[index] - h
            weights = weights + alpha * error * data_matrix[index]
            del(range_m[index])
    return weights

def plot_best_fit(weights):
    import matplotlib.pyplot
    data_matrix, label_matrix = load_dataset()
    data_array = numpy.array(data_matrix)
    n = numpy.shape(data_array)[0]
    x_coord_1 = []
    y_coord_1 = []
    x_coord_2 = []
    y_coord_2 = []
    for i in range(n):
        if int(label_matrix[i]) == 1:
            x_coord_1.append(data_array[i, 1])
            y_coord_1.append(data_array[i, 2])
        else:
            x_coord_2.append(data_array[i, 1])
            y_coord_2.append(data_array[i, 2])
    figure = matplotlib.pyplot.figure()
    subplot = figure.add_subplot(111)
    subplot.scatter(x_coord_1, y_coord_1, s=30, c='red', marker='s')
    subplot.scatter(x_coord_2, y_coord_2, s=30, c='green')
    x = numpy.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    subplot.plot(x, y)
    matplotlib.pyplot.xlabel('x_1')
    matplotlib.pyplot.ylabel('x_2')
    matplotlib.pyplot.show()

def classify_vector(input, weights):
    prob = sigmoid(sum(input * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colic_test():
    f_train = open('horseColicTraining.txt')
    f_test = open('horseColicTest.txt')
    train_data_array = []
    train_label_array = []
    for line in f_train.readlines():
        array = line.strip().split('\t')
        data = []
        for i in range(21):
            data.append(float(array[i]))
        train_data_array.append(data)
        train_label_array.append(float(array[21]))
    train_weights = stoc_grad_ascent_2(numpy.array(train_data_array), numpy.array(train_label_array), 500)
    
    error_count = 0
    test_vec_num = 0
    for line in f_test.readlines():
        test_vec_num += 1
        array = line.strip().split('\t')
        data = []
        for i in range(21):
            data.append(float(array[i]))
        label = classify_vector(numpy.array(data), train_weights)
        if int(label) != int(array[21]):
            error_count += 1
    error_rate = float(error_count) / test_vec_num
    print('the error rate of this test is: ', error_rate)
    return error_rate