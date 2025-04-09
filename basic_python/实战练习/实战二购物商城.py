# 作者：Alex
# 2024/9/28 上午6:58
import random
import json
import re
import tkinter as tk

shopping_cart = {}
product_list = {}
PRODUCT_FILES = {
    '1': 'slave.jsonl',
    '2': 'women_product.jsonl',
    '3': 'BDSM_gear.jsonl',
    '4': 'large_item_product.jsonl',
    '5': 'service_product.jsonl',
    '6': 'slave_Marketplace.jsonl'
}


def login_main():

def main_customer(account):

def main_merchant(account):


def generate_unique_product_id(filename):
    try:
        # 检查文件是否存在，如果不存在则自动创建文件
        with open(filename, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        # 如果文件不存在，创建空文件
        with open(filename, 'w', encoding='utf-8') as f:
            pass

    while True:
        product_id = f"{random.randint(1, 99999999):08}"

        # 打开文件逐行检查是否有相同的ID
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                product = json.loads(line.strip())
                if product.get('product_id') == product_id:
                    break  # 如果找到相同ID，则重新生成
            else:
                # 如果没有相同的ID，返回该ID
                return product_id


def add_product_to_product_list(product_name, product_price, available_stock,account, product_list_address):
    product_id = generate_unique_product_id(product_list_address)
    new_product = {'product_id': product_id,
                   'product_name': product_name,
                   'product_price': product_price,
                   'available_stock': available_stock,
                   'merchant': account,
                   }
    with open(product_list_address, 'a', encoding='utf-8') as f:
        json.dump(new_product, f, ensure_ascii=False)
        f.write('\n')
    print(f'{product_name}已经成功上架')


def add_product(account):
    while True:
        userinput = input('请输入添加的商品名称，价格，库存（用英文逗号分隔）：')
        if userinput == '退出':
            return 'main'
        parts = re.split(r'[，,]', userinput)
        if len(parts) != 3:
            print("输入格式错误！请确保输入格式为：名称,价格,库存")
            continue
        product_name, product_price, available_stock = parts
        try:
            product_price = float(product_price)
        except ValueError:
            print('价格必须为数字')
            continue
        try:
            available_stock = int(available_stock)
            if available_stock <= 0:
                print('库存必须为正整数')
                continue
        except ValueError:
            print('库存必须为正整数')
            continue
        else:
            break
    while True:
        type_input = input(
            '1.315\n2.女性用品\n3.调教用具\n4.大件物品\n5.服务\n6.135\n7.返回\n8.退出到主界面\n请选择商品类型:')
        if type_input in PRODUCT_FILES:
            product_list_address = PRODUCT_FILES[type_input]
            break
        elif type_input == '7':
            return 'add'
        elif type_input == '8':
            return 'main_merchant'
        else:
            print("无效的选择")
            continue
    add_product_to_product_list(product_name, product_price, available_stock,account, product_list_address)
    return 'main_merchant'
def controller():
    page = 'login_main'
    account = None
    while True:
        if page == 'login_main':
            page,account = login_main()
        elif page == 'main_merchant':
            page,account = main_merchant(account)
        elif page == 'main_customer':
            page,account = main_customer(account)
        elif page == 'add_product':
            page,account = add_product(account)
        elif page == 'quit':
            break

if __name__ == '__main__':
    controller()
