import LogRegress

data_array, label_array = LogRegress.load_dataset()
weights = LogRegress.grad_ascent(data_array, label_array)
LogRegress.plot_best_fit(weights.getA())