import trees

dataset, labels = trees.create_dataset()
print(dataset)
trees.best_feature_split(dataset)
best_feature = trees.best_feature_split(dataset)
print(best_feature)