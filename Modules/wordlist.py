# Auto Almost Everything
# Youtube Channel https://www.youtube.com/channel/UC4cNnZIrjAC8Q4mcnhKqPEQ
# Please read README.md carefully before use

import glob, os, random


def get():
    os.chdir('Wordlist\\')
    dicts = glob.glob('*.txt')
    wordlist = []
    for dict in dicts:
        f = open(dict, 'r', encoding='utf8')
        for line in f:
            wordlist.append(line.strip())
    os.chdir('..')
    return wordlist


def gen(wordlist):
    return ' '.join([wordlist[random.randint(0, len(wordlist))] for j in range(random.randint(1, 3))])
