import numpy
import LogRegress

data_array, label_array = LogRegress.load_dataset()
weights = LogRegress.stoc_grad_ascent_1(numpy.array(data_array), numpy.array(label_array))
LogRegress.plot_best_fit(weights)