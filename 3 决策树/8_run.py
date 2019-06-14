import trees
import tree_plotter

tree = tree_plotter.retrieve_tree(0)
print(tree)
dataset, labels = trees.create_dataset()
print(labels)
label = trees.classify(tree, labels, [1, 0])
print(label)
label = trees.classify(tree, labels, [1, 1])
print(label)