import trees

dataset, labels = trees.create_dataset()
print(dataset)
split_dataset = trees.split_dataset(dataset, 0, 1)
print(split_dataset)
split_dataset = trees.split_dataset(dataset, 0, 0)
print(split_dataset)