import LogRegress

data_array, label_array = LogRegress.load_dataset()
weights = LogRegress.grad_ascent(data_array, label_array)
print(weights)