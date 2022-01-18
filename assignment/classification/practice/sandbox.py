import torch
import torch.nn as nn
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split

BATCH_SIZE = 16
NUM_EPOCHS = 1
EVAL_STEPS = 1000
WARMUP_STEPS = int(len(train) // BATCH_SIZE * 0.1)
OUTPUT_PATH = "./sbert_stair"

# model = SentenceTransformer('whaleloops/phrase-bert')
#
# # 訓練データの読み込み
# def load_data(path):
#     with open(path, 'r') as f:
#         data = f.readlines()
#     return data #list of sentences
#
# data = load_data('train.txt')
# data = data[:100] # 一旦数を絞って扱う
#
# # データを(文:ラベル)のtupleのlistにする
# for line in data:
#     lst = line.split()
#
#     input_data.append((' '.join(lst[1:]), int(lst[0])))
#
# # 読み込んだデータの7.5割で学習し残りでテストする
# train_data, test_data = train_test_split(input_data, test_size = 0.25)

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.classifier = nn.Sequential(
        nn.Linear(768, 2),
        nn.ReLU(inplace = True)
        )

    def forward(self, x):
        output = self.classifier(x)
        return output
