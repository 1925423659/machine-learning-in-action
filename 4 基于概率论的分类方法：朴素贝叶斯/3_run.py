import bayes

dataset, labels = bayes.load_dataset()
print(dataset)
print(labels)
vocab_list = bayes.create_vocab_list(dataset)
print(vocab_list)
matrix = []
for array in dataset:
    vec = bayes.words_set_to_vec(vocab_list, array)
    matrix.append(vec)
print(matrix)
p_0_v, p_1_v, p_ab = bayes.train(matrix, labels)
print(p_0_v)
print(p_1_v)
print(p_ab)
print('<--->')
test = ['love', 'my', 'dalmation']
vec = bayes.words_set_to_vec(vocab_list, test)
classify = bayes.classify(vec, p_0_v, p_1_v, p_ab)
print(test)
print(vec)
print(classify)
print('<--->')
test = ['stupid', 'garbage']
vec = bayes.words_set_to_vec(vocab_list, test)
classify = bayes.classify(vec, p_0_v, p_1_v, p_ab)
print(test)
print(vec)
print(classify)