# Sample code.
from ngram_model import Ngram

ngram = Ngram(input_file='train_processed.txt', N=2, smoothing='kneser-nay')
ngram.train()
ngram.ppl(input_file='train_processed.txt')
generated_list = ngram.generate(window=5, mode='sample', temprature=1.1, max_word=30, delta=0.5)

print("生成結果")
for words, log_prob in generated_list:
    print(log_prob, "".join(words[3::]))
