import math


def main():
    sentence = 'My name is Michelle'
    print(reverse_words(sentence))
    print(reverse_words_join(sentence))


def reverse_words(sentence: str):
    split = sentence.split()
    for index, _ in enumerate(range(math.floor(len(split)/2))):
        split[index], split[-(index+1)] = split[-(index+1)], split[index]
    #split.reverse()
    return split


def reverse_words_join(sentence: str):
    return ' '.join(sentence.split()[::-1])


main()
