import trees

dataset, labels = trees.create_dataset()
print(dataset)
entropy = trees.entropy(dataset)
print(entropy)