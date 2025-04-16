import pickle
import random
import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
    return np.maximum(0, x)

def relu_prime(x):
    return np.where(x > 0, 1, 0)

def tanh(x):
    return np.tanh(x)

class Network(object):
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases= [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]

    def feedforward(self,x):
        for b,w in zip(self.biases,self.weights):
            x= sigmoid(np.dot(w,x) + b)
        return x

    def sgd(self,training_data,epochs,batch_size,learning_rate, test_data=None):
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for epoch in range(epochs):
            random.shuffle(training_data)
            mini_batches= [training_data[k:k+batch_size] for k in range(0,n,batch_size)]  #mini_batches是拆分后的一部分数据集
            for mini_batch in mini_batches: #mini_batch是一个由x(1*784维向量)和y(正确数字结果)组成的列表
                self.update_mini_batch(mini_batch,learning_rate)
            if test_data:
                print("Epoch{0}:{1}/{2}".format(epoch,self.evaluate(test_data),n_test))
            else:
                print("Epoch{0} complete".format(epoch))

    def update_mini_batch(self,mini_batch,learning_rate):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:     #mini_batch是一个由x(1*784维向量)和y(正确数字结果)组成的列表
            delta_nabla_b, delta_nabla_w = self.backprop(x,y)
            nabla_b = [nb+dnb for nb,dnb in zip(nabla_b,delta_nabla_b)]
            nabla_w = [nw+dnw for nw,dnw in zip(nabla_w,delta_nabla_w)]
        self.weights = [w -(learning_rate/len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b -(learning_rate/len(mini_batch)) * nb for b,nb in zip(self.biases,nabla_b)]

    def backprop(self,x,y):
        delta_nabla_b = [np.zeros(b.shape) for b in self.biases]
        delta_nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs = []
        for b , w in zip(self.biases,self.weights):
            z = np.dot(w,activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        cost = self.cost_derivative(activations[-1],y)
        delta =  cost * sigmoid_prime(zs[-1])
        delta_nabla_b[-1] = delta
        delta_nabla_w[-1] = np.dot(delta,activations[-2].transpose())

        for l in range(2,self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            f_weight=self.weights[-l+1].transpose()
            delta = np.dot(f_weight,delta) * sp
            delta_nabla_b[-l] = delta
            delta_nabla_w[-l] = np.dot(delta,activations[-l-1].transpose())
        return delta_nabla_b, delta_nabla_w

    def evaluate(self,test_data):
        test_results = [(np.argmax(self.feedforward(x)),y) for (x,y) in test_data]
        return sum(int(x == y) for  (x,y) in test_results)

    def cost_derivative(self,output_activations,y):
        return output_activations-y

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

if __name__ == '__main__':
    DATASET_PATH = r"D:\git\gitstorege\mygits\github\deep_learniong\neural-networks-and-deep-learning\data\mnist.pkl\mnist.pkl"
    training_data, validation_data, test_data = load_data_wrapper()
    net = Network([784,100, 30, 10])

    net.sgd(training_data, 30, 10, 3.0, test_data=test_data)
