import json
import math
from decimal import Decimal

n = 4

lambda_1 = 0.95
lambda_2 = 0.95
V = 1000000 # 未知語を含めた語彙数

with open('4gram_model.json', 'r') as f:
    fourgram_model = json.load(f)

with open('trigram_model.json', 'r') as f:
    trigram_model = json.load(f)

correct_sentence = 'Natural language understanding is sometimes referred to as an AI-complete problem'
incorrect_sentence = 'Natural language understanding are sometimes referred to as a AI-complete problems' # 単複の一致をずらした

# 評価と結果表示
def get_score(n, sentence, model1, model2): # model1 = ngram model, model2 = n-1 gram model
    words = sentence.lower().split()
    score = 1
    for i in range(n - 1, len(words)-1):
        n_minusone_prob = model2.get(' '.join(words[i - (n - 1): i]), 0)
        ngram_prob = model1.get(' '.join(words[i - (n - 1): i + 1]), 0)
        P_1 = lambda_1 * n_minusone_prob + (1 - lambda_1)/V
        P_2 = lambda_2 * ngram_prob + (1 - lambda_2) * P_1
        score *= P_2
    return score


print(get_score(4, correct_sentence, fourgram_model, trigram_model))
print(get_score(4, incorrect_sentence, fourgram_model, trigram_model)) # incorrect sentenceの方が圧倒的に小さくなった
