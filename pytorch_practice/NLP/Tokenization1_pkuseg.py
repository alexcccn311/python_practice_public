import pkuseg

input_file = r'D:\git\gitstorege\data\knowledge_base\txt\如何训练厕奴\如何训练厕奴简体.txt'
output_file = r'test_data\1.txt'
model_name = 'web'
thread=20

seg = pkuseg.pkuseg(
    model_name= model_name
)
# text = seg.cut('我爱北京天安门')
# print(text)

if __name__ == '__main__':
    pkuseg.test(input_file=input_file,output_file= output_file,model_name=model_name,postag=True,nthread=thread)