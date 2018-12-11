import sys


def load_sentences(fname):
    with open(fname, 'r') as fp:
        sentences = []
        for sentence in fp:
            sentence = sentence.rstrip()
            sentences.append(sentence)
    return sentences


def convert_str(s):
    s = ord(s)
    s = s+2
    s = chr(s)

    return s



def encrypt_sentences(sentences, number):
    encrypted_sentences = []
    for sentence in sentences: 
           encrypted_words = [convert_str(s) for s in sentence] # TODO insert \n
           encrypted_sentence = ''.join(encrypted_words)
           encrypted_sentences.append(encrypted_sentence)
    return encrypted_sentences


def create_encrypted_corpus(encrypted_sentences):
    with open('encrypted_corpus', 'w') as fp:
        for encrypted_sentence in encrypted_sentences:
            encrypted_sentence = encrypted_sentence + '\n'
            fp.write(encrypted_sentence)


def main():
    corpus = sys.argv[1]
    number = sys.argv[2]
    sentences = load_sentences(corpus)
    encrypted_sentences = encrypt_sentences(sentences, number)
    create_encrypted_corpus(encrypted_sentences)


if __name__ == '__main__':
    main()
