import json
import math

n = 4

# パラメータの初期設定
lambda_1 = 0.95
lambda_2 = 0.95
V = 1000000 # 未知語を含めた語彙数
W = 0 # テストデータにおける語彙数
H = 0 # エントロピー

d = 0.75

# with open('trigram_model.json', 'r') as f:
#     trigram_model = json.load(f)
#
# with open('4gram_model.json', 'r') as f:
#     fourgram_model = json.load(f)
#
# with open('test.txt', 'r') as f:
#     test = f.readlines()
#
# # 評価と結果表示
# for line in test:
#     words = line.lower().split()
#     words.insert(0, '<s>')
#     words.append('</s>')
#
#     for i in range(1, len(words)-1):
#         trigram_prob = trigram_model.get(' '.join(words[i - (n - 1): i]), 0)
#         fourgram_prob = fourgram_model.get(' '.join(words[i - (n - 1): i + 1]), 0)
#         P_1 = lambda_1 * trigram_prob + (1 - lambda_1)/V
#         P_2 = lambda_2 * fourgram_prob + (1 - lambda_2) * P_1
#         H += -math.log(P_2, 2)
#         W += 1
#
# print('entropy:', 'H/W =', H/W)

def KNSmoothing(ngram, n, counts, d):
    # count = unigram, bigram,...ngramのカウントの辞書のリスト
    if n == 1:
        lambda_epsilon = 100
        return counts[n-1].get(ngram, 0) / sum(counts[n-1].values()) +
