import os
import sys
import pickle
import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

with open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/kg_whole.pickle','rb') as handle:
    kg = pickle.load(handle)

src = open('mention_test_nocopy.txt.shuffle.test.source.txt','r').readlines()
tgt = open('type_test_nocopy.txt.shuffle.test.target.txt','r').readlines()

#src = open('ex_src.txt','r').readlines()
#tgt = open('ex_tgt.txt','r').readlines()

total = 0
count = 0

for i,s in enumerate(src):
    s = s.split()
    t = tgt[i].split()

    j = 0
    l = 0
    r = 0
    total += (len(s)-1)
    while j + 1 < len(s):
        a = s[j]
        b = s[j+1]
        while r < len(t) and t[l][0] != '$':
            l += 1
        r = l + 1
        while r < len(t) and t[r][0] != '$':
            r += 1
        if l < len(t) and r < len(t) and l != r:
            try:
                vector1 = text_to_vector(' '.join(t[l+1:r]))
                vectors = [text_to_vector(text) for text in kg[a][b]]
                edges = [text for text in kg[a][b]]
                for i,vector in enumerate(vectors):
                    #print(get_cosine(vector1, vector))
                    if get_cosine(vector1, vector) > 0.6:
                        #print(vector1)
                        #print(vector)
                        #print('\n')
                        print(a)
                        print(b)
                        #print(t[l])
                        #print(t[r])
                        print(' '.join(t[l+1:r]))
                        print(edges[i])
                        print('\n')
                        count += 1
                        break
            except:
                pass
        j += 1
        l = r

print(count)
print(total)