import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

#pad_sequence方法自动将所有短句填充到最长句的长度
sentence1 = torch.randn(10, 100)  # 10 个单词，每个单词 100 维
sentence2 = torch.randn(15, 100)  # 15 个单词
sentence3 = torch.randn(8, 100)   # 8 个单词
sentence4 = torch.randn(10, 100)
sentence5 = torch.randn(17, 100)
sentence6 = torch.randn(8, 100)
sentences = [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6]
padded_sentences = pad_sequence(sentences, batch_first=True)  # [batch_size, max_len, embedding_dim]

#pack_padded_sequence方法可以避免计算填充词,来降低运算量
#**记录每句话的真实长度**
sentence_lengths = torch.tensor([len(s) for s in sentences])
# 4. **打包 PackedSequence**
packed_input = pack_padded_sequence(padded_sentences, sentence_lengths, batch_first=True, enforce_sorted=False) #enforce_sorted=False 让 PyTorch 自动处理 batch 排序（否则要手动按 length 降序排序)


lstm = nn.LSTM(input_size=100, hidden_size=20, num_layers=4, batch_first=True)

# 输入 PackedSequence，LSTM 只处理真实单词
packed_output, (h_n, c_n) = lstm(packed_input)

output, _ = pad_packed_sequence(packed_output, batch_first=True)

print(packed_output.data.shape) #不包含padding,并且将batch_size维度压缩掉了.
print(output.shape) #包含padding
print(h_n.shape)
print(c_n.shape)

