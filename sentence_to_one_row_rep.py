# coding: utf-8
# train-kytea -full train_corpus.txt -model train.mod -nows
# kytea < test_corpus.txt > test_result.txt -model train.mod  
import re
import random
f = open('sentence.txt')
sentences = f.readlines()
f.close()
print(len(sentences))
random.shuffle(sentences)

def convert_sentence_to_one_way(sentence):
    conv_sent = sentence
    conv_sent = re.sub('[qaZQAZ]', '1', conv_sent)
    conv_sent = re.sub('[wsxWSX]', '2', conv_sent)
    conv_sent = re.sub('[edcEDC]', '3', conv_sent)
    conv_sent = re.sub('[rfvRFV]', '4', conv_sent)
    conv_sent = re.sub('[tgbTGB]', '5', conv_sent)
    conv_sent = re.sub('[yhnYHN]', '6', conv_sent)
    conv_sent = re.sub('[ujmUJM]', '7', conv_sent)
    conv_sent = re.sub('[ikIK]', '8', conv_sent)
    conv_sent = re.sub('[olOL]', '9', conv_sent)
    conv_sent = re.sub('[pP]', '0', conv_sent)
    conv_sent = conv_sent.replace('\n', '')
    conv_sent = re.sub('\n+', '', conv_sent)

    return  conv_sent


result = open('train_corpus.txt', 'w')

for sentence in sentences[len(sentences)//4:]:
    terms = sentence.split(' ')
    terms = [convert_sentence_to_one_way(term) + '/' + term.lower() for term in terms if len(term) > 0 and term != '\n']
    terms = ' '.join(terms)
    terms = terms.replace('\n', '')
    result.write(terms + '\n')
result.close()

result = open('test_corpus.txt', 'w')
test_true = open('test_true.txt', 'w')

for sentence in sentences[:len(sentences)//4]:
    terms = sentence.split(' ')
    conv_terms = [convert_sentence_to_one_way(term)  for term in terms if len(term) > 0 and term != '\n']
    conv_terms = ' '.join(conv_terms)
    conv_terms = conv_terms.replace('\n', '')
    result.write(conv_terms + '\n')

    terms = [term.lower() for term in terms if len(term) > 0 and term != '\n']
    terms = ' '.join(terms)
    terms = terms.replace('\n', '')
    test_true.write(terms + '\n')

result.close()
test_true.close()

if __name__ == '__main__':
    print(convert_sentence_to_one_way('A keyboard with only the top row and a space bar'))
