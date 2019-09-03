def main():
    sentence = 'My name is Michelle'
    print(reverse_words(sentence))
    print(reverse_words_join(sentence))


def reverse_words(sentence: str):
    split = sentence.split()
    split.reverse()
    return split


def reverse_words_join(sentence: str):
    return ' '.join(sentence.split()[::-1])


main()
