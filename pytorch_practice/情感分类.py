import torch
import torch.optim as optim
import torch.nn.init as init
import datasets
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_scheduler
import torch.nn as nn


batch_size = 32
epochs = 100
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
save_dir = "../data/classification/Sentiment_Classification/"


# 1.datasets
def collate_fn(batch):
    # 处理每个batch，返回张量格式
    input_ids = torch.tensor([x['input_ids'] for x in batch])
    attention_mask = torch.tensor([x['attention_mask'] for x in batch])
    labels = torch.tensor([x['label'] for x in batch])
    return {'input_ids': input_ids, 'attention_mask': attention_mask, 'label': labels}

download_config = datasets.DownloadConfig(cache_dir='../data/classification/Sentiment_Classification/')
dataset = datasets.load_dataset('stanfordnlp/imdb', download_config=download_config)


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
def tokenize_function(examples):
    return tokenizer(examples['text'], padding=True, truncation=True, max_length=512)
tokenized_train_datasets = dataset['train'].map(tokenize_function, batched=True)
tokenized_test_datasets = dataset['test'].map(tokenize_function, batched=True)
print(tokenized_train_datasets)

train_dataloader = DataLoader(tokenized_train_datasets, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
test_dataloader = DataLoader(tokenized_test_datasets, batch_size=batch_size, shuffle=False, collate_fn=collate_fn)

# 2. model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2,ignore_mismatched_sizes=True)


# 3. init classifier 头
init.xavier_uniform_(model.classifier.weight)
init.zeros_(model.classifier.bias)
model.dropout = nn.Dropout(0.3)
for param in model.bert.embeddings.parameters():  # 冻结 BERT embedding 层
    param.requires_grad = False
for param in model.bert.encoder.layer[:7].parameters():  # 只训练最后 4 层
    param.requires_grad = False

# 4.optimizer
optimizer_grouped_parameters = [
    {"params": model.bert.encoder.layer[8:].parameters(), "lr": 1e-3},  # 训练最后 4 层
    {"params": model.classifier.parameters(), "lr": 1e-3},  # 分类器的学习率更大
]
optimizer = optim.AdamW(optimizer_grouped_parameters)
num_training_steps = epochs * len(train_dataloader)
lr_scheduler = get_scheduler("linear", optimizer=optimizer, num_warmup_steps=0.1 * num_training_steps, num_training_steps=num_training_steps)
scaler = torch.amp.GradScaler('cuda')    # 创建一个梯度缩放器，用于混合精度训练，防止 float16 下梯度过小导致更新失败


model.to(device)
print(model)

def main():
    model.train()  # 训练模式
    for epoch in range(epochs):
        running_loss = 0.0
        correct_preds = 0
        total_preds = 0
        for batch in train_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)

            # 前向传播
            optimizer.zero_grad()
            with torch.amp.autocast(device_type='cuda'):  #自动精度
                outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                logits = outputs.logits

            scaler.scale(loss).backward()   # 先对 loss 进行缩放，防止精度过低造成梯度为 0（尤其是在 fp16 下）
            scaler.step(optimizer)  # 使用缩放后的梯度进行参数更新（step() 里自动解缩放）
            scaler.update()     # 更新缩放器的缩放因子，动态调整以避免梯度 underflow

            running_loss += loss.item()

            # 计算准确率
            _, preds = torch.max(logits, dim=1)
            correct_preds += (preds == labels).sum().item()
            total_preds += labels.size(0)

        lr_scheduler.step()
        epoch_loss = running_loss / len(train_dataloader)
        epoch_accuracy = correct_preds / total_preds * 100
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_accuracy:.2f}%")
        if epoch % 5 == 0:
            # 验证阶段
            model.eval()  # 设置模型为评估模式
            val_loss = 0.0
            correct_preds = 0
            total_preds = 0

            with torch.no_grad(), torch.amp.autocast(device_type='cuda'):  # 禁用梯度计算
                for batch in test_dataloader:
                    input_ids = batch['input_ids'].to(device)
                    attention_mask = batch['attention_mask'].to(device)
                    labels = batch['label'].to(device)

                    # 前向传播
                    outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                    loss = outputs.loss
                    logits = outputs.logits

                    val_loss += loss.item()

                    # 计算准确率
                    _, preds = torch.max(logits, dim=1)
                    correct_preds += (preds == labels).sum().item()
                    total_preds += labels.size(0)

            val_loss = val_loss / len(test_dataloader)
            val_accuracy = correct_preds / total_preds * 100
            print(f"Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_accuracy:.2f}%")


            # 保存模型
            torch.save(model.state_dict(), f"{save_dir}model_epoch_{epoch + 1}.pth")
            model.train()

if __name__ == '__main__':
    main()

"""
BertForSequenceClassification(
  (bert): BertModel(
    (embeddings): BertEmbeddings(
      (word_embeddings): Embedding(30522, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (token_type_embeddings): Embedding(2, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (encoder): BertEncoder(
      (layer): ModuleList(
        (0-11): 12 x BertLayer(
          (attention): BertAttention(
            (self): BertSdpaSelfAttention(
              (query): Linear(in_features=768, out_features=768, bias=True)
              (key): Linear(in_features=768, out_features=768, bias=True)
              (value): Linear(in_features=768, out_features=768, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): BertSelfOutput(
              (dense): Linear(in_features=768, out_features=768, bias=True)
              (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): BertIntermediate(
            (dense): Linear(in_features=768, out_features=3072, bias=True)
            (intermediate_act_fn): GELUActivation()
          )
          (output): BertOutput(
            (dense): Linear(in_features=3072, out_features=768, bias=True)
            (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
      )
    )
    (pooler): BertPooler(
      (dense): Linear(in_features=768, out_features=768, bias=True)
      (activation): Tanh()
    )
  )
  (dropout): Dropout(p=0.1, inplace=False)
  (classifier): Linear(in_features=768, out_features=2, bias=True)
)
"""
