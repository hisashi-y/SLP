import json
import math

# パラメータの初期設定
lambda_1 = 0.95
lambda_2 = 0.95
V = 1000000 # 未知語を含めた語彙数
W = 0 # テストデータにおける語彙数
H = 0 # エントロピー


# bigramモデルを読み込む
with open('bigram_model.json', 'r') as f:
    bigram_model = json.load(f)

# unigramモデルを読み込む
with open('unigram_model.json', 'r') as f:
    unigram_model = json.load(f)

# テストデータを読み込む
with open('test.txt', 'r') as f:
    test = f.readlines()

# 評価と結果表示
for line in test:
    words = line.lower().split()
    words.insert(0, '<s>')
    words.append('</s>')

    for i in range(1, len(words)-1):
        unigram_prob = unigram_model.get(words[i], 0) # 未知語をkeyとしてdictにアクセスするとエラーが起きる対策
        bigram_prob = bigram_model.get(' '.join(words[i - 1: i + 1]), 0)
        P_1 = lambda_1 * unigram_prob + (1 - lambda_1)/V
        P_2 = lambda_2 * bigram_prob + (1 - lambda_2) * P_1
        H += -math.log(P_2, 2)
        W += 1

print('entropy:', 'H/W =', H/W)
