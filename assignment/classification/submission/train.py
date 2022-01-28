import json

# 訓練データを読み込む
with open('train.txt', 'r') as f:
    train = f.readlines()

def preprocessing(input): # readlinesで読み込んだデータを(文:ラベル)のリストにする
    input_data = []
    for line in input:
        lst = line.split()
        input_data.append((' '.join(lst[1:]), int(lst[0])))
    return input_data

input_data = preprocessing(train)

def create_features(x): # x = 入力データにおける各行の文
    phi = {}
    words = x.split()
    for word in words: # unigram featureを今回は使う
        phi.setdefault(word, 0)
        phi[word] += 1

    return phi

def predict_one(w, phi):
    score = 0
    # print('phi is', phi)
    for name, value in phi.items():
        if name in w:
            score += value * w[name]
    if score >= 1:
        return 1
    else:
        return -1

def update_weights(w, phi, y):
    for name, value in phi.items():
        w.setdefault(name, 0) # 訓練で得た重みをテストデータに適用して未知語が出てきた際への対処
        w[name] += value * y

def predict_all(w, input):
    count = 0
    correct_prediction = 0
    for line, label in input: # input = tupleのリスト
        phi = create_features(line)
        y_hat = predict_one(w, phi)
        count += 1
        # print('prediction:', y_hat)
        # print('correct ans:', label)
        if y_hat != label:
            update_weights(w, phi, label)
            # print('updated')
        else:
            correct_prediction += 1
    accuracy = float(correct_prediction) / count
    print('Accuracy is:', accuracy)
    return accuracy

# wの初期化
def initialize_weights(input):
    w = {}
    for line, label in input:
        words = line.split()
        for word in words:
            w[word] = 0
    return w

# 実際に動かす
w = initialize_weights(input_data)

predict_all(w, input_data)

# weightを出力する
with open('/Users/hisashi-y/python codes/SLP/assignment/classification/weights.json', 'w') as f:
    json.dump(w, f, indent=4)

# 結果: Accuracy is: 0.8769489723600283
