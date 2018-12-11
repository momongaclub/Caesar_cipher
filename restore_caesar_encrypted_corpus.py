import sys


def load_encrypted_sentences(fname):
    with open(fname, 'r') as fp:
        sentences = []
        for sentence in fp:
            sentence = sentence.rstrip('\n')
            sentences.append(sentence)
    return sentences


def convert_str(s, number):
    s = ord(s)
    s = s - number%126
    if 32 <= s <= 126:
        s = chr(s)
    else:
        s = chr(s + 95)
    return s


def restore_sentences(encrypted_sentences, number):
    sentences = []
    for encrypted_sentence in encrypted_sentences: 
           words = [convert_str(s, number) for s in encrypted_sentence] # TODO insert \n
           sentence = ''.join(words)
           sentences.append(sentence)
    return sentences


def create_corpus(sentences):
    with open('corpus', 'w') as fp:
        for sentence in sentences:
            sentence = sentence + '\n'
            fp.write(sentence)


def main():
    corpus = sys.argv[1]
    number = int(sys.argv[2])
    encrypted_sentences = load_encrypted_sentences(corpus)
    sentences = restore_sentences(encrypted_sentences, number)
    create_corpus(sentences)


if __name__ == '__main__':
    main()
