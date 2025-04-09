# 作者：Alex
# 2025/4/5 16:41
def int_to_roman(num: int) -> str:
    a, b, c, d = num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10
    k = 'M' * a

    def num_to_num(ori_num, one, five, ten):
        if ori_num == 4:
            result = one + five
        elif ori_num == 9:
            result = one + ten
        elif ori_num >= 5:
            result = five + one * (ori_num - 5)
        else:
            result = one * ori_num
        return result

    return k + num_to_num(b, 'C', 'D', 'M') + num_to_num(c, 'X', 'L', 'C') + num_to_num(d, 'I', 'V', 'X')

print(int_to_roman(3491))