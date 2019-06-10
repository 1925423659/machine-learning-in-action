# 科学计算模块
import numpy
# 运算符模块，用于排序操作
import operator

def create_dataset():
    dataset = numpy.array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return dataset, labels

def classify(dataset, labels, input, k):
    dataset_size = dataset.shape[0]
    # 将输入数据转换成二维数组，长度与 dataset 一致
    input_array = numpy.tile(input, (dataset_size, 1))

    # 计算已知类别数据集中的点与当前点之间的距离
    diff_array = input_array - dataset
    sq_diff_array = diff_array ** 2
    sq_distance_array = sq_diff_array.sum(axis=1)
    distance_array = sq_distance_array ** 0.5

    # 按照距离递增次序排序
    sort_distance_index_array = distance_array.argsort()

    # 选取与当前点距离最小的 k 个点
    # 确定前 k 个点所在类别的出现频率
    label_count_dict = {}
    for i in range(k):
        index = sort_distance_index_array[i]
        label = labels[index]
        label_count_dict[label] = label_count_dict.get(label, 0) + 1
    
    # 返回前 k 个点出现频率最高的类别作为当前点的预测分类
    sort_label_count_array = sorted(label_count_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sort_label_count_array[0][0]

def file_to_array(filename):
    f = open(filename)
    line_array = f.readlines()
    line_len = len(line_array)
    dataset = numpy.zeros((line_len, 3))
    labels = []
    for i in range(line_len):
        line = line_array[i]
        # 截去回车字符
        line = line.strip()
        # 字符串分割成数组
        line_data = line.split('\t')
        dataset[i, :] = line_data[:3]
        label = line_data[-1]
        labels.append(int(label))
    return dataset, labels

def image_to_array(filename):
    array = numpy.zeros(1024)
    f = open(filename)
    for i in range(32):
        line = f.readline()
        for j in range(32):
            array[32 * i + j] = int(line[j])
    return array

def normalize(dataset):
    dataset_len = dataset.shape[0]
    # 从列中选取最小值和最大值
    min_array = dataset.min(0)
    max_array = dataset.max(0)
    range_array = max_array - min_array
    min_dataset = numpy.tile(min_array, (dataset_len, 1))
    range_dataset = numpy.tile(range_array, (dataset_len, 1))
    normalize_dataset = (dataset - min_dataset) / range_dataset
    return normalize_dataset, min_array, max_array, range_array
