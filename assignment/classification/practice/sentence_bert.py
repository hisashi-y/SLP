# phraseBERTの仮想環境で起動
from sentence_transformers import SentenceTransformer
import numpy as np
import torch
from torch import nn
from sklearn.model_selection import train_test_split # 訓練データの分割

model = SentenceTransformer('whaleloops/phrase-bert')

# 訓練データの読み込み
def load_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data #list of sentences

data = load_data('train.txt')
data = data[:100]

# データを(文:ラベル)のtupleのlistにする
input_data = []
for line in data:
    lst = line.split()
    input_data.append((' '.join(lst[1:]), int(lst[0])))

# 読み込んだデータの7.5割で学習し残りでテストする
train_data, test_data = train_test_split(input_data, test_size = 0.25)

w = np.zeros(768)



# weightを出力する
# with open('/Users/hisashi-y/python codes/SLP/assignment/classification/weights.json', 'w') as f:
#     json.dump(w, f, indent=4)
