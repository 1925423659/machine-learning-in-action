import trees

dataset, labels = trees.create_dataset()
print(dataset)
print(labels)
tree = trees.create_tree(dataset, labels)
print(tree)