# coding: utf-8
#kytea < test_corpus.txt > test.full -model train.mod

def cacl_acculacy(result_filename):

    result_sentences = ''
    with open(result_filename, 'r') as f:
        result_sentences = f.readlines()

    test_true_sentences = ''
    with open('test/test_true.txt', 'r') as f:
        test_true_sentences = f.readlines()

    #print(len(result_sentences))
    #print(len(test_true_sentences))

    word_count = 0
    true_count = 0

    for i in range(len(result_sentences)):
        result_sentence = result_sentences[i]
        test_true_sentence = test_true_sentences[i]

        estimated_words = result_sentence.split(' ')
        estimated_words = [word.split('/')[1] for word in estimated_words if word != '\n']
        true_words = test_true_sentence.split(' ')
        true_words = [word for word in true_words if word != '\n']

        #if len(estimated_words) != len(true_words):
        #    print(len(estimated_words))
        #    print(len(true_words))

        for j in range(len(estimated_words)):
            word_count += 1
            #print('true: %s, estimated: %s' % (true_words[j], estimated_words[j]))
            if estimated_words[j] == true_words[j]:
                true_count += 1

    print('word count: %s, true count: %s, accuracy: %.6f' % (word_count, true_count, true_count / word_count))



if __name__ == '__main__':
    cacl_acculacy('results/test_result.txt')
    cacl_acculacy('results/test_result_05.txt')
    cacl_acculacy('results/test_result_025.txt')
    cacl_acculacy('results/test_result_0125.txt')
    cacl_acculacy('results/test_result_01.txt')
    cacl_acculacy('results/test_result_001.txt')

#result_sentences = result
#for sentence in result_sentences:
#    print(sentence)
