# 作者：Alex
# 2024/12/17 20:56

import pickle
import numpy as np

# 文件路径
DATASET_PATH = r"D:\git\gitstorege\mygits\github\deep_learniong\neural-networks-and-deep-learning\data\mnist.pkl\mnist.pkl"

def load_data():
    try:
        with open(DATASET_PATH, "rb") as f:
             data= pickle.load(f, encoding="latin1")
             a, b, c= data[0], data[1], data[2]
        return a, b, c
    except FileNotFoundError:
        print(f"错误：无法找到数据集文件 '{DATASET_PATH}'")
        return None, None, None

def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

def load_data_wrapper():
    tr_d, va_d, te_d = load_data()
    if tr_d is None:
        return None, None, None

    # 训练数据：将输入展平成 (784, 1)，标签转换为独热编码
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    train_data = list(zip(training_inputs, training_results))

    # 验证数据：将输入展平成 (784, 1)，标签保留为整数
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validate_data = list(zip(validation_inputs, va_d[1]))

    # 测试数据：将输入展平成 (784, 1)，标签保留为整数
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    testing_data = list(zip(test_inputs, te_d[1]))

    return train_data, validate_data, testing_data


training_data, validation_data, test_data = load_data_wrapper()
net = Handwritten_numbers.Network([784,30,10])

net.sgd(training_data, 30, 10, 3.0, test_data=test_data)