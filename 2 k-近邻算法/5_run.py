import kNN
import numpy

result_array = ['not at all', 'in small doses', 'in large doses']
dataset, labels = kNN.file_to_array('datingTestSet2.txt')
normalize_dataset, min_array, max_array, range_array = kNN.normalize(dataset)

fly_input = float(input('每年获得的飞行常客里程数 >>>'))
game_input = float(input('玩视频游戏所耗时间百分比 >>>'))
icecream_input = float(input('每周消费的冰淇淋公升数 >>>'))
input_array = numpy.array([fly_input, game_input, icecream_input])
normalize_input_array = (input_array - min_array) / range_array
label = kNN.classify(normalize_dataset, labels, normalize_input_array, 5)
print('label %s' % result_array[label - 1])