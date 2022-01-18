import json
import train
import sys
import pandas as pd
import matplotlib.pyplot as plt

# 訓練データにおけるaccuracyを測定
# アップデートなしの場合 Accuracy is: 0.8769489723600283
# 一回重みのアップデート済みのaccuracy: Accuracy is: 0.9255846917080085

class SetIO():
    """with構文でI/Oを切り替えるためのクラス"""
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        sys.stdout = _STDLogger(out_file=self.filename)

    def __exit__(self, *args):
        sys.stdout = sys.__stdout__

class _STDLogger():
    """カスタムI/O"""
    def __init__(self, out_file='out.log'):
        self.log = open(out_file, "a+")

    def write(self, message):
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        pass

# 訓練済の重みを読み込む
with open('weights.json', 'r') as f:
    w = json.load(f)

# 訓練データを読み込む
with open('train.txt', 'r') as f:
    training_data = f.readlines()

# 訓練データを(文:ラベル)のtupleのlistにする
input_data = []

for line in training_data:
    lst = line.split()
    input_data.append((' '.join(lst[1:]), int(lst[0])))

epoch = 70
with SetIO('evaluation_result.log'):
    results = []
    for i in range(epoch):
        print('epoch {}:'.format(str(i + 1)))
        results.append(train.predict_all(w, input_data))

s = pd.Series(data = results, index = range(1, epoch + 1))
s.plot()
plt.xlabel('# of epoch')
plt.ylabel('Accuracy')
plt.show()

# 62 epoch経過した後の重みを保存
# with open('62epoch_weights.json', 'w') as f:
#     json.dump(w, f, indent=4)
