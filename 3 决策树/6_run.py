import tree_plotter

tree = tree_plotter.retrieve_tree(1)
print(tree)
leaf = tree_plotter.leaf(tree)
depth = tree_plotter.depth(tree)
print(leaf, depth)
tree = tree_plotter.retrieve_tree(0)
print(tree)
leaf = tree_plotter.leaf(tree)
depth = tree_plotter.depth(tree)
print(leaf, depth)