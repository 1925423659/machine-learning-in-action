import kNN

dataset, labels = kNN.file_to_array('datingTestSet2.txt')
normalize_dataset, min_array, max_array, range_array = kNN.normalize(dataset)
dataset_len = dataset.shape[0]
ratio = 0.1
test_len = int(dataset_len * ratio)
train_dataset = normalize_dataset[:dataset_len - test_len, :]
train_labels = labels[:dataset_len - test_len]
error_len = 0

for i in range(dataset_len - test_len, dataset_len):
    label = kNN.classify(train_dataset, train_labels, normalize_dataset[i, :], 5)
    print('index: %d, train: %d, real: %d' % (i, label, labels[i]))
    if label != labels[i]:
        error_len += 1
print('error rate: %f' % (error_len/float(test_len)))