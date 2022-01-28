import json
import math
lambda_emission = 0.95
N = 1000000

# モデルの読み込み
with open('transition_model.json', 'r') as f:
    transition = json.load(f)

with open('emission_model.json', 'r') as f:
    emission = json.load(f)
# タグの読み込み
with open('possible_tags.json', 'r') as f:
    possible_tags = json.load(f)
# テストデータの読み込み
with open('test.txt', 'r') as f:
    test = f.readlines()

# 前向きアルゴリズム
def forward(line):
    best_score = {}
    best_edge = {}
    wordtags = line.split(' ')
    l = len(wordtags)
    best_score['0 <s>'] = 0 # 文頭なので<s>から始まる
    best_edge['0 <s>'] = None
    for i in range(l): # from 0 to l-1
        word, tag = map(str, wordtags[i].split('_'))
        for prev in possible_tags.keys():
            for next in possible_tags.keys():
                if (f'{i} {prev}' in best_score.keys()) and (f'{prev} {next}' in transition.keys()):
                    emission_prob = lambda_emission * emission.get(f'{next} {word}', 0) + (1 - lambda_emission) / N
                    score = best_score[f'{i} {prev}'] - math.log(transition[f'{prev} {next}']) - math.log(emission_prob)
                    if (f'{i + 1} {next}' not in best_score.keys()) or (best_score[f'{i + 1} {next}'] > score):
                        best_score[f'{i + 1} {next}'] = score
                        best_edge[f'{i + 1} {next}'] = f'{i} {prev}'
    # 最後に</s>に対して同じ操作を行う。range(l)だとfrom 0 to l-1なので</s>だけ取りこぼしが生じる
    next = '</s>'
    for prev in possible_tags.keys():
        if (f'{l} {prev}' in best_score.keys()) and (f'{prev} {next}' in transition.keys()):
            # 文末記号</s>ではemissionが起きない
            score = best_score[f'{l} {prev}'] - math.log(transition[f'{prev} {next}'])
            if (f'{l+1} {next}' not in best_score.keys()) or (best_score[f'{l+1} {next}'] > score):
                best_score[f'{l+1} {next}'] = score
                best_edge[f'{l+1} {next}'] = f'{l} {prev}'
    return best_score, best_edge

# 後ろ向きアルゴリズム
def backward(line, best_score, best_edge):
    tags = []
    wordtags = line.split(' ')
    l = len(wordtags)
    next_edge = best_edge[f'{l+1} </s>'] # 初期化
    while next_edge != "0 <s>":
        position, tag = map(str, next_edge.split())
        tags.append(tag)
        next_edge = best_edge[next_edge]
    tags.reverse()
    return tags

# for line in test[:1]:
#     best_score, best_edge = forward(line)
#     print('best_score:', best_score)
#     print('best_edge:', best_edge)
#     with open('best_score.json', 'w') as f:
#         json.dump(best_score, f, indent=4)
#     with open('best_edge.json', 'w') as f:
#         json.dump(best_edge, f, indent=4)
#     tags = backward(line, best_score, best_edge)
#     with open('tags.txt', 'w') as f:
#         json.dump(tags, f)
#     print('len', len(tags))

def evaluation(test):
    predictions = 0
    correct_predictions = 0
    for line in test:
        line = line.rstrip().lower()
        best_score, best_edge = forward(line)
        predictions_list = backward(line, best_score, best_edge)
        true_label = [i.split('_')[1] for i in line.split()]
        # print('predictons:', predictions_list)
        # print('true_label:', true_label)
        # print('# of predictions:', len(predictions_list))
        # print('# of true labels:', len(true_label))
        for i in range(len(predictions_list)):
            predictions += 1
            if true_label[i] == predictions_list[i]:
                correct_predictions += 1
    print('accuracy is:', correct_predictions/predictions)

evaluation(test)

# lowerするとaccuracy is: 0.908612754766601
# lowerしてないとaccuracy is: 0.9081744466359851
