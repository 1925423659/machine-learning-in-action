# coding:UTF-8

import numpy

def load_dataset():
    dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    labels = [0, 1, 0, 1, 0, 1] # 1 代表侮辱性文字，0 代表正常言论
    return dataset, labels

def create_vocab_list(dataset):
    vocab_set = set([])
    for array in dataset:
        vocab_set = vocab_set | set(array)
    return list(vocab_set)

def words_set_to_vec(vocab_list, inputs):
    vec = [0] * len(vocab_list)
    for word in inputs:
        if word in vocab_list:
            index = vocab_list.index(word)
            vec[index] = 1
        else:
            print('the word: %s is not in my vocabulary' % word)
    return vec

def words_bag_to_vec(vocab_list, inputs):
    vec = [0] * len(vocab_list)
    for word in inputs:
        if word in vocab_list:
            index = vocab_list.index(word)
            vec[index] += 1
    return vec

def train(matrix, categories):
    matrix_len = len(matrix)
    array_len = len(matrix[0])
    p_abusive = sum(categories) / float(matrix_len)
    p_0_num = numpy.zeros(array_len)
    p_1_num = numpy.zeros(array_len)
    p_0_denom = 0.0
    p_1_denom = 0.0
    for i in range(matrix_len):
        if categories[i] == 1:
            p_1_num += matrix[i]
            p_1_denom += sum(matrix[i])
        else:
            p_0_num += matrix[i]
            p_0_denom += sum(matrix[i])
    p_0_vec = p_0_num / p_0_denom
    p_1_vec = p_1_num / p_1_denom
    return p_0_vec, p_1_vec, p_abusive

def classify(vec, p_0_vec, p_1_vec, p_ab):
    p_1 = sum(vec * p_1_vec) + numpy.log(p_ab)
    p_0 = sum(vec * p_0_vec) + numpy.log(1.0 - p_ab)
    if p_1 > p_0:
        return 1
    else:
        return 0

def text_parse(string):
    import re
    array = re.split(r'\W*', string)
    array = [item.lower() for item in array if len(item) > 2]
    return array

def calc_most_freq(vocab_list, full_text):
    import operator
    freq_dict = {}
    for token in vocab_list:
        freq_dict[token] = full_text.count(token)
    sorted_freq = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_freq[:30]

def local_words(feed_1, feed_0):
    import feedparser
    import random

    doc_list = []
    class_list = []
    full_text = []
    min_len = min(len(feed_1['entries']), len(feed_0['entries']))
    for i in range(min_len):
        word_list = text_parse(feed_1['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)

        word_list = text_parse(feed_0['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    
    vocab_list = create_vocab_list(doc_list)
    top_30_words = calc_most_freq(vocab_list, full_text)
    for pair_w in top_30_words:
        if pair_w[0] in vocab_list:
            vocab_list.remove(pair_w[0])
    
    train_set = range(2 * min_len)
    test_set = []
    for i in range(20):
        rand_index = int(random.uniform(0, len(train_set)))
        test_set.append(train_set[rand_index])
        del(train_set[rand_index])
    
    train_matrix = []
    train_classes = []
    for index in train_set:
        vec = words_bag_to_vec(vocab_list, doc_list[index])
        train_matrix.append(vec)
        train_classes.append(class_list[index])
    
    p_0_v, p_1_v, p_ab = train(train_matrix, train_classes)

    error_count = 0
    for index in test_set:
        vec = words_bag_to_vec(vocab_list, doc_list[index])
        classify = classify(vec, p_0_v, p_1_v, p_ab)
        if classify != class_list[index]:
            error_count += 1
    print('the error rate is: ', float(error_count) / len(test_set))
    return vocab_list, p_0_v, p_1_v

def top_words(ny, sf):
    import operator

    vocab_list, p_0_v, p_1_v = local_words(ny, sf)
    print(p_0_v)
    print(p_1_v)
    
    top_ny = []
    top_sf = []
    for i in range(len(p_0_v)):
        if p_0_v[i] > -6.0:
            top_sf.append((vocab_list[i], p_0_v[i]))
        if p_1_v[i] > -6.0:
            top_ny.append((vocab_list[i], p_1_v[i]))
    
    sorted_sf = sorted(top_sf, key=lambda pair: pair[1], reverse=True)
    print('SF**SF**SF**SF**SF**SF**SF**')
    for item in sorted_sf:
        print(item)
    
    sorted_ny = sorted(top_ny, key=lambda pair: pair[1], reverse=True)
    print('NY**NY**NY**NY**NY**NY**NY**')
    for item in sorted_ny:
        print(item)