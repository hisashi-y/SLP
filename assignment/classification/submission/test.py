import json
import train

# 訓練済の重みを読み込む
with open('weights.json', 'r') as f:
    w = json.load(f)

# テストデータを読み込む
with open('test.txt', 'r') as f:
    test = f.readlines()

input_data = train.preprocessing(test)
train.predict_all(w, input_data)

# 結果: Accuracy is: 0.9029401346085725
