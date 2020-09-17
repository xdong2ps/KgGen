import os
import sys
import pickle


ents = open('dataset_ents.txt','r').readlines()
ent_pairs = []
ent_pairs_train = open('/afs/crc.nd.edu/group/dmsquare/vol3/xdong2/graph2seq/nqgln/data/redistribute/QG/train/mention_train.txt.source.txt','r').readlines()
ent_pairs_dev = open('/afs/crc.nd.edu/group/dmsquare/vol3/xdong2/graph2seq/nqgln/data/redistribute/QG/dev/mention_dev.txt.shuffle.dev.source.txt','r').readlines()
ent_pairs_test = open('/afs/crc.nd.edu/group/dmsquare/vol3/xdong2/graph2seq/nqgln/data/redistribute/QG/test/mention_test.txt.shuffle.test.source.txt','r').readlines()
ent_pairs.extend(ent_pairs_train)
ent_pairs.extend(ent_pairs_dev)
ent_pairs.extend(ent_pairs_test)

with open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/kg_whole.pickle','rb') as handle:
    kg = pickle.load(handle)

total_pairs = set()
missing_nodes = set()
avg_cons = []
max_cons = 0
min_cons = 1000000
med = []
a = ''
b = ''

count = 0
for ent_pair in ent_pairs:
    ent_pair = ent_pair.split()
    #print(ent_pair)
    i = 0
    while i + 1 < len(ent_pair):
        total_pairs.add((ent_pair[i],ent_pair[i+1]))
        if ent_pair[i] not in kg:
            count += 1
            missing_nodes.add(ent_pair[i])
        else:
            if ent_pair[i+1] not in kg[ent_pair[i]]:
                count += 1
            else:
                if len(kg[ent_pair[i]][ent_pair[i+1]]) > max_cons:
                    max_cons = len(kg[ent_pair[i]][ent_pair[i+1]])
                    a = ent_pair[i]
                    b = ent_pair[i+1]
                if len(kg[ent_pair[i]][ent_pair[i+1]]) < min_cons:
                    min_cons = len(kg[ent_pair[i]][ent_pair[i+1]])
                avg_cons.append(len(kg[ent_pair[i]][ent_pair[i+1]]))
    
        i+=1

print(len(missing_nodes))
print(count)
print(len(total_pairs))
print(sum(avg_cons)/float(len(total_pairs)))
print(max_cons)
print(min_cons)
print(a)
print(b)
'''
for each in kg['million']['million']:
    if kg['million']['million'][each] > 10:
        print(each)
'''
#print(kg['million']['million'])

print('median')
print(sorted(avg_cons)[int(len(avg_cons)/2)])
#print(kg[a][b][:100])

'''
count = 0
for ent in ents:
    ent = ent.split()[0]
    #print(kg[eat])
    if ent not in kg:
        print(ent)
        count += 1

print(count)
'''
#print(kg['Security_Council'])