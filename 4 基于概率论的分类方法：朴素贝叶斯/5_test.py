import bayes
import random

doc_list = []
class_list = []
full_text = []

for i in range(1, 26):
    text = open('email/spam/%d.txt' % i).read()
    word_list = bayes.text_parse(text)
    doc_list.append(word_list)
    full_text.extend(word_list)
    class_list.append(1)
    
    text = open('email/ham/%d.txt' % i).read()
    word_list = bayes.text_parse(text)
    doc_list.append(word_list)
    full_text.extend(word_list)
    class_list.append(0)

vocab_list = bayes.create_vocab_list(doc_list)

train_set = range(50)
test_set = []
for i in range(10):
    rand_index = int(random.uniform(0, len(train_set)))
    test_set.append(train_set[rand_index])
    del(train_set[rand_index])
train_matrix = []
train_classes = []
for index in train_set:
    vec = bayes.words_set_to_vec(vocab_list, doc_list[index])
    train_matrix.append(vec)
    train_classes.append(class_list[index])

p_0_v, p_1_v, p_ab = bayes.train(train_matrix, train_classes)

error_count = 0
for index in test_set:
    vec = bayes.words_set_to_vec(vocab_list, doc_list[index])
    classify = bayes.classify(vec, p_0_v, p_1_v, p_ab)
    if classify != class_list[index]:
        error_count += 1
print('the error rate is: ', float(error_count) / len(test_set))