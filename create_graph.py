# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

train_corpus_f = open('train/train_corpus.txt', 'r')
train_corpus = train_corpus_f.readlines()
train_corpus_f.close()

x = np.array([0.01, 0.1, 0.125, 0.25, 0.5, 1.0]) * len(train_corpus)
y = [0.589650, 0.817757, 0.834466, 0.878831, 0.911383, 0.934412]

plt.plot(x,y)
plt.xlabel('train data size (sentence)')
plt.ylabel('accuracy')
plt.savefig('results/accuracy.png')
plt.show()
