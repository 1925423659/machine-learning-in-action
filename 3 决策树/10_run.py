import trees
import tree_plotter

f = open('lenses.txt')
dataset = [line.strip().split('\t') for line in f.readlines()]
labels = ['age', 'prescript', 'astigmatic', 'tearRate']
tree = trees.create_tree(dataset, labels)
print(tree)
tree_plotter.create_plot(tree)