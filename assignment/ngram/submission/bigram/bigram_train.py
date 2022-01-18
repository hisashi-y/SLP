import json

n = 2

counts = {}
context_counts = {}

# 訓練データの読み込み
with open('train.txt', 'r') as f:
    train = f.readlines()

for line in train: # 行ごとに読み込み
    words = line.lower().split() # 各語のリスト、小文字に直している
    words.insert(0, '<s>') # 各行の最初と最後に挿入
    words.append('</s>')
    for i in range(n - 1, len(words)-1):
        # bigramの確率を求めるのに必要な分子(bigram)と分母(unigram)をカウントする
        bigram = ' '.join(words[i-(n - 1): i+1])
        context_word = ' '.join(bigram.split()[:-1])

        counts.setdefault(bigram, 0)
        counts[bigram] += 1
        context_counts.setdefault(context_word, 0)
        context_counts[context_word] += 1

# 各単語の出現確率を計算して{単語: 確率}の辞書として出力する
with open('bigram_model.json', 'w') as f:
    bigram_model = {}
    for bigram, count in counts.items():
        bigram_words = bigram.split()
        context_word = ' '.join(bigram_words[:-1])
        P = float(count) / context_counts[context_word] # bigram頻度 / unigram頻度
        bigram_model[bigram] = P
    json.dump(bigram_model, f, indent=4)

# bigramのテスト時に必要となるのでunigramモデルも出力する
with open('unigram_model.json', 'w') as f:
    unigram_model = {}
    total_count = sum(context_counts.values())
    for unigram, count in context_counts.items():
        P = float(count) / total_count
        unigram_model[unigram] = P
    json.dump(unigram_model, f, indent=4)
