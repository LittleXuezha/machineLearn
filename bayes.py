import re
import numpy as np
data = [
    'Nobody owns the the water.',
    'the quick rabbit jumps fences',
    'buy pharmaceuticals now',
    'make quick money at the online casino',
    'the quick brown fox jumps',
]
result = [1, 1, 0, 0, 1]


def getwords(doc):
    splitter = re.compile(r'\W+')
    words = [s.lower() for s in splitter.split(doc) if len(s) > 2]
    return list(set(words))


def getAllWords(dataset):
    tempset = set([])
    for oneSet in dataset:
        tempset = tempset | set(oneSet)
    return sorted(list(tempset))


# 构建了所有特征
allwords = getAllWords([getwords(s) for s in data])

