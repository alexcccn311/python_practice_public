# 作者：Alex
# 2024/12/17 20:30
import pickle
import numpy as np

# 文件的绝对路径
file_path = r"D:\git\gitstorege\mygits\github\deep_learniong\neural-networks-and-deep-learning\data\mnist.pkl\mnist.pkl"

# 加载 .pkl 文件
def load_pkl_file(file_path):
    """
    加载 .pkl 文件
    """
    try:
        with open(file_path, "rb") as f:  # 以二进制读取模式打开文件
            data = pickle.load(f, encoding='latin1')
        return data
    except Exception as e:
        print(f"文件加载失败: {e}")
        return None

# 分析数据结构
def analyze_structure(data, level=0):
    """
    递归分析数据结构，显示各部分的类型和长度
    """
    indent = "  " * level  # 缩进显示层级关系

    if isinstance(data, list):
        print(f"{indent}类型: {type(data)}, 长度: {len(data)}")
        if len(data) > 0:
            print(f"{indent}第一个元素:")
            analyze_structure(data[0], level + 1)

    elif isinstance(data, tuple):
        print(f"{indent}类型: {type(data)}, 元素数量: {len(data)}")
        for i, item in enumerate(data):
            print(f"{indent}第 {i+1} 个元素:")
            analyze_structure(item, level + 1)

    elif isinstance(data, dict):
        print(f"{indent}类型: {type(data)}, 键的数量: {len(data)}")
        for key, value in data.items():
            print(f"{indent}键: {key} -> 值类型: {type(value)}")
            analyze_structure(value, level + 1)
            break  # 只显示第一个键值对，防止数据过多

    elif isinstance(data, np.ndarray):
        print(f"{indent}类型: {type(data)}, 形状: {data.shape}, 数据类型: {data.dtype}")

    else:
        print(f"{indent}类型: {type(data)}, 值: {data}")

# 主程序
if __name__ == "__main__":
    data = load_pkl_file(file_path)

    if data is not None:
        print("开始分析数据结构...\n")
        analyze_structure(data)
    else:
        print("无法加载数据文件")
