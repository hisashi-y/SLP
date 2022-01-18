# Referred to https://www.kaggle.com/alvations/n-gram-language-model-with-nltk
import os
import requests
import io
import dill as pickle
import re
from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from nltk.lm import Laplace
from nltk.lm import KneserNeyInterpolated
from nltk.tokenize import ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

# The case of bigram.
n = 2

# Tokenizer
sent_tokenize = lambda x: re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', x)
toktok = ToktokTokenizer()
word_tokenize = word_tokenize = toktok.tokenize

# Load the training data.
if os.path.isfile('/Users/hisashi-y/python codes/SLP/assignment/train.txt'):
    with io.open('/Users/hisashi-y/python codes/SLP/assignment/train.txt', encoding='utf8') as fin:
        train = fin.read()
# Load the test data.
if os.path.isfile('/Users/hisashi-y/python codes/SLP/assignment/test.txt'):
    with io.open('/Users/hisashi-y/python codes/SLP/assignment/test.txt', encoding='utf8') as fin:
        test = fin.read()

# Tokenize the training data.
tokenized_train_text = [list(map(str.lower, word_tokenize(sent)))for sent in sent_tokenize(train)]
# Returns an iterator over text as ngrams and an iterator over text as vocabulary data.
train_data, padded_train_sents = padded_everygram_pipeline(n, tokenized_train_text)

# Tokenize the test data to use it to ckech the entropy of our LM.
tokenized_test_text = [list(map(str.lower, word_tokenize(sent)))for sent in sent_tokenize(test)]

# In this experiment we gonna use MLE as our LM pipeline.
# Laplace_model = Laplace(n)
# KneserNey_model = KneserNeyInterpolated(n)
MLE_model = MLE(n)

# Train the model.
# Laplace_model.fit(train_data, padded_train_sents)
# KneserNey_model.fit(train_data, padded_train_sents)
MLE_model.fit(train_data, padded_train_sents)


# bigram of the test data to check the entropy of LM.
bi = list(bigrams(tokenized_train_text[0]))

# Calculate the entropy.
# print(Laplace_model.entropy(bi))
# print(KneserNey_model.entropy(bi))
# print(MLE_model.entropy(bi))

# Generate a sentenec with the model.
detokenize = TreebankWordDetokenizer().detokenize

def generate_sent(model, num_words, random_seed=42):
    """
    :param model: An ngram language model from `nltk.lm.model`.
    :param num_words: Max no. of words to generate.
    :param random_seed: Seed value for random.
    """
    content = []
    for token in model.generate(num_words, random_seed=random_seed):
        if token == '<s>':
            continue
        if token == '</s>':
            break
        content.append(token)
    return detokenize(content)

# generate_sent(Laplace_model, 20, random_seed=7)

# Compare scores on correct and incorrect sentences.
print(MLE_model.score('linguistics', ['computational']))
print(MLE_model.score('visions', ['computational']))
print(Laplace_model.score('linguistics', ['computational']))
print(Laplace_model.score('visions', ['computational']))


# Saving the model
# with open('bigram_model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# Load the model
# with open('bigram_model.pkl', 'rb') as f:
#     model_loaded = pickle.load(f)

#print(len(model.vocab))
