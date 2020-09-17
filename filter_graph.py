import os
import sys
import pickle

kg = {}
filtered = {}

with open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/kg_whole.pickle','rb') as handle:
    kg = pickle.load(handle)

found = False

for node in kg:
    for nb in kg[node]:
        if len(kg[node][nb]) > 5:
            if node not in filtered:
                filtered[node] = {}
            if nb not in filtered[node]:
                filtered[node][nb] = kg[node][nb]
        '''
        if len(kg[node][nb]) > 100:
            print(kg[node][nb])
            print(node)
            print(nb)
            found = True
            break
    if found == True:
        break
    '''

with open('/afs/crc.nd.edu/group/dmsquare/vol1/data/EngGigV5/corpus/kg_filtered.pickle','wb') as handle:
    pickle.dump(filtered,handle,protocol=pickle.HIGHEST_PROTOCOL)
