# 作者：Alex
# 2024/12/14 12:50
import numpy as np
import random
import matplotlib.pyplot as plt

def func(x):
    return x*13 + 3

def generate_epsilon(mean, std_dev, lower, upper):
    while True:
        value = random.gauss(mean, std_dev)
        if lower <= value <= upper:
            return value

def generate_points(times):
    points = []
    for i in range(times):
        x = random.uniform(-50,50)
        epsilon = generate_epsilon(0,0.5, -1,1)
        y = func(x) + epsilon
        point = (x,y)
        points.append(point)
    return points

def compute_loss(b,w,points):
    total_loss = 0
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        total_loss += (y-(w*x+b))**2
    return total_loss/float(len(points))

def gradient(b,w,points,learning_rate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((w * x) + b))
        w_gradient += -(2 / N) * x * (y - ((w * x) + b))
    new_b = b - (learning_rate * b_gradient)
    new_w = w - (learning_rate * w_gradient)
    return [new_b, new_w]

def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = gradient(b, w, np.array(points), learning_rate)
    return [b, w]

def plot_results(points, b, w):
    """绘制散点图和拟合直线"""
    # 分离点的 x 和 y 坐标
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]

    # 绘制散点图
    plt.scatter(x_vals, y_vals, color='blue', label='Data Points')

    # 绘制拟合直线
    x_line = np.linspace(min(x_vals), max(x_vals), 1000)  # 在 x 范围内生成平滑曲线
    y_line = w * x_line + b
    plt.plot(x_line, y_line, color='red', label=f'Fitted Line: y = {w:.2f}x + {b:.2f}')

    # 图形标题和标签
    plt.title("Linear Regression: Data and Fitted Line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    initial_b = 0
    initial_w = 0
    random.seed(27)
    learning_rate = 0.001
    num_iterations = 10000
    points = generate_points(1000)
    print("Starting gradient descent at b = {0}, w = {1}, loss = {2}"
          .format(initial_b, initial_w, compute_loss(initial_b, initial_w, points)))
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, w = {2}, loss = {3}"
          .format(num_iterations, b, w, compute_loss(b, w, points)))
    plot_results(points, b, w)

if __name__ == "__main__":
    main()





"""
import numpy as np

# y = wx + b
def compute_error_for_line_given_points(b, w, points):
    totalLoss = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalLoss += (y - (w * x + b)) ** 2
    return totalLoss / len(points)

def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = len(points)
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((w_current * x) + b_current))
        w_gradient += -(2 / N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = w_current - (learningRate * w_gradient)
    return [new_b, new_m]
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]

def run():
    points = np.genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_w = 0  # initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, m = {1}, loss = {2}"
          .format(initial_b, initial_w, compute_error_for_line_given_points(initial_b, initial_w, points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, loss = {3}"
          .format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))

"""