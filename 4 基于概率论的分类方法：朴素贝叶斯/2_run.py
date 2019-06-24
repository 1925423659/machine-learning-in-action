import bayes

dataset, labels = bayes.load_dataset()
print(dataset)
print(labels)
vocab_list = bayes.create_vocab_list(dataset)
print(vocab_list)
matrix = []
for array in dataset:
    matrix.append(bayes.words_set_to_vec(vocab_list, array))
print(matrix)
p_0_v, p_1_v, p_ab = bayes.train(matrix, labels)
print(p_ab)
print(p_0_v)
print(p_1_v)