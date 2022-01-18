import json

n = 4

# 訓練データの読み込み
with open('train.txt', 'r') as f:
    train = f.readlines()

def ngram_training(train, n):
    counts = {} # ngramのカウント
    context_counts = {} # n-1gramのカウント
    for line in train: # 行ごとに読み込み
        words = line.lower().split() # 各語のリスト、小文字に直している
        words.insert(0, '<s>') # 各行の最初と最後に挿入
        words.append('</s>')
        for i in range(n - 1, len(words)-1):
            ngram = ' '.join(words[i-(n - 1): i+1])
            context_word = ' '.join(ngram.split()[:-1])
            counts.setdefault(ngram, 0)
            counts[ngram] += 1
            context_counts.setdefault(context_word, 0)
            context_counts[context_word] += 1
    return counts, context_counts

counts, context_counts = ngram_training(train, n)

# 各単語の出現確率を計算して{単語: 確率}の辞書として出力する
with open(f'{n}gram_model.json', 'w') as f:
    ngram_model = {}
    for ngram, count in counts.items():
        ngram_words = ngram.split()
        context_word = ' '.join(ngram_words[:-1])
        P = float(count) / context_counts[context_word]
        ngram_model[ngram] = P
    json.dump(ngram_model, f, indent=4)
