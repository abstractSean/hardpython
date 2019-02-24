import operator
import os
import re
import sys

from itertools import groupby
from pprint import pprint as pp

def main():
    file_source = os.getcwd() + "\\" + sys.argv[1]

    with open(file_source) as f:
        lines = [line for line in f]
    
    lines_split = [re.split('\W+',words) for words in lines]
    words = [word for split in lines_split for word in split if word != '']
    words.sort()
    word_frequency = {key: len(list(group)) for key, group in groupby(words)}
    word_freq_sorted = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
    
    most_used_word = word_freq_sorted[0][0]
    count = word_freq_sorted[0][1]

    print("The most used word in file {} is {}, used {} times.".format(
        file_source, most_used_word, count))

if __name__ == '__main__':
    main()
