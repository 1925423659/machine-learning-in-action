import bayes

dataset, labels =bayes.load_dataset()

vocab_list = bayes.create_vocab_list(dataset)
print(vocab_list)
vec = bayes.words_set_to_vec(vocab_list, dataset[0])
print(vec)
vec = bayes.words_set_to_vec(vocab_list, dataset[3])
print(vec)