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

correct_sentence1 = 'Natural language understanding is sometimes referred to as an AI-complete problem'
incorrect_sentence1 = 'Natural language understanding are sometimes referred to as a AI-complete problems' # 単複の一致をずらした

correct_sentence2 = 'The Association for Computational Linguistics defines the latter as focusing on the theoretical aspects of NLP .'
incorrect_sentence2 = 'The Association for Computational Vision defining the latter as focusing in the theoretical aspects of NLP .' # 単語の変更、前置詞の変更

correct_sentence3 = 'Little further research in machine translation was conducted until the late 1980s , when the first statistical machine translation systems were developed .'
incorrect_sentence3 = 'Little further research in machine translation were conducted until the late 1980s , where the first statistical machine translation systems was developed .'

correct_sentences = [correct_sentence1, correct_sentence2, correct_sentence3]
incorrect_sentences = [incorrect_sentence1, incorrect_sentence2, incorrect_sentence3]

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

for i, j in zip(correct_sentences, incorrect_sentences):
    print('Correct sentence:', i)
    print('Score of this correct sentence:', get_score(4, i, fourgram_model, trigram_model))
    print('Incorrect sentence:', j)
    print('Score of this incorrect sentence:', get_score(4, j, fourgram_model, trigram_model))


# print(get_score(4, correct_sentence, fourgram_model, trigram_model))
# print(get_score(4, incorrect_sentence, fourgram_model, trigram_model))
