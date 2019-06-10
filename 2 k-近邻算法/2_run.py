import matplotlib.pyplot
import numpy
import pandas
import kNN

dataset, labels = kNN.file_to_array('datingTestSet2.txt')
columns = ['每年获得的飞行常客里程数', '玩视频游戏所耗时间百分比', '每周消费的冰淇淋公升数']
pandas_dataset = pandas.DataFrame(dataset, columns=columns)
print(pandas_dataset.head())

figure = matplotlib.pyplot.figure()
subplot_1 = figure.add_subplot(2, 2, 1)
subplot_1.scatter(dataset[:, 0], dataset[:, 1], 15.0 * numpy.array(labels), 15.0 * numpy.array(labels))
subplot_2 = figure.add_subplot(2, 2, 2)
subplot_2.scatter(dataset[:, 1], dataset[:, 2], 15.0 * numpy.array(labels), 15.0 * numpy.array(labels))
subplot_3 = figure.add_subplot(2, 2, 3)
subplot_3.scatter(dataset[:, 0], dataset[:, 2], 15.0 * numpy.array(labels), 15.0 * numpy.array(labels))
matplotlib.pyplot.show()