# coding:UTF-8

import matplotlib.pyplot

decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')    

def plot_node(subplot, node_type, parent_point, center_point, node_text):
    subplot.annotate(node_text, xy=parent_point, xycoords='axes fraction',
                                xytext=center_point, textcoords='axes fraction',
                                va='center', ha='center', bbox=node_type, arrowprops=arrow_args)

# def create_plot():
#     figure = matplotlib.pyplot.figure(1, facecolor='white')
#     figure.clf()
#     subplot = matplotlib.pyplot.subplot(111, frameon=False)
#     subplot.annotate('a decision node', xy=(0.1, 0.5), xycoords='axes fraction',
#                                 xytext=(0.5, 0.1), textcoords='axes fraction',
#                                 va='center', ha='center', bbox=decision_node, arrowprops=arrow_args)
#     subplot.annotate('a leaf node', xy=(0.3, 0.8), xycoords='axes fraction',
#                                 xytext=(0.8, 0.1), textcoords='axes fraction',
#                                 va='center', ha='center', bbox=leaf_node, arrowprops=arrow_args)
#     matplotlib.pyplot.show()

def leaf(tree):
    leaf_num = 0
    key = tree.keys()[0]
    sub_tree = tree[key]
    for key, value in sub_tree.items():
        if type(value).__name__ == 'dict':
            leaf_num += leaf(value)
        else:
            leaf_num += 1
    return leaf_num

def depth(tree):
    depth_num = 0
    key = tree.keys()[0]
    sub_tree = tree[key]
    for key, value in sub_tree.items():
        if type(value).__name__ == 'dict':
            current_depth = 1 + depth(value)
        else:
            current_depth = 1
        if depth_num < current_depth:
            depth_num = current_depth
    print(tree, depth_num)
    return depth_num

def retrieve_tree(i):
    tree = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
            {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return tree[i]

def plot_text(subplot, parent_point, center_point, text):
    x = (parent_point[0] - center_point[0]) / 2.0 + center_point[0]
    y = (parent_point[1] - center_point[1]) / 2.0 + center_point[1]
    subplot.text(x, y, text)

def plot_tree(tree, subplot, parent_point, text):
    leaf_num = leaf(tree)
    depth_num = depth(tree)
    key = tree.keys()[0]
    subtree = tree[key]
    center_point = (plot_tree.xOff + (1.0 + float(leaf_num)) / 2.0 / plot_tree.totalW,
                    plot_tree.yOff)
    plot_text(subplot, parent_point, center_point, text)
    plot_node(subplot, decision_node, parent_point, center_point, key)
    plot_tree.yOff = plot_tree.yOff - 1.0 / plot_tree.totalD
    for key, value in subtree.items():
        if type(value).__name__ == 'dict':
            plot_tree(value, subplot, center_point, str(key))
        else:
            plot_tree.xOff = plot_tree.xOff + 1.0 / plot_tree.totalW
            plot_node(subplot, leaf_node, center_point, (plot_tree.xOff, plot_tree.yOff), value)
            plot_text(subplot, (plot_tree.xOff, plot_tree.yOff), center_point, str(key))
    plot_tree.yOff = plot_tree.yOff + 1.0 / plot_tree.totalD

def create_plot(tree):
    figure = matplotlib.pyplot.figure(1, facecolor='white')
    figure.clf()
    axprops = {'xticks': [], 'yticks': []}
    subplot = matplotlib.pyplot.subplot(111, frameon=False, **axprops)
    plot_tree.totalW = float(leaf(tree))
    plot_tree.totalD = float(depth(tree))
    plot_tree.xOff = -0.5 / plot_tree.totalW
    plot_tree.yOff = 1.0
    plot_tree(tree, subplot, (0.5, 1.0), '')
    matplotlib.pyplot.show()