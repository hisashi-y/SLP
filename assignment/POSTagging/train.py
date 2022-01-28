import json



# 訓練データの読み込み
with open('train.txt', 'r') as f:
    train = f.readlines()

emit = {}
transition = {}
context = {}
possible_tags = {}

for line in train:
    line = line.rstrip()
    line = line.lower()
    previous = '<s>' # 文頭のPOSタグとして初期化
    context.setdefault(previous, 0)
    context[previous] += 1
    wordtags = line.split(' ')
    for wordtag in wordtags:
        word, tag = wordtag.split('_')
        possible_tags[tag] = 1 # テストの時のために使用可能なタグをカウントしておく
        # 遷移を数える
        transition_sequence = previous + ' ' + tag
        transition.setdefault(transition_sequence, 0)
        transition[transition_sequence] += 1
        # 文脈を数える
        context.setdefault(tag, 0)
        context[tag] += 1
        # 生成を数える
        emit_sequence = tag + ' ' + word
        emit.setdefault(emit_sequence, 0)
        emit[emit_sequence] += 1

        previous = tag
    # 文末における遷移
    eos_transition = previous +' '+ '</s>'
    transition.setdefault(eos_transition, 0)
    transition[eos_transition] += 1

transition_model = {}
emission_model = {}

# 遷移確率を出力
for key, value in transition.items():
    previous, current = map(str, key.split())
    prob = float(value) / context[previous]
    print("Transition:", key, prob)
    transition_model[key] = prob


# 生成確率を出力
for key, value in emit.items():
    previous, current = map(str, key.split())
    prob = float(value) / context[previous]
    print("Emmission:", key, prob)
    emission_model[key] = prob

with open('transition_model.json', 'w') as f:
    json.dump(transition_model, f, indent=4)

with open('emission_model.json', 'w') as f:
    json.dump(emission_model, f, indent=4)

# <s>, </s>もタグとして考慮
possible_tags['<s>'] = 1
possible_tags['</s>'] = 1

with open('possible_tags.json', 'w') as f:
    json.dump(possible_tags, f, indent=4)
