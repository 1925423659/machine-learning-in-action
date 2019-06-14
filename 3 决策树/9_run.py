import trees
import tree_plotter

tree = tree_plotter.retrieve_tree(0)
print(tree)
trees.store_tree(tree, 'classifier_storage.txt')
storage_tree = trees.grab_tree('classifier_storage.txt')
print(storage_tree)