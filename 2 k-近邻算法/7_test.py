import kNN
import numpy
import os

train_file_array = os.listdir('digits/trainingDigits')
train_file_len = len(train_file_array)
train_labels = []
train_dataset = numpy.zeros((train_file_len, 1024))
for i in range(train_file_len):
    filename = train_file_array[i]
    label = filename.split('.')[0]
    label = label.split('_')[0]
    label = int(label)
    train_labels.append(label)
    train_dataset[i, :] = kNN.image_to_array('digits/trainingDigits/' + filename)

test_file_array = os.listdir('digits/testDigits')
test_file_len = len(test_file_array)
error_len = 0
for i in range(test_file_len):
    filename = test_file_array[i]
    label = filename.split('.')[0]
    label = label.split('_')[0]
    label = int(label)
    input = kNN.image_to_array('digits/testDigits/' + filename)
    result = kNN.classify(train_dataset, train_labels, input, 5)
    print('result: %d, label: %d' % (result, label))
    if result != label:
        error_len += 1
print('error count: %d' % error_len)
print('error rate: %f' % (error_len / float(test_file_len)))