import json
import train

# 訓練済の重みを読み込む
with open('weights.json', 'r') as f:
    w = json.load(f)

# テストデータを読み込む
with open('test.txt', 'r') as f:
    test = f.readlines()

input_data = train.preprocessing(test)

def test_predict_all(w, input): # train.predict_allは各predictionごとに重みの更新をしてしまっていたが、今回はtestなので重みの更新を行わない。
    count = 0
    correct_prediction = 0
    for line, label in input: # input = tupleのリスト
        phi = train.create_features(line)
        y_hat = train.predict_one(w, phi)
        count += 1
        if y_hat == label:
            correct_prediction += 1
    accuracy = float(correct_prediction) / count
    print('Accuracy is:', accuracy)
    return accuracy

test_predict_all(w, input_data)

# 結果: Accuracy is: 0.9029401346085725
