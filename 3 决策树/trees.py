# coding:UTF-8

import math
import operator
import pickle

def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

def entropy(dataset):
    dataset_len = len(dataset)
    label_count_dict = {}
    for array in dataset:
        label = array[-1]
        label_count_dict[label] = label_count_dict.get(label, 0) + 1
    entropy = 0.0
    for key, value in label_count_dict.items():
        prob = float(value) / dataset_len
        entropy -= prob * math.log(prob, 2)
    return entropy

def split_dataset(dataset, axis, value):
    split_dataset = []
    for array in dataset:
        if array[axis] == value:
            split_array = array[:axis]
            split_array.extend(array[axis+1:])
            split_dataset.append(split_array)
    return split_dataset

def best_feature_split(dataset):
    feature_len = len(dataset[0]) - 1
    base_entropy = entropy(dataset)
    best_gain = 0.0
    best_feature = -1
    for i in range(feature_len):
        # 列数组
        feature_array = [array[i] for array in dataset]
        feature_set = set(feature_array)
        new_entropy = 0.0
        for feature in feature_set:
            # 子数据
            sub_dataset = split_dataset(dataset, i, feature)
            sub_prob = len(sub_dataset) / float(len(dataset))
            sub_entropy = entropy(sub_dataset)
            new_entropy += sub_prob * sub_entropy
        gain = base_entropy - new_entropy
        if gain > best_gain:
            best_gain = gain
            best_feature = i
    return best_feature

def majority(array):
    item_count_dict = {}
    for item in array:
        item_count_dict[item] = item_count_dict.get(item, 0) + 1
    print(item_count_dict)
    sort_item_array = sorted(item_count_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(sort_item_array)
    return sort_item_array[0][0]

def create_tree(dataset, labels):
    classes = [array[-1] for array in dataset]
    # 分类全部相同，返回分类
    if classes.count(classes[0]) == len(classes):
        return classes[0]
    # 数据中已没有特征，只有分类，返回数量最多的分类
    if len(dataset[0]) == 1:
        return majority(classes)
    best_feature = best_feature_split(dataset)
    best_feature_label = labels[best_feature]
    feature_array = [array[best_feature] for array in dataset]
    feature_set = set(feature_array)
    tree = {best_feature_label: {}}
    del(labels[best_feature])
    for feature in feature_set:
        sublabels = labels[:]
        subdataset = split_dataset(dataset, best_feature, feature)
        tree[best_feature_label][feature] = create_tree(subdataset, sublabels)
    return tree

def classify(tree, labels, array):
    key = tree.keys()[0]
    sub_tree = tree[key]
    index = labels.index(key)
    for key, value in sub_tree.items():
        if array[index] == key:
            if type(value).__name__ == 'dict':
                label = classify(sub_tree[key], labels, array)
            else:
                label = sub_tree[key]
    return label

def store_tree(tree, filename):
    f = open(filename, 'w')
    pickle.dump(tree, f)
    f.close()

def grab_tree(filename):
    f = open(filename)
    tree = pickle.load(f)
    return tree