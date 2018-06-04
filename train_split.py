# coding: utf-8
import random
train_corpus_f = open('train/train_corpus.txt', 'r')
train_corpus = train_corpus_f.readlines()


splited_train = open('train/train_corpus_01.txt', 'w')
random.shuffle(train_corpus)
for sentence in train_corpus[:len(train_corpus)//10]:
    splited_train.write(sentence)
splited_train.close()

splited_train = open('train/train_corpus_001.txt', 'w')
random.shuffle(train_corpus)
for sentence in train_corpus[:len(train_corpus)//100]:
    splited_train.write(sentence)
splited_train.close()


'''
splited_train = open('train/train_corpus_05.txt', 'w')
random.shuffle(train_corpus)
for sentence in train_corpus[:len(train_corpus)//2]:
    splited_train.write(sentence)
splited_train.close()

splited_train = open('train/train_corpus_025.txt', 'w')
random.shuffle(train_corpus)
for sentence in train_corpus[:len(train_corpus)//4]:
    splited_train.write(sentence)
splited_train.close()

splited_train = open('train/train_corpus_0125.txt', 'w')
random.shuffle(train_corpus)
for sentence in train_corpus[:len(train_corpus)//8]:
    splited_train.write(sentence)
splited_train.close()
'''
