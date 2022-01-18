import json

# 今回は n = 3のケース
n = 3

counts = {} # trigramのカウント
context_counts = {} # bigramのカウント

# 訓練データの読み込み
with open('train.txt', 'r') as f:
    train = f.readlines()

for line in train: # 行ごとに読み込み
    words = line.lower().split() # 各語のリスト、小文字に直している
    words.insert(0, '<s>') # 各行の最初と最後に挿入
    words.append('</s>')
    for i in range(n - 1, len(words)-1):
        # bigramの確率を求めるのに必要な分子(trigram)と分母(bigram)をカウントする
        trigram = ' '.join(words[i-(n - 1): i+1])
        context_word = ' '.join(trigram.split()[:-1])
        counts.setdefault(trigram, 0)
        counts[trigram] += 1
        context_counts.setdefault(context_word, 0)
        context_counts[context_word] += 1

# 各単語の出現確率を計算して{単語: 確率}の辞書として出力する
with open('trigram_model.json', 'w') as f:
    trigram_model = {}
    for trigram, count in counts.items():
        trigram_words = trigram.split()
        context_word = ' '.join(trigram_words[:-1])
        P = float(count) / context_counts[context_word] # trigram頻度 / bigram頻度
        trigram_model[trigram] = P
    json.dump(trigram_model, f, indent=4)

# bigramの際にunigramモデルも出力したのとは異なり、今回は既に作成したbigramモデルを読み込んでtestすることができる
