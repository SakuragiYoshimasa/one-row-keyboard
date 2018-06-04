# coding: utf-8
from glob import glob
import re

genres = glob('./masc_500k_texts/written/*')
result = open('sentence.txt', 'w')

sentence_count = 0
for genre in genres:
    text_files = glob(genre + '/*')

    for text_file in text_files:

        with open(text_file) as f:
            texts = f.readlines()
            texts = ' '.join(texts)
            #print(texts)
            texts = re.sub(' +', ' ', texts)
            texts = re.sub('\n+', ' ', texts)
            texts = re.sub('\t+', ' ', texts)
            texts = re.sub('"', '', texts)
            texts = re.sub("'", '', texts)
            texts = re.sub("`", '', texts)
            texts = re.sub("”", '', texts)
            texts = re.sub("“", '', texts)
            texts = re.sub('(○|△|×|●|◯|□|〇|◇|◆)+', '', texts)
            texts = re.sub('[0-9０-９]+', '', texts)
            texts = re.sub('( |\u3000|\t)+', ' ', texts)
            texts = re.sub('[^a-zA-Z.]', ' ', texts)

            texts = texts.split('.')

            for text in texts:
                if(len(text) > 30):
                    result.write(text + '\n')
                    sentence_count += 1
print(sentence_count)
result.close()
