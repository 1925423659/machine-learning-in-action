import kNN

dataset, labels = kNN.file_to_array('datingTestSet2.txt')
print(dataset)
print(labels)

normalize_dataset, min_array, max_array, range_array = kNN.normalize(dataset)

print(normalize_dataset)
print(min_array)
print(max_array)
print(range_array)