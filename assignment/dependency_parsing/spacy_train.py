import spacy


with open('train.txt', 'r') as f:
    train = f.readlines()

sentence_pos = {}
words = []
pos = []
for i in train:
    line = i.split()
    if line != []:
        word = line[1]
        tag = line[3]
        words.append(word)
        pos.append(tag)
    else:
        sentence_pos[' '.join(words)] = pos
        words.clear()
        pos.clear()


nlp = spacy.load("en_core_web_sm")
doc = nlp(list(sentence_pos.keys())[10])

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
